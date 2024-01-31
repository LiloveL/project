import axios from 'axios'
// 前端向后端进行请求数据
const service = axios.create({
    baseURL : "http://127.0.0.1:8000/",
    timeout : 50000
})

export default service