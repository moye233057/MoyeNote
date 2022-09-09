# 前端向后端传递数据，Django后端如何获取？
一、第一种方法（添加了请求超时时间）：
假设：1.js、2.js、3.js都放在同一个文件夹
前端：
//1、配置axios的请求拦截(1.js)
import axios from 'axios'
const service = axios.create({
    timeout: 600000, // 链接超时  当发送时间超过10分钟就不再发送了
    transformRequest: [function (data) {
        return qs.stringify(data) // 将对象或者数组序列化成URL的格式
    }],
})

// 以下两个是对axios对象进行登录访问限制，作用：
// 1.通过存储在浏览器session里的值判断是否已登录，
// 2.通过后端的信息进行路由跳转
// 添加请求拦截器
service.interceptors.request.use(function (config) {
    console.log('请求数据', config)
    let token = window.sessionStorage.getItem('token')
    let username = window.sessionStorage.getItem('username')
    // console.log(token)
    if (token) { //已登陆
        config.headers['X-Token'] = token
        config.headers['username'] = username
    }
    return config;
}, function (error) {
    console.log(error);
    // 对请求错误做些什么
    return Promise.reject('请求错误', error);
});

// 添加响应拦截器
service.interceptors.response.use(function (response) {
    console.log('响应数据', response);
    if (response.data.msg == "该账号被其它用户登录，请重新登录" || response.data.msg == "该账号未登录") {
        window.sessionStorage.setItem('isLogin', false)
        //跳转至登录界面
        router.push({
            path: "/login",
            query: {
                logout: response.data.msg
            }
        });
    }
    // 对响应数据做点什么
    return response;
}, function (error) {
    console.log(error);
    // 对响应错误做点什么
    return Promise.reject('响应错误', error);
});

export default service


//2、配置基础路由(2.js)
const base = {
    trizhi: "http://59.110.237.12:8000"
}
export default base


//3、构建所有api的路径(3.js)
import service from './1'
import base from './2'
const apis = {
        //注册用户
        registUser(data){
            return service.post(`${base.trizhi}/api/admin/registUser/`,data);
        },
    }
export default apis
