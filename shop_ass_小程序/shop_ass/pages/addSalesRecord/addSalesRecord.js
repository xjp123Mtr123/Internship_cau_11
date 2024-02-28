Page({
  data: {
    productName: '',
    quantity: '',
    salePrice: '',
    costPrice: ''
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
  addSalesRecord: function() {
    const app = getApp();
    wx.request({
      url: 'http://43.142.142.224:8000/myapp/wx_AddSalesRecordView/',
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
        }
      }
    });
  }
});