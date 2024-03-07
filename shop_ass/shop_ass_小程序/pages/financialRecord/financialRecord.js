Page({
  data: {
    financialRecords: [],
    totalMoney:0,
    totalSaleMoney:0
  },
  onShow: function() {
    this.fetchFinancialRecords();
  },
  fetchFinancialRecords: function() {
    const app = getApp();
    wx.request({
      url: 'http://127.0.0.1:8000/myapp/wx_GetFinancialRecordView/',
      data: { username: app.globalData.username },
      success: res => {
        if (res.data.status) {
          this.setData({ financialRecords: res.data.financial_records });
          this.setData({totalMoney: res.data.totalMoney});
          this.setData({totalSaleMoney: res.data.totalSaleMoney});
        }
      }
    });
  },
  navigateToAddFinancialRecord: function() {
    wx.navigateTo({
      url: '/pages/addFinancialRecord/addFinancialRecord'
    });
  }
});
