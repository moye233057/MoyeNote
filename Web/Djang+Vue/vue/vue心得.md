# 前端心得
一、部署到服务器需要注意的点
（1）注意路由文件router里的index.js中如果存在mode:history需要去掉
（2）如果前端文件中要静态图片，假设引用该图片的vue文件在component的下一级，需要将其路径修改为：“../../static/...”，用相对文件路径来理解。
没多一级加一个“../”，在nginx中配置加上：
location /static {
root /usr/share/nginx/html/打包文件名;
}
这样就能在一开始取到静态图片。

（3）npm run dev出现 'webpack-dev-server' 不是内部或外部命令，也不是可运行的程序错误时，运行：
npm install webpack(https://so.csdn.net/so/search?q=webpack&amp;spm=1001.2101.3001.7020)-dev-server --save-dev

（4）在vue中用router进行前端页面间的跳转
如果想要在下一个页面用this.$route.params.变量名的方法传递值
需要在路由中进行添加
首先在router文件夹的index.js文件中path要设置为path:'url/:id'
然后在源页面方法中的this.$route.push里的path需要添加对应的id
例如：
this.$router.push({path:'/thankyou/'+id});//跳到欢迎页
这样用户访问到的页面路由应为
域名+/~/thankyou/id
代表对应id的下一个动态页面，在下一个页面的vue文件中就可以这样获取id：
var id = this.$route.params.id

（5）在config文件夹中的index.js中，对build相关的默认api进行修改。
两个例子：
1、dev和build分开配置。
1.build中的proxy(XXX)里的target要变化
2.再添加（不知道是不是关键，但是可以添加上）：
chainWebpack和configureWebpack相关配置

constpath=require("path");
module.exports= {
 dev:{
   // Paths
   assetsSubDirectory:"static",
   assetsPublicPath:"/",
   proxyTable:{
     "/api":{
       target:"http://59.110.237.12:8007",
       changeOrigin:true
      }
    },

   // Various Dev Server settings
   host:"127.0.0.1",// can be overwritten by process.env.HOST
   port:8080,// can be overwritten by process.env.PORT, if port is in use, a free one will be determined
   autoOpenBrowser:false,
   errorOverlay:true,
   notifyOnErrors:true,
   poll:false,
   devtool:"cheap-module-eval-source-map",
   cacheBusting:true,
   cssSourceMap:true
  },

 build:{
   // Template for index.html
   index:path.resolve(__dirname,"../dist/index.html"),

   // Paths
   assetsRoot:path.resolve(__dirname,"../dist"),
   assetsSubDirectory:"static",
   assetsDir:"static",// 打包后静态资源目录，注意public文件下目录（别名）配置，index.html的icon路径
   assetsPublicPath:"/",
   proxy:{
     "/api":{
       target:"http://59.110.237.12:8007/",
       changeOrigin:true
      }
    },

   productionSourceMap:false,
   // https://webpack.js.org/configuration/devtool/#production
   devtool:"#source-map",

   // Gzip off by default as many popular static hosts such as
   // Surge or Netlify already gzip all static assets for you.
   // Before setting to `true`, make sure to:
   // npm install --save-dev compression-webpack-plugin
   productionGzip:false,
   productionGzipExtensions:["js","css"],

   // Run the build command with an extra argument to
   // View the bundle analyzer report after build finishes:
   // `npm run build --report`
   // Set to `true` or `false` to always turn it on or off
   bundleAnalyzerReport:process.env.npm_config_report,

   chainWebpack:config=>{
   // 添加别名（src默认为@，不用再次添加）
   config.resolve.alias
      .set('@pub',resolve('public'))// 设置public别名为@pub
    },
   configureWebpack:config=>{
     if(process.env.NODE_ENV==='production') {
       // 为生产环境修改配置...
       constterserWebpackPlugin=config.optimization.minimizer[0];
       const{terserOptions} =terserWebpackPlugin.options;
       terserOptions.compress.drop_console=true;
       terserOptions.compress.drop_debugger=true;
      }else{
       // 为开发环境修改配置...
      }
    }
  }
};**

2、只配置build
constpath=require('path');
constresolve= (dir)=>path.join(__dirname,dir);// 给public路径添加别名

constfs=require('fs')
 

module.exports= {
 publicPath:'./',//部署设置
 outputDir:'dist',
 assetsDir:"static",// 打包后静态资源目录，注意public文件下目录（别名）配置，index.html的icon路径
 devServer:{
   open:true,
   host:"localhost",
   port:8080,
   // https: false,
   // https: {  //开启https服务
   //   cert: fs.readFileSync(path.join(__dirname, '/build/ssl/cert.crt')),
   //   key: fs.readFileSync(path.join(__dirname, '/build/ssl/cert.key'))
   // },
   // before: app => {
   //   // 执行前操作，可以在此添加mock数据。与proxy代理不可并用
   //   app.get('/api/test', function (req, res) {
   //     let data = require('./src/mock/test.json')
   //     res.json(data)
   //   })
   // },
   proxy:{    //解决跨域
     '/api':{//将/api开头的请求加上target
         target:'http://59.110.237.12:8001',
         changeOrigin:true,//是否允许跨越
         // secure:false, //https要加这个
      }
    }
  },
 productionSourceMap:false,// 生产环境map文件
 chainWebpack:config=>{
   // 添加别名（src默认为@，不用再次添加）
   config.resolve.alias
      .set('@pub',resolve('public'))// 设置public别名为@pub
  },
 configureWebpack:config=>{
   if(process.env.NODE_ENV === 'production') {
     // 为生产环境修改配置...
     constterserWebpackPlugin=config.optimization.minimizer[0];
     const{terserOptions} =terserWebpackPlugin.options;
     terserOptions.compress.drop_console=true;
     terserOptions.compress.drop_debugger=true;
    }else{
     // 为开发环境修改配置...
    }
  }
}