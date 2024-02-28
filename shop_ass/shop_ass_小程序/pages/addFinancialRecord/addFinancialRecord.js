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
      url: 'http://43.142.142.224:8000/myapp/wx_AddFinancialRecordView/',
      data: {
        username: app.globalData.username,
        item_name: this.data.itemName,
        amount: this.data.amount
      },
      success: res => {
        if (res.data.status) {
          wx.showToast({ title: '财务记录添加成功' });
          // 可以添加跳转或其他逻辑
        }
      }
    });
  }
});
