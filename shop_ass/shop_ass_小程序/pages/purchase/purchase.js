var app =getApp();

Page({
  data: {
    stockList: [],
    searchQuery: '',
    
  },
  onLoad: function() {

  },
  onShow:function(){
    this.fetchStockList();
  },
  inputSearch: function(e) {
    this.setData({ searchQuery: e.detail.value });
  },
  searchStock: function() {
    
    console.log(app.globalData.username); // 访问全局变量

    wx.request({
      method: 'GET',
      header: {
        'Content-Type': 'application/json'
      },
      url: 'http://127.0.0.1:8000/myapp/wx_SearchStockView/',
      header: {
        'Content-Type': 'application/json'
      },
      data: { query: this.data.searchQuery ,
              username:app.globalData.username
      },
      success: res => {
        if (res.data.status) {
          this.setData({ stockList: res.data.stockList });
        }
      }
    });
  },
  fetchStockList: function() {
    wx.request({
      method: 'GET',
      header: {
        'Content-Type': 'application/json'
      },
      url: 'http://127.0.0.1:8000/myapp/wx_GetStockListView/',
      data: { query: '',
              username:app.globalData.username
       },
      success: res => {
        if (res.data.status) {
          this.setData({ stockList: res.data.stockList });
        }
      }
    });
  },
  navigateToAddPurchase: function() {
    wx.navigateTo({
      url: '/pages/addPurchase/addPurchase'
    });
  }
})
