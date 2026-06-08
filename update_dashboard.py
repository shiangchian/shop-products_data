import re

with open('/Users/sean/Desktop/A/database_demo.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Localize Login Screen
content = content.replace("SYSTEM LOGIN", "系統登入")
content = content.replace("AUTHENTICATE", "確認進入")

# 2. Add New KPIs
new_kpis = """
            <div class="kpi-card" style="border-left: 4px solid var(--accent-success);">
                <div class="kpi-icon" style="background: rgba(16, 185, 129, 0.1); color: var(--accent-success);"><i class="fa-solid fa-users"></i></div>
                <div class="kpi-content">
                    <h3>總會員數</h3>
                    <p class="kpi-value"><span id="kpi-members-count">0</span> 人</p>
                    <p class="kpi-desc" style="color:var(--text-muted);"><i class="fa-solid fa-user-check"></i> 註冊會員總計</p>
                </div>
            </div>
            <div class="kpi-card" style="border-left: 4px solid var(--accent-primary);">
                <div class="kpi-icon" style="background: rgba(56, 189, 248, 0.1); color: var(--accent-primary);"><i class="fa-solid fa-coins"></i></div>
                <div class="kpi-content">
                    <h3>平均客單價</h3>
                    <p class="kpi-value">NT$ <span id="kpi-avg-order">0</span></p>
                    <p class="kpi-desc" style="color:var(--text-muted);"><i class="fa-solid fa-calculator"></i> 每筆訂單均價</p>
                </div>
            </div>
            <div class="kpi-card" style="border-left: 4px solid var(--accent-warning);">
                <div class="kpi-icon" style="background: rgba(245, 158, 11, 0.1); color: var(--accent-warning);"><i class="fa-solid fa-trophy"></i></div>
                <div class="kpi-content">
                    <h3>熱銷排行冠軍</h3>
                    <p class="kpi-value" style="font-size: 1.5rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 150px;" id="kpi-top-item">-</p>
                    <p class="kpi-desc" style="color:var(--text-muted);"><i class="fa-solid fa-fire"></i> 歷史銷量最高</p>
                </div>
            </div>
"""

# Insert new KPIs after the "alerts" KPI card
alerts_kpi_end = """            <div class="kpi-card alerts" onclick="scrollToStock()">
                <div class="kpi-icon"><i class="fa-solid fa-triangle-exclamation"></i></div>
                <div class="kpi-content">
                    <h3>需進貨品項</h3>
                    <p class="kpi-value"><span id="kpi-restock-count">0</span> 項</p>
                    <p class="kpi-desc"><i class="fa-solid fa-eye"></i> 點擊查看缺貨清單</p>
                </div>
            </div>"""

content = content.replace(alerts_kpi_end, alerts_kpi_end + "\n" + new_kpis)

# 3. Add Doughnut Chart HTML
new_chart_html = """
            <!-- 類別銷售圓餅圖 -->
            <div class="chart-card">
                <div class="card-header-title">
                    <span><i class="fa-solid fa-chart-pie text-success me-2"></i> 各類別銷售佔比</span>
                </div>
                <div style="height: 350px; width: 100%; position: relative;">
                    <canvas id="categoryChart"></canvas>
                </div>
            </div>
"""

# The grid needs to handle 3 items instead of 2. Let's make it grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)) 
# or just change content-grid CSS
css_grid_replace = ".content-grid { display: grid; grid-template-columns: 2fr 1fr; gap: 25px; margin-bottom: 40px; }"
css_grid_new = ".content-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 25px; margin-bottom: 40px; }"
content = content.replace(css_grid_replace, css_grid_new)

# Insert new_chart_html after the first chart
content = content.replace('</canvas>\n                </div>\n            </div>', '</canvas>\n                </div>\n            </div>\n' + new_chart_html)


# 4. JS Logic Updates
# Find the end of `const dailyRevenue = {};` logic
js_insert = """
            // 新增變數
            let totalMembers = 5; // 寫死的會員資料表數量
            const itemSales = {}; // 追蹤各品項銷量
            const categorySales = { '茶飲類': 0, '甜甜圈': 0, '鮮果類': 0 };
"""

content = content.replace("            // 初始化商品庫存追蹤", js_insert + "\n            // 初始化商品庫存追蹤")

# In the loop parsing order items:
item_loop = """
                        if(match) {
                            const pName = match[1].trim();
                            const pQty = parseInt(match[2]);
                            if(inventory[pName] !== undefined) {
                                inventory[pName] -= pQty;
                            }
"""
item_loop_new = item_loop + """
                            // 記錄總銷量
                            if(!itemSales[pName]) itemSales[pName] = 0;
                            itemSales[pName] += pQty;

                            // 記錄類別銷量
                            if(pName.includes('抹茶') || pName.includes('紅茶') || pName.includes('鮮奶') || pName.includes('烏龍') || pName.includes('綠') || pName.includes('冰茶') || pName.includes('氣泡飲') || pName.includes('果茶')) {
                                categorySales['茶飲類'] += pQty;
                            } else if(pName.includes('波堤') || pName.includes('甜甜圈') || pName.includes('巧貝')) {
                                categorySales['甜甜圈'] += pQty;
                            } else {
                                categorySales['鮮果類'] += pQty;
                            }
"""
content = content.replace(item_loop, item_loop_new)

# Update KPI DOM logic
kpi_dom_insert = """
            // 計算新 KPI
            const avgOrderValue = orders.length > 0 ? Math.round(totalRevenue / orders.length) : 0;
            document.getElementById('kpi-avg-order').innerText = avgOrderValue.toLocaleString();
            document.getElementById('kpi-members-count').innerText = totalMembers;

            // 找熱銷冠軍
            let topItem = '-';
            let maxSales = 0;
            for(let item in itemSales) {
                if(itemSales[item] > maxSales) {
                    maxSales = itemSales[item];
                    topItem = item;
                }
            }
            document.getElementById('kpi-top-item').innerText = topItem;
            
            // 畫甜甜圈圖
            renderCategoryChart(categorySales);
"""

content = content.replace("            document.getElementById('kpi-orders-count').innerText = orders.length;", "            document.getElementById('kpi-orders-count').innerText = orders.length;\n" + kpi_dom_insert)


# Add Doughnut Chart Render Function
doughnut_func = """
        let categoryChartInstance = null;
        function renderCategoryChart(data) {
            const ctx = document.getElementById('categoryChart').getContext('2d');
            if(categoryChartInstance) categoryChartInstance.destroy();
            
            categoryChartInstance = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: Object.keys(data),
                    datasets: [{
                        data: Object.values(data),
                        backgroundColor: ['rgba(56, 189, 248, 0.8)', 'rgba(245, 158, 11, 0.8)', 'rgba(16, 185, 129, 0.8)'],
                        borderColor: '#0f172a',
                        borderWidth: 2,
                        hoverOffset: 10
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { position: 'bottom', labels: { color: '#94a3b8', font: { family: 'Noto Sans TC' } } },
                        tooltip: { backgroundColor: 'rgba(15, 23, 42, 0.9)', titleFont: { family: 'Noto Sans TC' }, bodyFont: { family: 'Outfit', size: 14 } }
                    },
                    cutout: '70%'
                }
            });
        }
"""
content = content.replace("        // Chart.js 渲染函式", doughnut_func + "\n        // Chart.js 渲染函式")


with open('/Users/sean/Desktop/A/database_demo.html', 'w', encoding='utf-8') as f:
    f.write(content)
