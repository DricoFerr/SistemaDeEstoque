use estoque;
db.dropDatabase(); // Garante que começa do zero

// --- FORNECEDORES ---
db.Fornecedores.insertMany([
    { "fornecedor_id": 1, "nome": "Ambev", "telefone": "(27) 98171-1808", "email": "Ambev@gmail.com", "endereco": "Moacir Avidos, 120" },
    { "fornecedor_id": 2, "nome": "Heineken", "telefone": "(27) 67821-1236", "email": "Heineken@gmail.com", "endereco": "Joaquim Lirio, 152" },
    { "fornecedor_id": 3, "nome": "Coca-cola", "telefone": "(27) 97385-5138", "email": "Cocacola@gmail.com", "endereco": "Vila Rubim, 45" },
    { "fornecedor_id": 4, "nome": "Campari", "telefone": "(27) 93621-8153", "email": "Campari@gmail.com", "endereco": "Praia da Costa, 102" },
    { "fornecedor_id": 5, "nome": "Jack-Daniels", "telefone": "(27) 73782-3124", "email": "JackDaniels@gmail.com", "endereco": "Castanheiras, 55" },
    { "fornecedor_id": 6, "nome": "Vinicola Salton", "telefone": "(27) 82641-9172", "email": "SaltonVinhos@gmail.com", "endereco": "Reta da penha, 33" },
    { "fornecedor_id": 7, "nome": "RedBull", "telefone": "(27) 89154-0192", "email": "Redbull@gmail.com", "endereco": "Rua das flores, 3" },
    { "fornecedor_id": 8, "nome": "Vinicola Miolo", "telefone": "(27) 35613-7712", "email": "MiolosVinhos@gmail.com", "endereco": "Ozorio Brito, 284" },
    { "fornecedor_id": 9, "nome": "Fanta", "telefone": "(27) 12463-8821", "email": "Fanta@gmail.com", "endereco": "Santo antonio, 320" },
    { "fornecedor_id": 10, "nome": "Del Valle", "telefone": "(27) 99153-2190", "email": "DelValle@gmail.com", "endereco": "Barro vermelho, 201" },
    { "fornecedor_id": 11, "nome": "Stock", "telefone": "(27) 26841-2252", "email": "Stock@gmail.com", "endereco": "Avenida Vitoria, 156" },
    { "fornecedor_id": 12, "nome": "Catucai", "telefone": "(27) 84926-8413", "email": "Catucai@gmail.com", "endereco": "Savassi, 62" }
]);

