import re

with open('/Users/sean/Desktop/A/database_demo.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix CSS
css_fix = """
        .table { margin-bottom: 0; font-size: 0.95rem; vertical-align: middle; white-space: nowrap; text-align: center; color: var(--text-main); }
        .table th { background-color: rgba(0,0,0,0.3) !important; color: var(--text-muted) !important; font-weight: 600; padding: 15px; border-bottom: 1px solid var(--border-color) !important; text-align: center; border-top: none; }
        .table td { padding: 15px; border-bottom: 1px solid var(--border-color) !important; color: var(--text-main) !important; background-color: transparent !important; }
        .table tbody tr { background-color: transparent !important; }
        .table tbody tr:hover { background-color: rgba(255,255,255,0.05) !important; }
"""

content = re.sub(r'\.table \{ margin-bottom: 0;.*?\.table tbody tr:hover \{ background-color: rgba\(255,255,255,0\.05\); \}', css_fix.strip(), content, flags=re.DOTALL)

# We need to insert the tables back.
tables_html = """
        <!-- 產品資料表 -->
        <div class="table-section">
            <div class="table-card">
                <div class="table-header">
                    <h4><i class="fa-solid fa-box-open text-info me-2"></i>產品資料表 (Product Table)</h4>
                    <span class="record-count">目前共有：37 筆</span>
                </div>
                <div class="table-responsive" style="max-height: 600px; overflow-y: auto;">
                    <table class="table align-middle">
                        <thead style="position: sticky; top: 0; z-index: 1;">
                            <tr><th>產品編碼</th><th>產品名稱</th><th>售價</th><th>產品描述</th><th>產品圖示</th><th>現有庫存</th><th>最後異動時間</th></tr>
                        </thead>
                        <tbody>
                            <tr><td>2026055001</td><td>水之森玄米抹茶</td><td>NT$ 65</td><td>嚴選靜岡抹茶搭配焙煎玄米</td><td><img src="image/01.jpg" class="product-img"></td><td>120</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055002</td><td>英倫伯爵紅茶</td><td>NT$ 55</td><td>佛手柑香氣與紅茶的經典結合</td><td><img src="image/02.jpg" class="product-img"></td><td>115</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055003</td><td>珍珠鮮奶</td><td>NT$ 75</td><td>Q彈手作珍珠搭配直送鮮乳</td><td><img src="image/03.jpg" class="product-img"></td><td>108</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055004</td><td>手炒黑糖鮮奶</td><td>NT$ 80</td><td>職人手工慢炒黑糖，香氣濃郁</td><td><img src="image/04.jpg" class="product-img"></td><td>95</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055005</td><td>嫩仙草凍奶</td><td>NT$ 70</td><td>滑嫩鮮草搭配濃郁奶茶</td><td><img src="image/05.jpg" class="product-img"></td><td>88</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055006</td><td>海鹽芒果綠</td><td>NT$ 65</td><td>芒果鮮甜與微鹹海鹽奶蓋</td><td><img src="image/06.jpg" class="product-img"></td><td>76</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055007</td><td>琥珀高峰烏龍</td><td>NT$ 55</td><td>炭焙香氣重，茶韻悠長</td><td><img src="image/07.jpg" class="product-img"></td><td>150</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055008</td><td>茉香綠茶拿鐵</td><td>NT$ 65</td><td>清新茉莉花香與鮮奶交織</td><td><img src="image/08.jpg" class="product-img"></td><td>102</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055009</td><td>芋頭鮮奶</td><td>NT$ 85</td><td>手作芋泥，口感綿密扎實</td><td><img src="image/09.jpg" class="product-img"></td><td>65</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055010</td><td>果漾微甜氣泡飲</td><td>NT$ 75</td><td>清爽氣泡搭配季節果漿</td><td><img src="image/10.jpg" class="product-img"></td><td>92</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055011</td><td>經典冰水果茶</td><td>NT$ 80</td><td>多種鮮切水果與茶湯結合</td><td><img src="image/11.jpg" class="product-img"></td><td>80</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055012</td><td>季節限定特調</td><td>NT$ 85</td><td>主廚當季推薦，驚喜口感</td><td><img src="image/12.jpg" class="product-img"></td><td>50</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055013</td><td>招牌綜合果茶</td><td>NT$ 90</td><td>得正招牌果茶，豐富多層次</td><td><img src="image/13.jpg" class="product-img"></td><td>70</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055027</td><td>焙烏龍鮮奶</td><td>NT$ 70</td><td>深焙烏龍與鮮奶完美比例</td><td><img src="image/27.jpg" class="product-img"></td><td>110</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055015</td><td>柚見冰茶</td><td>NT$ 65</td><td>葡萄柚果肉清爽微苦甘甜</td><td><img src="image/28.jpg" class="product-img"></td><td>85</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055031</td><td>蜜桃春烏龍</td><td>NT$ 75</td><td>甜蜜桃果香與春烏龍茶香</td><td><img src="image/31.jpg" class="product-img"></td><td>96</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055017</td><td>芝士奶蓋紅茶</td><td>NT$ 70</td><td>濃厚芝士奶蓋搭配純紅茶</td><td><img src="image/32.jpg" class="product-img"></td><td>77</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055018</td><td>桂花烏龍凍飲</td><td>NT$ 65</td><td>手工桂花凍，芬芳清爽</td><td><img src="image/33.jpg" class="product-img"></td><td>105</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055101</td><td>蜜糖波堤</td><td>NT$ 45</td><td>口感Q彈，裹上經典糖衣</td><td><img src="image/0001.jpg" class="product-img"></td><td>126</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055102</td><td>雙層巧克力波堤</td><td>NT$ 50</td><td>巧克力波堤裹黑巧克力</td><td><img src="image/0002.jpg" class="product-img"></td><td>110</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055103</td><td>草莓波堤</td><td>NT$ 50</td><td>草莓沾醬搭配Q彈波堤</td><td><img src="image/0003.jpg" class="product-img"></td><td>95</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055104</td><td>經典糖霜甜甜圈</td><td>NT$ 45</td><td>手工揉製，口感鬆軟綿密</td><td><img src="image/0004.jpg" class="product-img"></td><td>80</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055105</td><td>巧克力脆片波堤</td><td>NT$ 55</td><td>巧克力搭配酥脆脆片</td><td><img src="image/0005.jpg" class="product-img"></td><td>60</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055106</td><td>草莓夾心甜甜圈</td><td>NT$ 55</td><td>內含濃郁草莓內餡</td><td><img src="image/0006.jpg" class="product-img"></td><td>45</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055107</td><td>抹茶巧貝</td><td>NT$ 55</td><td>靜岡抹茶特調內餡</td><td><img src="image/0007.jpg" class="product-img"></td><td>85</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055201</td><td>鮮甜愛文芒果</td><td>NT$ 100</td><td>台灣特選芒果，飽滿多汁</td><td><img src="image/S1.jpg" class="product-img"></td><td>72</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055202</td><td>清香麻豆文旦</td><td>NT$ 80</td><td>嚴選老欉文旦，細緻清甜</td><td><img src="image/S2.jpg" class="product-img"></td><td>68</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055203</td><td>活力陽光香蕉</td><td>NT$ 50</td><td>產地直送，口感Ｑ彈綿密</td><td><img src="image/S3.jpg" class="product-img"></td><td>110</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055204</td><td>進口紅櫻桃</td><td>NT$ 150</td><td>空運直送，果實碩大酸甜</td><td><img src="image/S4.jpg" class="product-img"></td><td>48</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055205</td><td>清脆鮮切小黃瓜</td><td>NT$ 40</td><td>產銷履歷，口感清脆低卡</td><td><img src="image/S5.jpg" class="product-img"></td><td>62</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055206</td><td>紐西蘭奇異果</td><td>NT$ 85</td><td>富含維他命C，酸甜健康</td><td><img src="image/S6.jpg" class="product-img"></td><td>55</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055207</td><td>鮮甜多汁水蜜桃</td><td>NT$ 120</td><td>果肉細白，香氣濃郁多汁</td><td><img src="image/unnamed.jpg" class="product-img"></td><td>35</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055208</td><td>屏東金鑽鳳梨</td><td>NT$ 70</td><td>果肉纖維細緻，甜度極高</td><td><img src="image/unnamed (1).jpg" class="product-img"></td><td>40</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055209</td><td>屏東黑珍珠蓮霧</td><td>NT$ 90</td><td>色澤紅潤，清甜爽脆</td><td><img src="image/unnamed (2).jpg" class="product-img"></td><td>50</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055210</td><td>沁涼紅肉西瓜盤</td><td>NT$ 65</td><td>嚴選西瓜，果肉沙脆甜度高</td><td><img src="image/unnamed (3).jpg" class="product-img"></td><td>90</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055211</td><td>屏東無籽綠檸檬</td><td>NT$ 55</td><td>香氣強郁，適合泡茶入菜</td><td><img src="image/unnamed (4).jpg" class="product-img"></td><td>120</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055212</td><td>清脆甜水梨</td><td>NT$ 95</td><td>水潤飽滿，降火解膩首選</td><td><img src="image/unnamed (5).jpg" class="product-img"></td><td>60</td><td>2026-04-16 22:00:01</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- 金流資料 -->
        <div class="table-section">
            <div class="table-card">
                <div class="table-header">
                    <h4><i class="fa-solid fa-credit-card text-warning me-2"></i>金流資料 (Payment Table)</h4>
                </div>
                <div class="table-responsive">
                    <table class="table align-middle">
                        <thead><tr><th>金流交易編號</th><th>對應訂單編號</th><th>付款方式</th><th>付款金額</th><th>付款狀態</th></tr></thead>
                        <tbody id="db-payment-body">
                            <tr><td colspan="5" class="empty-row">尚無金流資料。</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- 物流資料 -->
        <div class="table-section">
            <div class="table-card">
                <div class="table-header">
                    <h4><i class="fa-solid fa-truck-fast text-primary me-2"></i>物流資料 (Shipping Table)</h4>
                </div>
                <div class="table-responsive">
                    <table class="table align-middle">
                        <thead><tr><th>物流追蹤單號</th><th>對應訂單編號</th><th>配送方式</th><th>收件人</th><th>配送狀態</th></tr></thead>
                        <tbody id="db-shipping-body">
                            <tr><td colspan="5" class="empty-row">尚無物流資料。</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
"""

# Find where to insert tables_html
# We can insert it after the Member Table
parts = content.split('<!-- 隱藏的產品清單，用於初始化庫存基底 -->')
if len(parts) == 2:
    content = parts[0] + tables_html + '\n        <!-- 隱藏的產品清單，用於初始化庫存基底 -->' + parts[1]

# Now, we need to update the Javascript to populate db-payment-body and db-shipping-body based on orders
js_update = """
                // 金流與物流
                const payId = `PAY-${order.timestamp.toString().substring(7)}`;
                const shipId = `SHP-${order.timestamp.toString().substring(5)}`;
                
                paymentHtml += `<tr>
                    <td>${payId}</td>
                    <td>${orderId}</td>
                    <td>線上刷卡</td>
                    <td>NT$ ${order.total}</td>
                    <td><span class="status-badge status-success">已付款</span></td>
                </tr>`;

                const shipBadge = isCompleted 
                    ? '<span class="status-badge status-success">已配達</span>' 
                    : '<span class="status-badge status-pending">準備中</span>';
                    
                shippingHtml += `<tr>
                    <td>${shipId}</td>
                    <td>${orderId}</td>
                    <td>得正低溫配送</td>
                    <td>${order.customer}</td>
                    <td>${shipBadge}</td>
                </tr>`;
"""

# Let's insert the JS logic
# We need to find `let orderHtml = '';`
content = content.replace("let orderHtml = '';", "let orderHtml = '';\n            let paymentHtml = '';\n            let shippingHtml = '';")

# Replace `orderHtml += `<tr>` with the JS update
content = content.replace("orderHtml += `<tr>", js_update + "\n                orderHtml += `<tr>")

content = content.replace("document.getElementById('db-orders-body').innerHTML = orderHtml;", "document.getElementById('db-orders-body').innerHTML = orderHtml;\n                document.getElementById('db-payment-body').innerHTML = paymentHtml;\n                document.getElementById('db-shipping-body').innerHTML = shippingHtml;")

content = content.replace("document.getElementById('db-orders-body').innerHTML = '<tr><td colspan=\"6\" class=\"empty-row\">尚無訂單資料</td></tr>';", "document.getElementById('db-orders-body').innerHTML = '<tr><td colspan=\"6\" class=\"empty-row\">尚無訂單資料</td></tr>';\n                document.getElementById('db-payment-body').innerHTML = '<tr><td colspan=\"5\" class=\"empty-row\">尚無金流資料。</td></tr>';\n                document.getElementById('db-shipping-body').innerHTML = '<tr><td colspan=\"5\" class=\"empty-row\">尚無物流資料。</td></tr>';")

with open('/Users/sean/Desktop/A/database_demo.html', 'w', encoding='utf-8') as f:
    f.write(content)
