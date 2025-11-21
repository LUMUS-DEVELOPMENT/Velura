import { reactive, computed } from 'vue'

const state = reactive({ lang: 'en' })

const messages = {
    en: {
        required: 'This field is required',
        email: 'Invalid email',
        minLength: (len) => `Must be at least ${len} characters`,
        maxLength: (len) => `Must be at most ${len} characters`,
        match: 'Password fields do not match',
        accepted: 'You must accept the terms'

    },
    ru: {
        required: 'Поле обязательно',
        email: 'Неверный email',
        minLength: (len) => `Минимум ${len} символов`,
        maxLength: (len) => `Максимум ${len} символов`,
        match: 'Пароли не совпадают',
        accepted: 'Вы должны принять условия'
    }
}

export function useRules() {
    const rules = computed(() => ({
        required: (v) => (v ? '' : messages[state.lang].required),
        email: (v) =>
            /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) ? '' : messages[state.lang].email,
        minLength: (len) => (v) =>
            v.length >= len ? '' : messages[state.lang].minLength(len),
        maxLength: (len) => (v) =>
            v.length <= len ? '' : messages[state.lang].maxLength(len),
        match: (otherField) => (v, form) =>
            v === form[otherField] ? '' : messages[state.lang].match,
        accepted: (v) => (v ? '' : messages[state.lang].accepted)
    }))

    const setFormLang = (newLang) => {
        if (messages[newLang]) state.lang = newLang
    }

    const getLang = () => state.lang

    return { rules, setFormLang, getLang }
}
