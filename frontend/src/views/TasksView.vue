<template>
    <div>
      <h2>Task List</h2>
      <ul>
        <li v-for="task in taskStore.tasks" :key="task.id">
          {{ task.title }} - {{ task.is_done ? "Done" : "Not Done" }}
        </li>
      </ul>
  
      <!-- 새 Task 추가 폼 -->
      <form @submit.prevent="onSubmit">
        <input v-model="newTitle" placeholder="Task Title" />
        <input v-model="newDesc" placeholder="Task Description" />
        <button type="submit">Add Task</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useTaskStore } from '../stores/taskStore.js'
  
  // Pinia 스토어 불러오기
  const taskStore = useTaskStore()
  
  // 폼 입력 값
  const newTitle = ref('')
  const newDesc = ref('')
  
  // 컴포넌트 로드 시, 백엔드에서 Task 목록 불러오기
  onMounted(() => {
    taskStore.fetchTasks()
  })
  
  // 폼 전송 핸들러
  const onSubmit = async () => {
    // Store 액션 호출
    await taskStore.createTask({
      title: newTitle.value,
      description: newDesc.value,
    })
  
    // 입력 필드 초기화
    newTitle.value = ''
    newDesc.value = ''
  }
  </script>
  
  <style scoped>
  /* 선택적으로 스타일 추가 */
  </style>
  