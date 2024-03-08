Page({
  data: {
    financialRecords: [],
    totalMoney:0,
    totalSaleMoney:0
  },
  
  data:{
    date:'2021-01-01',
  },
  bindDateChange: function(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      date: e.detail.value
    })
  },
  
  
  onShow: function() {
    this.fetchFinancialRecords();
  },
  fetchFinancialRecords: function() {
    const app = getApp();
    wx.request({
      url: 'http://8.146.209.237:8000/myapp/wx_GetFinancialRecordView/',
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
