Page({
  data: {
    name: '',
    sname: '',
    // 其他字段
  },
  onLoad: function(options) {
    // 加载用户信息
    this.loadUserInfo();
  },
  loadUserInfo: function() {
    const app = getApp();
    // 假设有一个方法获取当前用户信息
    const userInfo = app.getUserInfo();
    this.setData({
      name: userInfo.name,
      sname: userInfo.sname,
      // 其他字段
    });
  },
  inputName: function(e) {
    this.setData({ name: e.detail.value });
  },
  inputSname: function(e) {
    this.setData({ sname: e.detail.value });
  },
  // 其他字段的input函数
  updateUserInfo: function() {
    const app = getApp();
    wx.request({
      url: 'http://127.0.0.1:8000/myapp/wx_UpdateUserInfoView/',
      data: {
        username: app.globalData.username,
        name: this.data.name,
        sname: this.data.sname,
        // 其他字段
      },
      success: res => {
        if (res.data.status) {
          wx.showToast({ title: '信息更新成功' });
          // 可以添加跳转或其他逻辑
        }
      }
    });
  }
});
