import { reactive, ref, computed, watch } from 'vue'
import { useRules } from "@/composables/useRules.js"

export function useAuthForm(fields, fieldRules = {}) {
    const { rules, getLang } = useRules()

    const createReactive = (initial) => reactive(Object.fromEntries(fields.map(f => [f, initial])))

    const form = createReactive('')
    const errors = createReactive('')
    const touched = createReactive(false)
    const submitted = ref(false)

    const getValidators = (validators) => {
        return validators.map(v => {
            if (typeof v === 'string') return rules.value[v]
            if (Array.isArray(v) && typeof v[0] === 'string') {
                return rules.value[v[0]](v[1])
            }
            if (v.name === undefined && v.toString().includes('form')) {
                Object.defineProperty(v, 'name', { value: 'matchValidator' })
            }
            return v
        })
    }

    const validateField = (key) => {
        const validators = getValidators(fieldRules[key] || [])
        for (let rule of validators) {
            errors[key] = rule(form[key], form, getLang())
            if (errors[key]) break
        }
    }

    const validateAll = () => fields.forEach(validateField)

    watch(getLang, validateAll)

    fields.forEach(key => {
        watch(() => form[key], () => {
            if (touched[key] || submitted.value) validateField(key)
            fields.forEach(f => {
                const validators = getValidators(fieldRules[f] || [])
                if (validators.some(v => v.name === 'matchValidator')) {
                    validateField(f)
                }
            })
        })
    })

    const isValid = computed(() => Object.values(errors).every(e => e === ''))

    const touch = (key) => {
        touched[key] = true
        validateField(key)
    }

    const submit = (callback) => {
        submitted.value = true
        validateAll()
        if (!isValid.value) return
        callback({ ...form })
    }

    return { form, errors, touched, submitted, isValid, touch, submit, getLang }
}
