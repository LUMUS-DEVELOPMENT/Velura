<script setup>
import { useAuthForm } from '@/composables/useAuthForm.js'

const { form, errors, submitted, submit } = useAuthForm([
    'name',
    'email',
    'password',
    'confirmPassword'
])

const register = (e) => {
    e.preventDefault()
    submit((data) => console.log('Register submitted', data))
}
</script>

<template>
    <div class="min-h-screen flex items-center justify-center bg-gray-50 p-4">
        <Form title="Register" @submit="register">
            <Input
                v-model="form.name"
                label="Full Name"
                :error="submitted.value ? errors.value.name : ''"
            />

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

            <Input
                v-model="form.confirmPassword"
                label="Confirm Password"
                type="password"
                :error="submitted.value ? errors.value.confirmPassword : ''"
            />

            <Button  class="mt-4">
                Register
            </Button>
        </Form>
    </div>
</template>
