<script setup>
import {useAuthForm} from '@/composables/useAuthForm.js'
import Checkbox from "@/components/ui/base/Checkbox.vue";


const { form, errors, touched, submitted, isValid, touch, submit } = useAuthForm(
    ['name', 'email', 'password', 'confirmPassword', 'remember'],
    {
        name: ['required'],
        email: ['required', 'email'],
        password: ['required', ['minLength', 6],['maxLength', 12]],
        confirmPassword: ['required', ['match', 'password']],
        remember: []
    }
)

const register = () => {
    submit((data) => {
        console.log('Register submitted', data)
    })
}
</script>

<template>
    <div class="min-h-screen flex items-center justify-center bg-gray-50 p-4">
        <Form
            title="Register"
            :submitted="submitted"
            @submit="register"
        >

            <Input
                v-model="form.name"
                label="Name"
                :error="errors.name"
                :touched="touched.name"
                :submitted="submitted"
                @blur="touch('name')"
            />

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

            <Input
                v-model="form.confirmPassword"
                type="password"
                label="Confirm Password"
                :error="errors.confirmPassword"
                :touched="touched.confirmPassword"
                :submitted="submitted"
                @blur="touch('confirmPassword')"
            />

            <Checkbox
                v-model="form.remember"
                label="Remember me"
            />

            <Button type="submit" :disabled="!isValid">
                Register
            </Button>

        </Form>
    </div>
</template>
