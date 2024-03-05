Page({
  data: {
    stocks: [],
    updatedQuantity: '', // 用户输入的更新数量
    updatedPrice: '' // 用户输入的更新价格
  },
  onLoad: function() {
    // this.fetchStocks();
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
  },
  navigateToUpdateStock: function(e) {
    const id = e.currentTarget.dataset.id;
    const quantity=e.currentTarget.dataset.quantity;
    const price=e.currentTarget.dataset.price;
    wx.navigateTo({
      url: '/pages/updateStock/updateStock?id=' + id+'&quantity='+quantity+'&price='+price
    });
    
  },
  deleteStock: function(e) {
    const app = getApp();
    const id = e.currentTarget.dataset.id;
    wx.request({
      url: `http://127.0.0.1:8000/myapp/wx_DeleteStockView/`,
      data: { pk: id ,
        username:app.globalData.username
},
      success: res => {
        if (res.data.status) {
          wx.showToast({ title: '删除成功' });
          this.fetchStocks(); // 重新加载库存
        }
      }
    });
  }
})
