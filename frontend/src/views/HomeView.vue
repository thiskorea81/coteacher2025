<template>
  <div class="home">
    <h1>Welcome to Coteacher</h1>
    <p>
      이 페이지는 Coteacher 앱의 메인(Home) 페이지입니다.
      <br />
      일정, 할일, 성적 관리 등 다양한 기능으로 이동하려면
      상단/좌측 메뉴(또는 아래 버튼)를 활용하세요.
    </p>

    <!-- 예시: Tasks 페이지로 이동하는 버튼 -->
    <button @click="goToTasks">
      Go to Tasks
    </button>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

// Vue Router 사용
const router = useRouter()

function goToTasks() {
  router.push({ name: 'tasks' })
}
</script>

<style scoped>
.home {
  text-align: center;
  margin-top: 40px;
}
button {
  margin-top: 20px;
  padding: 10px 20px;
}
</style>
