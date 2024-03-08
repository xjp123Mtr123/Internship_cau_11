const app = getApp();
Page({
  data: {
    financialRecords: [],
    totalMoney:0,
    totalSaleMoney:0,
    date:'',
  },
  
  bindDateChange: function(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      date: e.detail.value
    })
    wx.request({
      url: 'http://'+app.globalData.ip+'/myapp/wx_GetFinancialRecordByDateView/',
      data: { username: app.globalData.username,
              date:this.data.date
       },
      success: res => {
        if (res.data.status) {
          this.setData({ financialRecords: res.data.financial_records });
          this.setData({totalMoney: res.data.totalMoney});
          this.setData({totalSaleMoney: res.data.totalSaleMoney});
        }
      }
    });
  },

  
  
  onShow: function() {
    this.fetchFinancialRecords();
  },
  fetchFinancialRecords: function() {

    wx.request({
      url: 'http://'+app.globalData.ip+'/myapp/wx_GetFinancialRecordView/',
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
