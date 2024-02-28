Page({
  data: {
    id: null,
    quantity: '',
    price: ''
  },
  onLoad: function(options) {
    this.setData({ id: options.id });
    this.fetchStockDetail();
  },
  fetchStockDetail: function() {
    wx.request({
      url: `http://43.142.142.224:8000/myapp/wx_StockDetailView/${this.data.id}/`,
      success: res => {
        if (res.data.status) {
          this.setData({
            quantity: res.data.stock.quantity,
            price: res.data.stock.price
          });
        }
      }
    });
  },
  inputQuantity: function(e) {
    this.setData({ quantity: e.detail.value });
  },
  inputPrice: function(e) {
    this.setData({ price: e.detail.value });
  },
  updateStock: function() {
    const app = getApp();
    console.log(app.globalData.username); // 访问全局变量
    wx.request({
      url: `http://43.142.142.224:8000/myapp/wx_UpdateStockView/?quantity=${this.data.quantity}&price=${this.data.price}`,
      data: { pk: this.data.id ,
              username:app.globalData.username
      },
      success: res => {
        if (res.data.status) {
          wx.showToast({ title: '更新成功' });
          wx.navigateBack(); // 返回库存列表页面
        }
      }
    });
  }
})
Page({
  data: {
    id: null,
    quantity: '',
    price: ''
  },
  onLoad: function(options) {
    this.setData({ id: options.id });
    this.fetchStockDetail();
  },
  fetchStockDetail: function() {
    wx.request({
      url: `http://43.142.142.224:8000/stock/${this.data.id}/`,
      success: res => {
        if (res.data.status) {
          this.setData({
            quantity: res.data.stock.quantity,
            price: res.data.stock.price
          });
        }
      }
    });
  },
  inputQuantity: function(e) {
    this.setData({ quantity: e.detail.value });
  },
  inputPrice: function(e) {
    this.setData({ price: e.detail.value });
  },
  updateStock: function() {
    wx.request({
      url: `http://43.142.142.224:8000/stock/update/${this.data.id}/?quantity=${this.data.quantity}&price=${this.data.price}`,
      success: res => {
        if (res.data.status) {
          wx.showToast({ title: '更新成功' });
          wx.navigateBack(); // 返回库存列表页面
        }
      }
    });
  }
})
