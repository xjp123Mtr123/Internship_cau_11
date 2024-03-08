var app =getApp();
Page({
  data: {
    username: '',
    password: ''
  },
  inputUsername: function(e) {
    this.setData({ username: e.detail.value });
  },
  inputPassword: function(e) {
    this.setData({ password: e.detail.value });
  },
  // 新增跳转到注册页面的函数
navigateToRegister: function() {
  wx.navigateTo({
    url: '/pages/register/register' // 确保你有一个名为 register 的页面
  });
},
  // 登录页面的 login 函数
login: function() {
  wx.request({
    url: 'http://'+app.globalData.ip+'/myapp/wx_login/', 
    data: {
      username: this.data.username,
      password: this.data.password
    },
    success: res => {
      if (res.data.status) {
        wx.showToast({
          title: '登录成功',
          icon: 'success',
          duration: 10000
        });

        // 更新全局变量
        const app = getApp();
        app.globalData.username = this.data.username;
        wx.navigateTo({
          url: '/pages/index/index'
        });
        // 进行其他操作，例如页面跳转
      } else {
        wx.showToast({
          title: '登录失败',
          icon: 'none',
          duration: 10000
        });
      }
    }
  });
}

})
