<script setup>
import Signup  from './components/Signup.vue'
import Login  from './components/Login.vue'
import Logout  from './components/Logout.vue'

const routes = {
  '/': Home,
  '/login': 로그인,
  '/signup': 회원가입
}

const currentPath = ref(window.location.hash)

window.addEventListener('hashchange', () => {
  currentPath.value = window.location.hash
})

const currentView = computed(() => {
  return routes[currentPath.value.slice(1) || '/'] || NotFound
})
</script>

<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <a href="#/">Home</a> |
        <a href="#/signup">회원가입</a> |
        <a href="#/login">로그인</a> 
      </div>
      <div class="col-6">
        <component :is="currentView" />
        <Logout />
      </div>
      <div class="col">
        3 of 3
      </div>
    </div>
  </div>
</template>>

<style scoped>
.container {
  
}

</style>
