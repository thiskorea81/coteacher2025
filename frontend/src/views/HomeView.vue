<template>
  <div>
    <h1>교사 도우미 홈</h1>
    <button @click="getMessage">백엔드 메시지 가져오기</button>
    <p>{{ message }}</p>
  </div>
</template>

<script>
import apiClient from '@/services/api';

export default {
  name: 'Home',
  data() {
    return {
      message: ''
    }
  },
  methods: {
    async getMessage() {
      try {
        const response = await apiClient.get('/');
        this.message = response.data.message;
      } catch (error) {
        console.error(error);
      }
    }
  }
}
</script>
