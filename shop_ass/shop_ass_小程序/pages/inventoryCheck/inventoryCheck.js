Page({
  data: {
    stocks: []
  },
  onLoad: function() {
    this.fetchStocks();
  },
  fetchStocks: function() {
    const app = getApp();
    wx.request({
      url: 'http://43.142.142.224:8000/myapp/wx_StockListView/',
      data: { 
        username:app.globalData.username
      },
      success: res => {
        if (res.data.status) {
          this.setData({ stocks: res.data.stocks });
        }
      }
    });
  }
})
