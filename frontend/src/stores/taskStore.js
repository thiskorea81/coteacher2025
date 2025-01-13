import { defineStore } from 'pinia'
import axios from 'axios'

export const useTaskStore = defineStore('task', {
  state: () => ({
    tasks: [],
  }),
  actions: {
    async fetchTasks() {
      try {
        const res = await axios.get('http://127.0.0.1:8000/api/tasks')
        this.tasks = res.data
      } catch (err) {
        console.error(err)
      }
    },
    async createTask(payload) {
      try {
        await axios.post('http://127.0.0.1:8000/api/tasks', payload)
        await this.fetchTasks()
      } catch (err) {
        console.error(err)
      }
    },
    // 수정, 삭제 등 추가 가능
  },
})
