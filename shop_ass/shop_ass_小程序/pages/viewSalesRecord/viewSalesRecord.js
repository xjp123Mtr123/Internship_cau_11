const app = getApp();
Page({
  data: {
    salesRecords: [],
    date:''
  },
 
  bindDateChange: function(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      date: e.detail.value
    })
    wx.request({
      url: 'http://'+app.globalData.ip+'/myapp/wx_GetSalesRecordByDateView/',
      data: { username: app.globalData.username,
        date:this.data.date
       },
      success: res => {
        if (res.data.status) {
          this.setData({ salesRecords: res.data.sales_records });
        }
      }
    });
  },
  onShow: function() {
    this.fetchSalesRecords();
  },
  navigateToAddSalesRecord: function() {
    wx.navigateTo({
      url: '/pages/addSalesRecord/addSalesRecord'
    });
  },
  fetchSalesRecords: function() {

    wx.request({
      url: 'http://'+app.globalData.ip+'/myapp/wx_GetSalesRecordView/',
      data: { username: app.globalData.username },
      success: res => {
        if (res.data.status) {
          this.setData({ salesRecords: res.data.sales_records });
        }
      }
    });
  }
});
