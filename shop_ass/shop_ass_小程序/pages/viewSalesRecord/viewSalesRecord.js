Page({
  data: {
    salesRecords: []
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
    const app = getApp();
    wx.request({
      url: 'http://8.146.209.237:8000/myapp/wx_GetSalesRecordView/',
      data: { username: app.globalData.username },
      success: res => {
        if (res.data.status) {
          this.setData({ salesRecords: res.data.sales_records });
        }
      }
    });
  }
});
