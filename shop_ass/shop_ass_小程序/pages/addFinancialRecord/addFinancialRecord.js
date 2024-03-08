Page({
  data: {
    itemName: '',
    amount: 0
  },
  inputItemName: function(e) {
    this.setData({ itemName: e.detail.value });
  },
  inputAmount: function(e) {
    this.setData({ amount: e.detail.value });
  },
  addFinancialRecord: function() {
    const app = getApp();
    wx.request({
      url: 'http://'+app.globalData.ip+'/myapp/wx_AddFinancialRecordView/',
      data: {
        username: app.globalData.username,
        item_name: this.data.itemName,
        amount: this.data.amount
      },
      success: res => {
        if (res.data.status) {
          wx.showToast({ title: '财务记录添加成功' });
          // 可以添加跳转或其他逻辑
          wx.navigateBack(); // 返回库存列表页面
        }
      }
    });
  }
});
