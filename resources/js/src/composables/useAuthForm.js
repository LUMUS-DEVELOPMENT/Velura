import { reactive, computed, ref } from 'vue'

export function useAuthForm(fields) {
    const form = reactive(Object.fromEntries(fields.map(f => [f, ''])))
    const submitted = ref(false)

    const errors = computed(() => {
        const errs = {}

        if (fields.includes('name') && !form.name) errs.name = 'Name is required'

        if (fields.includes('email')) {
            if (!form.email) errs.email = 'Email is required'
            else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email)) errs.email = 'Email is invalid'
        }

        if (fields.includes('password')) {
            if (!form.password) errs.password = 'Password is required'
            else if (form.password.length < 6) errs.password = 'Password must be at least 6 characters'
        }

        if (fields.includes('confirmPassword')) {
            if (!form.confirmPassword) errs.confirmPassword = 'Confirm Password is required'
            else if (form.confirmPassword !== form.password) errs.confirmPassword = 'Passwords do not match'
        }

        return errs
    })

    const isValid = computed(() => Object.keys(errors.value).length === 0)

    const submit = (callback) => {
        submitted.value = true
        if (!isValid.value) return
        callback({ ...form })
    }

    return { form, errors, submitted, isValid, submit }
}
