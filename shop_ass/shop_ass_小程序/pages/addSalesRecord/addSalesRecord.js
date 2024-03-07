var app =getApp();
Page({
  data: {
    stockList: [],
    productName: '',
    quantity: '',
    salePrice: '',
    costPrice: '',
    searchQuery: ''
  },
  onShow:function(){
    this.fetchStockList();
  },
  inputSearch: function(e) {
    this.setData({ searchQuery: e.detail.value });
  },
  inputProductName: function(e) {
    this.setData({ productName: e.detail.value });
  },
  inputQuantity: function(e) {
    this.setData({ quantity: e.detail.value });
  },
  inputSalePrice: function(e) {
    this.setData({ salePrice: e.detail.value });
  },
  inputCostPrice: function(e) {
    this.setData({ costPrice: e.detail.value });
  },
  admitStock: function(e) {
    this.setData({ productName: e.currentTarget.dataset.product_name });
    this.setData({ quantity: e.currentTarget.dataset.quantity });
    this.setData({ costPrice: e.currentTarget.dataset.price });
 
  },
  searchStock: function() {
    
    console.log(app.globalData.username); // 访问全局变量

    wx.request({
      method: 'GET',
      header: {
        'Content-Type': 'application/json'
      },
      url: 'http://8.146.209.237:8000/myapp/wx_SearchStockView/',
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
      url: 'http://8.146.209.237:8000/myapp/wx_GetStockListView/',
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
  addSalesRecord: function() {
    const app = getApp();
    wx.request({
      url: 'http://8.146.209.237:8000/myapp/wx_AddSalesRecordView/',
      data: {
        username: app.globalData.username,
        product_name: this.data.productName,
        quantity: this.data.quantity,
        sale_price: this.data.salePrice,
        cost_price: this.data.costPrice
      },
      success: res => {
        if (res.data.status) {
          wx.showToast({ title: '销售记录添加成功' });
          // 可以添加跳转或其他逻辑
          wx.navigateBack(); // 返回库存列表页面
        }else{
          wx.showToast({ title: '请勿超出库存数量！',
          icon: 'none',
          duration: 1000 });
        }
      }
    });
  }
});