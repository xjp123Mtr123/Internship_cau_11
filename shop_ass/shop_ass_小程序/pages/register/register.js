Page({
  data: {
    name: '',
    password: '',
    phone: '',
    email: ''
  },
  inputName: function(e) {
    this.setData({ name: e.detail.value });
  },
  inputPassword: function(e) {
    this.setData({ password: e.detail.value });
  },
  inputPhone: function(e) {
    this.setData({ phone: e.detail.value });
  },
  inputEmail: function(e) {
    this.setData({ email: e.detail.value });
  },
  register: function() {
    wx.request({
      url: 'http://43.142.142.224:8000/myapp/wx_register/', 
      data: {
        name: this.data.name,
        password: this.data.password,
        phone: this.data.phone,
        email: this.data.email
      },
      success: res => {
        if (res.data.status) {
          wx.showToast({
            title: '注册成功',
            icon: 'success',
            duration:5000
          });
          
          wx.navigateTo({
            url: '/pages/login/login'
          });
        } else {
          wx.showToast({
            title: '注册失败: ' + res.data.message,
            icon: 'none',
            duration:10000
          });
        }
      }
    });
  }
})
