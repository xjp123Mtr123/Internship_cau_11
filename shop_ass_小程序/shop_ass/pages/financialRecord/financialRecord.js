Page({
  data: {
    financialRecords: []
  },
  onLoad: function() {
    this.fetchFinancialRecords();
  },
  fetchFinancialRecords: function() {
    const app = getApp();
    wx.request({
      url: 'http://43.142.142.224:8000/myapp/wx_GetFinancialRecordView/',
      data: { username: app.globalData.username },
      success: res => {
        if (res.data.status) {
          this.setData({ financialRecords: res.data.financial_records });
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
