<script setup>
import { useAuthForm } from '@/composables/useAuthForm.js'
import {useRules} from "@/composables/useRules.js";


const { form, errors, touched, submitted, isValid, touch, submit } = useAuthForm(
    ['email', 'password'],
    {
        email: ['required', 'email'],
        password: ['required', ['minLength', 6]]
    }
)

const login = () => {
    submit((data) => {
        console.log('Login submitted', data)
    })
}
</script>

<template>
    <div class="min-h-screen flex items-center justify-center bg-gray-50 p-4">
        <Form
            title="Sign In"
            :submitted="submitted"
            @submit="login"
        >

            <Input
                v-model="form.email"
                label="Email"
                :error="errors.email"
                :touched="touched.email"
                :submitted="submitted"
                @blur="touch('email')"
            />

            <Input
                v-model="form.password"
                type="password"
                label="Password"
                :error="errors.password"
                :touched="touched.password"
                :submitted="submitted"
                @blur="touch('password')"
            />

            <Button type="submit" :disabled="!isValid">
                Sign In
            </Button>

        </Form>
    </div>
</template>
