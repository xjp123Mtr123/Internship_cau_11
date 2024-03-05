Page({
  data: {
    productName: '',
    category: '',
    quantity: '',
    price: ''
  },
  onLoad: function(options) {
    this.setData({ productName: options.productName });
    this.setData({category:options.category});
    this.setData({price:options.price});
  },
  inputProductName: function(e) {
    this.setData({ productName: e.detail.value });
  },
  inputCategory: function(e) {
    this.setData({ category: e.detail.value });
  },
  inputQuantity: function(e) {
    this.setData({ quantity: e.detail.value });
  },
  inputPrice: function(e) {
    this.setData({ price: e.detail.value });
  },
  submitPurchase: function() {
    const app = getApp();

    
    wx.request({
      method: 'GET',
      header: {
        'Content-Type': 'application/json'
      },
      url: 'http://127.0.0.1:8000/myapp/wx_AddPurchaseView/',

      data: {
        username: app.globalData.username,
        productName: this.data.productName,
        category: this.data.category,
        quantity: this.data.quantity,
        price: this.data.price
      },
      success: res => {
        if (res.data.status) {
          wx.showToast({  
            title: '进货信息添加成功',
            icon: 'success'
          });
          // wx.navigateTo({
          //   url: '/pages/purchase/purchase'
          // });
          wx.navigateBack()
        } else {
          wx.showToast({
            title: '添加失败',
            icon: 'none'
          });
        }
      }
    });
  }
})
