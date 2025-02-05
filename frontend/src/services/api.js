import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000', // 백엔드 FastAPI 서버 주소
  headers: {
    'Content-Type': 'application/json'
  }
});

export default apiClient;
