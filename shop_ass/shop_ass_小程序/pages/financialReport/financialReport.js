Page({
  data: {
    financialData: []
  },

  onReady: function () {
    this.fetchFinancialData();
  },

  fetchFinancialData: function () {
    const app = getApp();
    wx.request({
      url: 'http://43.142.142.224:8000/myapp/wx_GetFinancialRecordView/', // 替换为您的后端API地址
      data: { username: app.globalData.username },
      success: res => {
        if (res.data.status) {
          this.setData({ financialData: res.data.financial_records });
          this.drawBarChart();
        }
      },
      fail: err => {
        console.error("获取财务数据失败", err);
      }
    });
  },

  drawBarChart: function () {
    const context = wx.createCanvasContext('barCanvas');
    const data = this.data.financialData;
    const canvasWidth = 320; // 画布宽度
    const canvasHeight = 300; // 画布高度
    const yAxisMax = Math.max(...data.map(record => record.amount)); // Y轴最大值
    const columnWidth = 20; // 柱子宽度
    const columnGap = 30; // 柱子间隔

    data.forEach((record, index) => {
      const x = columnGap * (index + 1) + columnWidth * index;
      const y = canvasHeight - (record.amount / yAxisMax * canvasHeight);
      context.rect(x, y, columnWidth, canvasHeight - y);
      context.fillText(record.item_name, x, canvasHeight - 10);
    });

    context.stroke();
    context.draw();
  }
});
