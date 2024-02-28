Page({
  data: {
    salesRecords: []
  },
  onLoad: function() {
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
      url: 'http://43.142.142.224:8000/myapp/wx_GetSalesRecordView/',
      data: { username: app.globalData.username },
      success: res => {
        if (res.data.status) {
          this.setData({ salesRecords: res.data.sales_records });
        }
      }
    });
  }
});