// --- PRODUTOS ---
db.Produtos.insertMany([
    { "produto_id": 1, "nome": "Corona", "descricao": "Long neck corona", "preco": 6.50, "quantidade_estoque": 120, "estoque_minimo": 10, "fornecedor_id": 1 },
    { "produto_id": 2, "nome": "Skol", "descricao": "Lata de skol", "preco": 4.20, "quantidade_estoque": 76, "estoque_minimo": 10, "fornecedor_id": 1 },
    { "produto_id": 3, "nome": "Heineken 1L", "descricao": "Garrafa Heineken 1L", "preco": 14.00, "quantidade_estoque": 62, "estoque_minimo": 10, "fornecedor_id": 2 },
    { "produto_id": 4, "nome": "Heineken Long neck", "descricao": "Garrada Heineken 320ml", "preco": 6.00, "quantidade_estoque": 231, "estoque_minimo": 10, "fornecedor_id": 2 },
    { "produto_id": 5, "nome": "Coca-cola 1L", "descricao": "Garrafa Coca-cola 1L", "preco": 9.00, "quantidade_estoque": 61, "estoque_minimo": 10, "fornecedor_id": 3 },
    { "produto_id": 6, "nome": "Coca-cola 2L", "descricao": "Garrafa Coca-cola 2L", "preco": 13.00, "quantidade_estoque": 48, "estoque_minimo": 10, "fornecedor_id": 3 },
    { "produto_id": 7, "nome": "Campari", "descricao": "Garrafa de campari", "preco": 52.90, "quantidade_estoque": 60, "estoque_minimo": 10, "fornecedor_id": 4 },
    { "produto_id": 8, "nome": "Aperol", "descricao": "Garrafa de aperol", "preco": 59.90, "quantidade_estoque": 25, "estoque_minimo": 10, "fornecedor_id": 4 },
    { "produto_id": 9, "nome": "Jack-Daniels original", "descricao": "Garrafa sabor original", "preco": 119.90, "quantidade_estoque": 55, "estoque_minimo": 10, "fornecedor_id": 5 },
    { "produto_id": 10, "nome": "Jack-Daniels apple", "descricao": "Garrafa sabor maca", "preco": 119.90, "quantidade_estoque": 77, "estoque_minimo": 10, "fornecedor_id": 5 },
    { "produto_id": 11, "nome": "Vinho San Martin", "descricao": "Vinho chileno", "preco": 89.90, "quantidade_estoque": 83, "estoque_minimo": 10, "fornecedor_id": 6 },
    { "produto_id": 12, "nome": "Vinho Merlot", "descricao": "Vinho argentino", "preco": 59.90, "quantidade_estoque": 55, "estoque_minimo": 10, "fornecedor_id": 6 },
    { "produto_id": 13, "nome": "RedBull Original", "descricao": "Lata RedBull original", "preco": 8.90, "quantidade_estoque": 35, "estoque_minimo": 10, "fornecedor_id": 7 },
    { "produto_id": 14, "nome": "RedBull Melancia", "descricao": "Lata RedBull melancia", "preco": 8.90, "quantidade_estoque": 43, "estoque_minimo": 10, "fornecedor_id": 7 },
    { "produto_id": 15, "nome": "Vinho Origini", "descricao": "Vinho frances", "preco": 49.90, "quantidade_estoque": 52, "estoque_minimo": 10, "fornecedor_id": 8 },
    { "produto_id": 16, "nome": "Vinho Casa Blanca", "descricao": "Vinho espanhol", "preco": 40.00, "quantidade_estoque": 41, "estoque_minimo": 10, "fornecedor_id": 8 },
    { "produto_id": 17, "nome": "Fanta Uva", "descricao": "Lata fanta uva", "preco": 5.50, "quantidade_estoque": 112, "estoque_minimo": 10, "fornecedor_id": 9 },
    { "produto_id": 18, "nome": "Fanta Laranja", "descricao": "Lata fanta laranja", "preco": 5.50, "quantidade_estoque": 98, "estoque_minimo": 10, "fornecedor_id": 9 },
    { "produto_id": 19, "nome": "Suco de morango", "descricao": "Garrafa suco de laranja 1L", "preco": 9.50, "quantidade_estoque": 83, "estoque_minimo": 10, "fornecedor_id": 10 },
    { "produto_id": 20, "nome": "Suco de limao", "descricao": "Garrafa suco de limao 1L", "preco": 9.50, "quantidade_estoque": 68, "estoque_minimo": 10, "fornecedor_id": 10 },
    { "produto_id": 21, "nome": "Gin dry cat", "descricao": "Garrafa gin dry cat", "preco": 119.90, "quantidade_estoque": 45, "estoque_minimo": 10, "fornecedor_id": 11 },
    { "produto_id": 22, "nome": "Gin tropical", "descricao": "Garrafa gin tropical", "preco": 139.90, "quantidade_estoque": 64, "estoque_minimo": 10, "fornecedor_id": 11 },
    { "produto_id": 23, "nome": "Catucai 1L", "descricao": "Garrafa de catucai 1L", "preco": 15.90, "quantidade_estoque": 62, "estoque_minimo": 10, "fornecedor_id": 12 },
    { "produto_id": 24, "nome": "Catucai 500ml", "descricao": "Garrafa de catucai 500ml", "preco": 9.00, "quantidade_estoque": 55, "estoque_minimo": 10, "fornecedor_id": 12 }
]);

// --- COMPRAS ---
db.Compras.insertMany([
    { "compra_id": 1, "produto_id": 1, "fornecedor_id": 1, "quantidade": 60, "valor_total": 390.00, "data_compra": new Date("2025-10-15T10:30:28") },
    { "compra_id": 2, "produto_id": 4, "fornecedor_id": 2, "quantidade": 25, "valor_total": 150.00, "data_compra": new Date("2025-10-16T14:45:46") },
    { "compra_id": 3, "produto_id": 6, "fornecedor_id": 3, "quantidade": 20, "valor_total": 260.00, "data_compra": new Date("2025-10-17T09:20:57") },
    { "compra_id": 4, "produto_id": 9, "fornecedor_id": 5, "quantidade": 15, "valor_total": 1798.50, "data_compra": new Date("2025-10-18T16:10:31") },
    { "compra_id": 5, "produto_id": 12, "fornecedor_id": 6, "quantidade": 30, "valor_total": 1797.00, "data_compra": new Date("2025-10-18T16:37:32") },
    { "compra_id": 6, "produto_id": 18, "fornecedor_id": 9, "quantidade": 50, "valor_total": 275.00, "data_compra": new Date("2025-10-20T14:45:29") },
    { "compra_id": 7, "produto_id": 23, "fornecedor_id": 12, "quantidade": 25, "valor_total": 397.50, "data_compra": new Date("2025-10-20T14:52:54") },
    { "compra_id": 8, "produto_id": 14, "fornecedor_id": 7, "quantidade": 10, "valor_total": 89.00, "data_compra": new Date("2025-10-21T13:17:21") }
]);