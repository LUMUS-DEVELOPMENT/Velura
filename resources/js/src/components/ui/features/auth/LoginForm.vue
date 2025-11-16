<script setup>
import { useAuthForm } from '@/composables/useAuthForm.js'

const { form, errors, submitted, submit } = useAuthForm(['email', 'password'])

const login = (e) => {
    e.preventDefault()
    submit((data) => console.log('Login submitted', data))
}
</script>

<template>
    <div class="min-h-screen flex items-center justify-center bg-gray-50 p-4">
        <Form title="Sign In" @submit="login">
            <Input
                v-model="form.email"
                label="Email"
                :error="submitted.value ? errors.value.email : ''"
            />
            <Input
                v-model="form.password"
                label="Password"
                type="password"
                :error="submitted.value ? errors.value.password : ''"
            />
            <Button  class="mt-4">
                Sign In
            </Button>
        </Form>
    </div>
</template>
