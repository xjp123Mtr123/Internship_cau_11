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
      url: 'http://'+app.globalData.ip+'/myapp/wx_SearchStockView/',
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
      url: 'http://'+app.globalData.ip+'/myapp/wx_GetStockListView/',
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
  navigateToAddSamePurchase: function(e) {
    const productName = e.currentTarget.dataset.product_name;
    const category=e.currentTarget.dataset.category;
    const price=e.currentTarget.dataset.price;
    const warnNum=e.currentTarget.dataset.warn_num;
    wx.navigateTo({
      url: '/pages/addPurchase/addPurchase?status=true&productName=' + productName+'&category='+category+'&price='+price+'&warnNum='+warnNum
    });
  },
  navigateToAddPurchase: function() {
    wx.navigateTo({
      url: '/pages/addPurchase/addPurchase'
    });
  }
})
