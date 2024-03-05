Page({
  data: {
    stocks: []
  },
  onShow:function(){
    this.fetchStocks(); // 重新加载库存
  },
  fetchStocks: function() {
    const app = getApp();
    wx.request({
      url: 'http://127.0.0.1:8000/myapp/wx_StockListView/',
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
