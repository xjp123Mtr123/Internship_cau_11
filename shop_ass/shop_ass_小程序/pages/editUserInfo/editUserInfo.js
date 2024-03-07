const app = getApp();
Page({
  data: {
    name: '',
    phone: '',
    email:'',
    password:'',
    newPassword:''
    // 其他字段
  },
  onLoad: function(options) {
    // 加载用户信息
    this.loadUserInfo();
  },
  loadUserInfo: function() {

      wx.request({
        url: 'http://8.146.209.237:8000/myapp/wx_GetUserInfoView/',
        data: {
          username: app.globalData.username,
        },
        success: res => {
          if (res.data.status) {
            this.setData({
              name: app.globalData.username,
              phone:res.data.phone,
              email: res.data.email,
              // 其他字段
            });

          }
        }
      });
   
  },
  
  inputName: function(e) {
    this.setData({ name: e.detail.value });
  },
  inputPhone: function(e) {
    this.setData({ phone: e.detail.value });
  },
  inputEmail: function(e) {
    this.setData({ email: e.detail.value });
  },
  inputPassword: function(e) {
    this.setData({ password: e.detail.value });
  },
  inputNewPassword: function(e) {
    this.setData({ newPassword: e.detail.value });
  },
  // 其他字段的input函数
  updateUserInfo: function() {
    wx.request({
      url: 'http://8.146.209.237:8000/myapp/wx_UpdateUserInfoView/',
      data: {
        username: app.globalData.username,
        phone: this.data.phone,
        email: this.data.email,
        password:this.data.password,
        newPassword:this.data.newPassword,
        // 其他字段
      },
      success: res => {
        if (res.data.status) {
          wx.showToast({ title: '信息更新成功' });
          // 可以添加跳转或其他逻辑
        }else{
          wx.showToast({ title: '信息更新失败' });
        }
      }
    });
  }
});
