<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Peshku Artel - Maishiy Texnika</title>
    
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">

    <script src="https://telegram.org/js/telegram-web-app.js"></script>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }
        body {
            background-color: #121212;
            color: #ffffff;
            padding-bottom: 75px;
        }
        .banner {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, #2b2b2b, #1f1f1f);
        }
        .banner-content {
            background: linear-gradient(90deg, #ff416c, #ff4b2b);
            border-radius: 12px;
            padding: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: white;
        }
        .banner-text h2 { font-size: 18px; margin-bottom: 4px; }
        .banner-text p { font-size: 13px; opacity: 0.9; }

        .categories {
            display: flex;
            gap: 10px;
            overflow-x: auto;
            padding: 15px;
            scrollbar-width: none;
        }
        .categories::-webkit-scrollbar { display: none; }
        .category-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            background: #1e1e1e;
            padding: 10px;
            border-radius: 12px;
            min-width: 95px;
            cursor: pointer;
            border: 1px solid #333;
            transition: 0.2s;
            -webkit-tap-highlight-color: transparent;
        }
        .category-item span {
            font-size: 11px;
            color: #ccc;
            text-align: center;
            pointer-events: none;
            margin-top: 4px;
        }
        .category-item.active { border-color: #ff4b2b; background: #2a1f1d; }
        .category-item.active span { color: #ff4b2b; font-weight: bold; }

        .section-title { padding: 10px 15px; font-size: 18px; font-weight: bold; }

        .products-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
            padding: 10px 15px;
        }
        .product-card {
            background: #1e1e1e;
            border-radius: 16px;
            padding: 12px;
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .product-image {
            width: 100%;
            height: 120px;
            object-fit: contain;
            margin-bottom: 10px;
            background: #252525;
            border-radius: 10px;
            padding: 5px;
        }
        .price { font-size: 14px; font-weight: bold; color: #fff; margin-bottom: 4px; }
        .product-name { font-size: 12px; color: #aaa; margin-bottom: 15px; line-height: 1.3; }
        .add-btn {
            position: absolute;
            bottom: 12px;
            right: 12px;
            background: #ff4b2b;
            color: white;
            border: none;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            font-size: 18px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: 0.2s;
        }
        .add-btn:active { transform: scale(0.9); }

        .cart-item {
            background: #1e1e1e;
            padding: 12px;
            border-radius: 12px;
            margin: 0 15px 10px 15px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .cart-item-info { display: flex; align-items: center; gap: 10px; }
        .cart-item-img {
            width: 50px;
            height: 50px;
            object-fit: contain;
            background: #252525;
            border-radius: 8px;
        }
        .remove-btn {
            background: #333;
            color: #ff4b2b;
            border: none;
            padding: 6px 10px;
            border-radius: 6px;
            cursor: pointer;
        }

        .checkout-box {
            padding: 15px;
            margin: 15px;
            background: #1e1e1e;
            border-radius: 12px;
        }
        .primary-btn {
            width: 100%;
            padding: 12px;
            background: #ff4b2b;
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            font-size: 15px;
            cursor: pointer;
            margin-top: 10px;
        }

        .form-group { margin-bottom: 12px; }
        .form-group label {
            display: block;
            font-size: 13px;
            color: #ccc;
            margin-bottom: 5px;
        }
        .form-group input, .form-group textarea {
            width: 100%;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #333;
            background: #2a2a2a;
            color: #fff;
            font-size: 14px;
        }

        .page-content { display: none; }
        .page-content.active { display: block; }
        .empty-state { text-align: center; padding: 40px 20px; color: #777; }

        .bottom-nav {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background: #181818;
            border-top: 1px solid #282828;
            display: flex;
            justify-content: space-around;
            padding: 8px 0;
            z-index: 1000;
        }
        .nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            color: #777;
            text-decoration: none;
            font-size: 11px;
            cursor: pointer;
            background: none;
            border: none;
            -webkit-tap-highlight-color: transparent;
        }
        .nav-item svg { width: 22px; height: 22px; margin-bottom: 3px; fill: currentColor; }
        .nav-item.active { color: #ff4b2b; }

        .gps-status {
            font-size: 12px;
            color: #00ff88;
            margin-top: 5px;
            display: none;
        }
    </style>
</head>
<body>

    <!-- BOSH SAHIFA -->
    <div id="homePage" class="page-content active">
        <div class="banner">
            <div class="banner-content">
                <div class="banner-text">
                    <h2>Artel Texnikalari</h2>
                    <p>Katta chegirmalar va aksiya!</p>
                </div>
                <span style="font-size: 28px;">🔥</span>
            </div>
        </div>

        <div class="categories">
            <div class="category-item active" onclick="selectCategory('Aksiyadagi Mahsulotlar', this)">
                <span style="font-size: 20px;">🔥</span>
                <span>Aksiyalar</span>
            </div>
            <div class="category-item" onclick="selectCategory('Muzlatgich', this)">
                <span style="font-size: 20px;">❄️</span>
                <span>Muzlatgich</span>
            </div>
            <div class="category-item" onclick="selectCategory('Kir yuvish', this)">
                <span style="font-size: 20px;">🌀</span>
                <span>Kir yuvish</span>
            </div>
            <div class="category-item" onclick="selectCategory('Televizor', this)">
                <span style="font-size: 20px;">📺</span>
                <span>Televizor</span>
            </div>
            <div class="category-item" onclick="selectCategory('Pechlar', this)">
                <span style="font-size: 20px;">🍳</span>
                <span>Pechlar</span>
            </div>
        </div>

        <div class="section-title" id="sectionTitle">Aksiyadagi Mahsulotlar</div>
        <div class="products-grid" id="productsGrid"></div>
    </div>

    <!-- SAVAT SAHIFA -->
    <div id="cartPage" class="page-content">
        <div class="section-title">Savat</div>
        <div id="cartList"></div>
        <div class="empty-state" id="cartEmpty">Savatangiz hozircha bo'sh 🛒</div>
        
        <div class="checkout-box" id="checkoutBox" style="display: none;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 15px;">
                <span>Jami mahsulotlar:</span>
                <b id="cartTotalItems">0 ta</b>
            </div>

            <div class="form-group">
                <label style="color: #ff4b2b; font-weight: bold;">1. Ismingiz:</label>
                <input type="text" id="custFirstName" placeholder="Masalan: Muhammadjon">
            </div>

            <div class="form-group">
                <label style="color: #ff4b2b; font-weight: bold;">2. Familiyangiz:</label>
                <input type="text" id="custLastName" placeholder="Masalan: Muhammadov">
            </div>

            <div class="form-group">
                <label style="color: #ff4b2b; font-weight: bold;">3. Telefon raqamingiz:</label>
                <input type="tel" id="custPhone" placeholder="+998 90 123 45 67">
            </div>

            <div class="form-group" style="margin-top: 15px;">
                <label style="color: #ff4b2b; font-weight: bold;">4. Turgan joyingizni lokatsiyadan uring:</label>
                <button type="button" class="primary-btn" style="background: #252525; border: 1px solid #ff4b2b;" id="getGpsBtn" onclick="getLocation()">
                    📍 Turgan joyimni aniqlash
                </button>
                <div id="gpsStatus" class="gps-status">✓ GPS Lokatsiya muvaffaqiyatli olindi!</div>
            </div>

            <div class="form-group" style="margin-top: 15px;">
                <label style="color: #ff4b2b; font-weight: bold;">5. Qayergaligini yozing (Mo'ljal / Uy raqami):</label>
                <textarea id="locationDetail" rows="2" placeholder="Masalan: Peshku markazi, Hokimiyat ro'parasida, 12-uy"></textarea>
            </div>

            <button class="primary-btn" id="orderBtn" onclick="placeOrder()">Buyurtma berish</button>
        </div>
    </div>

    <!-- BUYURTMALAR SAHIFA -->
    <div id="ordersPage" class="page-content">
        <div class="section-title">Buyurtmalarim</div>
        <div id="ordersList"></div>
        <div class="empty-state" id="ordersEmpty">Hozircha faol buyurtmalar yo'q 📦</div>
    </div>

    <!-- Bottom Navigation -->
    <div class="bottom-nav">
        <button class="nav-item active" onclick="switchPage('home', this)">
            <svg viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>
            Bosh sahifa
        </button>
        <button class="nav-item" onclick="switchPage('cart', this)">
            <svg viewBox="0 0 24 24"><path d="M7 18c-1.1 0-1.99.9-1.99 2S5.9 22 7 22s2-.9 2-2-.9-2-2-2zM1 2v2h2l3.6 7.59-1.35 2.45c-.16.28-.25.61-.25.96 0 1.1.9 2 2 2h12v-2H7.42c-.14 0-.25-.11-.25-.25l.03-.12.9-1.63h7.45c.75 0 1.41-.41 1.75-1.03l3.58-6.49c.08-.14.12-.31.12-.48 0-.55-.45-1-1-1H5.21l-.94-2H1zm16 16c-1.1 0-1.99.9-1.99 2s.89 2 1.99 2 2-.9 2-2-.9-2-2-2z"/></svg>
            Savat
        </button>
        <button class="nav-item" onclick="switchPage('orders', this)">
            <svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>
            Buyurtmalar
        </button>
    </div>

    <script>
        let tg = window.Telegram.WebApp;
        tg.expand();

        const botToken = '8914337317:AAGi--DubDzA7LwArdc6RCsgMN_CU_d2wRs';
        const adminChatId = '6584293343';

        let currentGpsUrl = null;

        const products = [
            { id: 1, name: "Gaz plitas Vesta AK Lite Sovg'asi bilan birga", price: "1 760 000 UZS", category: "Aksiyadagi Mahsulotlar", image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5EGl6gEVUaxbE_FQsjLVnWQ_r5WlrHY86LABhsJ2xog&s=10" },
            { id: 2, name: "Gaz plitas Vesta AK-00 Sovg'asi bilan birga", price: "1 850 000 UZS", category: "Aksiyadagi Mahsulotlar", image: "https://assets.asaxiy.uz/product/items/desktop/96a3be3cf272e017046d1b2674a52bd32024012210022833037PDAQNmNFuA.jpg.webp" },
            { id: 3, name: "Gaz plitas Vesta AK-10 Sovg'asi bilan birga", price: "1 960 000 UZS", category: "Aksiyadagi Mahsulotlar", image: "https://avatars.mds.yandex.net/get-mpic/18061612/pic6dcec2bbdcc9cfb59d12f9beb0f4ffe3/orig" },
            { id: 4, name: "Gaz plitas Vesta AG-01 Sovg'asi bilan birga", price: "1 990 000 UZS", category: "Aksiyadagi Mahsulotlar", image: "https://assets.asaxiy.uz/product/items/desktop/e45ee7ce7e88149af8dd32b27f9512ce2025092614583233355tk1AcwMSOY.jpg.webp" },
            { id: 5, name: "Gaz plitas Vesta MK-10 Sovg'asi bilan birga", price: "2 050 000 UZS", category: "Aksiyadagi Mahsulotlar", image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnHpTSGlok8m9_qyjcZMtUjEASQd5iaasG0HT0Lxg-A4cssyEj5Ypx8fK1&s=10" },
            { id: 6, name: "Gaz plitas Vesta MG-01 Sovg'asi bilan birga", price: "2 050 000 UZS", category: "Aksiyadagi Mahsulotlar", image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVWqxKuXK2ZAVWzru5wxlq_QGje78fX8e7k5eBTWiNemZwsLP28td7WBk&s=10" },
            { id: 7, name: "Gaz plitas Vesta MK-02 Sovg'asi bilan birga", price: "2 350 000 UZS", category: "Aksiyadagi Mahsulotlar", image: "https://assets.asaxiy.uz/product/items/desktop/96a3be3cf272e017046d1b2674a52bd32024012210022833037PDAQNmNFuA.jpg.webp" },
            { id: 8, name: "Kir moshina Vesta 6,5 kg", price: "960 000 UZS", category: "Aksiyadagi Mahsulotlar", image: "https://cdn.asaxiy.uz/asaxiy-content/product/items/desktop/96a3be3cf272e017046d1b2674a52bd32025112512074280427rMuFq2tMkO.jpg.webp" },
            { id: 9, name: "Kir moshina Vesta 7,5 kg", price: "999 000 UZS", category: "Aksiyadagi Mahsulotlar", image: "https://images.uzum.uz/da2k05e1464l8lvn4dk0/t_product_540_high.jpg" },
            { id: 10, name: "Kir moshina Artel 8 kg", price: "1 260 000 UZS", category: "Aksiyadagi Mahsulotlar", image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQr4Lth65_gzvEYqR5ojm9rugeSv2F2Fr92m3ZCe2JYwxR_u4JwF0sxd2c9&s=10" },
            { id: 11, name: "Kir moshina Vesta 8,5 kg", price: "1 320 000 UZS", category: "Aksiyadagi Mahsulotlar", image: "https://s3.fortifai.uz/shop/moderation/partner-1453/1782301968-clean-image-1782301967938-0.jpg" },
            { id: 12, name: "Kir moshina Vesta 10 kg", price: "1 520 000 UZS", category: "Aksiyadagi Mahsulotlar", image: "https://images.uzum.uz/da2k05e1464l8lvn4dk0/t_product_540_high.jpg" },
            { id: 13, name: "Mytech 32Tv", price: "999 000 UZS", category: "Aksiyadagi Mahsulotlar", image: "https://s3.fortifai.uz/shop/moderation/partner-1061/1759147322-1753709403-cni2u04u2hhlb05gfam0.jpg" },
            { id: 14, name: "Domassi smart 43 Tv", price: "2 000 000 UZS", category: "Aksiyadagi Mahsulotlar", image: "https://images.uzum.uz/d84ta2a1146tv0710e50/t_product_540_high.jpg" },
            { id: 15, name: "Domassi smart 32 TV", price: "1 200 000 UZS", category: "Aksiyadagi Mahsulotlar", image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRp2Hn9_ipNmmpFE8skibZ-hF4rmmixb94vs-dnMfijIQ&s" }
        ];

        let cart = [];
        let orders = [];

        function renderProducts(category = "Aksiyadagi Mahsulotlar") {
            const grid = document.getElementById('productsGrid');
            grid.innerHTML = "";
            let filtered = products.filter(p => p.category === category);

            filtered.forEach(p => {
                const card = document.createElement('div');
                card.className = 'product-card';
                card.innerHTML = `
                    <img src="${p.image}" alt="${p.name}" class="product-image">
                    <div>
                        <div class="price">${p.price}</div>
                        <div class="product-name">${p.name}</div>
                    </div>
                    <button class="add-btn" onclick="addToCart(${p.id})">+</button>
                `;
                grid.appendChild(card);
            });
        }

        function selectCategory(categoryName, element) {
            document.querySelectorAll('.category-item').forEach(el => el.classList.remove('active'));
            element.classList.add('active');
            document.getElementById('sectionTitle').innerText = categoryName;
            renderProducts(categoryName);
        }

        function switchPage(pageName, btnElement) {
            document.querySelectorAll('.page-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));

            btnElement.classList.add('active');

            if (pageName === 'home') document.getElementById('homePage').classList.add('active');
            else if (pageName === 'cart') { document.getElementById('cartPage').classList.add('active'); renderCart(); }
            else if (pageName === 'orders') { document.getElementById('ordersPage').classList.add('active'); renderOrders(); }
        }

        function addToCart(productId) {
            const product = products.find(p => p.id === productId);
            cart.push(product);
            alert(`"${product.name}" savatga qo'shildi! 🛒`);
        }

        function removeFromCart(index) {
            cart.splice(index, 1);
            renderCart();
        }

        function renderCart() {
            const cartList = document.getElementById('cartList');
            const cartEmpty = document.getElementById('cartEmpty');
            const checkoutBox = document.getElementById('checkoutBox');

            cartList.innerHTML = "";

            if (cart.length === 0) {
                cartEmpty.style.display = 'block';
                checkoutBox.style.display = 'none';
                return;
            }

            cartEmpty.style.display = 'none';
            checkoutBox.style.display = 'block';
            document.getElementById('cartTotalItems').innerText = `${cart.length} ta`;

            cart.forEach((item, idx) => {
                const cItem = document.createElement('div');
                cItem.className = 'cart-item';
                cItem.innerHTML = `
                    <div class="cart-item-info">
                        <img src="${item.image}" class="cart-item-img">
                        <div>
                            <div style="font-size: 13px; font-weight: bold;">${item.name}</div>
                            <div style="font-size: 12px; color: #ff4b2b;">${item.price}</div>
                        </div>
                    </div>
                    <button class="remove-btn" onclick="removeFromCart(${idx})">O'chirish</button>
                `;
                cartList.appendChild(cItem);
            });
        }

        function getLocation() {
            if (!navigator.geolocation) {
                alert("Qurilmangizda GPS funksiyasi qo'llab-quvvatlanmaydi!");
                return;
            }

            const getGpsBtn = document.getElementById('getGpsBtn');
            getGpsBtn.innerText = "⏳ Aniqlanmoqda...";
            getGpsBtn.disabled = true;

            navigator.geolocation.getCurrentPosition(
                (position) => {
                    const lat = position.coords.latitude;
                    const lon = position.coords.longitude;
                    currentGpsUrl = `https://www.google.com/maps?q=${lat},${lon}`;

                    getGpsBtn.innerText = "✓ Lokatsiya olindi";
                    getGpsBtn.disabled = false;
                    document.getElementById('gpsStatus').style.display = 'block';
                },
                (error) => {
                    getGpsBtn.innerText = "📍 Turgan joyimni aniqlash";
                    getGpsBtn.disabled = false;
                    alert("Lokatsiyangizni aniqlashga ruxsat berilmadi! GPS ruxsatini yoqing.");
                },
                { enableHighAccuracy: true }
            );
        }

        function placeOrder() {
            const firstName = document.getElementById('custFirstName').value.trim();
            const lastName = document.getElementById('custLastName').value.trim();
            const phone = document.getElementById('custPhone').value.trim();

            if (!firstName) {
                alert("Iltimos, ismingizni kiriting!");
                return;
            }
            if (!lastName) {
                alert("Iltimos, familiyangizni kiriting!");
                return;
            }
            if (!phone) {
                alert("Iltimos, telefon raqamingizni kiriting!");
                return;
            }

            if (!currentGpsUrl) {
                alert("Iltimos, 'Turgan joyimni aniqlash' tugmasini bosib, GPS lokatsiyangizni urib ko'rsating!");
                return;
            }

            const detail = document.getElementById('locationDetail').value.trim();
            if (!detail) {
                alert("Iltimos, qayergaligini (mo'ljal/uy raqamini) yozing!");
                return;
            }

            let itemsText = cart.map(i => `- ${i.name} (${i.price})`).join('\n');

            let orderMessage = `🚨 YANGI BUYURTMA TUSHDI!\n\n` +
                               `👤 Ism: ${firstName}\n` +
                               `👤 Familiya: ${lastName}\n` +
                               `📞 Tel: ${phone}\n\n` +
                               `🗺 GPS Lokatsiyasi:\n${currentGpsUrl}\n\n` +
                               `📍 Qayergaligi (Mo'ljal):\n${detail}\n\n` +
                               `🛒 Mahsulotlar:\n${itemsText}`;

            const btn = document.getElementById('orderBtn');
            btn.innerText = "⏳ Yuborilmoqda...";
            btn.disabled = true;

            fetch(`https://api.telegram.org/bot${botToken}/sendMessage`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ chat_id: adminChatId, text: orderMessage })
            })
            .then(res => res.json())
            .then(data => {
                btn.innerText = "Buyurtma berish";
                btn.disabled = false;

                if (data.ok) {
                    alert("Buyurtmangiz muvaffaqiyatli qabul qilindi! 🎉");
                    
                    orders.push({
                        id: Math.floor(1000 + Math.random() * 9000),
                        items: [...cart],
                        date: new Date().toLocaleDateString('uz-UZ'),
                        address: detail,
                        customer: `${firstName} ${lastName} (${phone})`,
                        status: "Qabul qilindi 🟡"
                    });

                    cart = [];
                    currentGpsUrl = null;
                    document.getElementById('custFirstName').value = "";
                    document.getElementById('custLastName').value = "";
                    document.getElementById('custPhone').value = "";
                    document.getElementById('locationDetail').value = "";
                    document.getElementById('gpsStatus').style.display = 'none';
                    document.getElementById('getGpsBtn').innerText = "📍 Turgan joyimni aniqlash";

                    switchPage('orders', document.querySelectorAll('.nav-item')[2]);
                } else {
                    alert("Xatolik: Botga yuborib bo'lmadi (" + data.description + ")");
                }
            })
            .catch(err => {
                btn.innerText = "Buyurtma berish";
                btn.disabled = false;
                alert("Tarmoq xatosi yuz berdi!");
            });
        }

        function renderOrders() {
            const ordersList = document.getElementById('ordersList');
            const ordersEmpty = document.getElementById('ordersEmpty');
            ordersList.innerHTML = "";

            if (orders.length === 0) {
                ordersEmpty.style.display = 'block';
                return;
            }
            ordersEmpty.style.display = 'none';

            orders.forEach(o => {
                const oCard = document.createElement('div');
                oCard.className = 'checkout-box';
                let itemsHtml = o.items.map(i => `<li style="font-size: 12px; color: #ccc;">${i.name} (${i.price})</li>`).join('');
                
                oCard.innerHTML = `
                    <div style="display: flex; justify-content: space-between; font-size: 14px; font-weight: bold; margin-bottom: 8px;">
                        <span>Buyurtma #${o.id}</span>
                        <span style="color: #ff4b2b;">${o.status}</span>
                    </div>
                    <div style="font-size: 12px; color: #aaa; margin-bottom: 4px;">👤 Xaridor: ${o.customer}</div>
                    <div style="font-size: 12px; color: #aaa; margin-bottom: 4px;">Sana: ${o.date}</div>
                    <div style="font-size: 12px; color: #aaa; margin-bottom: 8px;">📍 Mo'ljal: ${o.address}</div>
                    <ul style="padding-left: 15px;">${itemsHtml}</ul>
                `;
                ordersList.appendChild(oCard);
            });
        }

        renderProducts("Aksiyadagi Mahsulotlar");
    </script>
</body>
</html>
