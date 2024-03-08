// log_out/log_out.js
Page({

  /**
   * 页面的初始数据
   */
  data: {

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    wx.showModal({
      title: '提示',
      content: '请注意查询今日销售记录',
      success (res) {
        if (res.confirm) {
          console.log('用户点击确定')
        } else if (res.cancel) {
          console.log('用户点击取消')
        }
      }
    })
    

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {

  },
  // 新增跳转到进货页面的函数
  navigateToPurchase: function() {
    wx.navigateTo({
      url: '/pages/purchase/purchase' 
    });
  },
  navigateToinventoryCheck: function() {
    wx.navigateTo({
      url: '/pages/inventoryCheck/inventoryCheck' 
    });
  },
  navigateTostockList: function() {
    wx.navigateTo({
      url: '/pages/stockList/stockList'
    });
  },
  navigateToviewSalesRecord: function() {
    wx.navigateTo({
      url: '/pages/viewSalesRecord/viewSalesRecord' 
    });
  },

  navigateTofinancialRecord: function() {
    wx.navigateTo({
      url: '/pages/financialRecord/financialRecord' 
    });
  },
  navigateToeditUserInfo: function() {
    wx.navigateTo({
      url: '/pages/editUserInfo/editUserInfo' 
    });
  },
  logout: function() {
    wx.navigateTo({
      url: '/pages/login/login' 
    });
  },
  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {

  }
})