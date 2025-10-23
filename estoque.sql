CREATE DATABASE IF NOT EXISTS estoque;
USE estoque;

CREATE TABLE Fornecedores (
    fornecedor_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100),
    endereco VARCHAR(200)
);

CREATE TABLE Produtos (
    produto_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10,2) NOT NULL,
    quantidade_estoque INT NOT NULL,
    estoque_minimo INT NOT NULL,
    fornecedor_id INT NOT NULL,
    CONSTRAINT fk_produto_fornecedor
        FOREIGN KEY (fornecedor_id)
        REFERENCES Fornecedores(fornecedor_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
CREATE TABLE Compras (
    compra_id INT AUTO_INCREMENT PRIMARY KEY,
    produto_id INT NOT NULL,
    fornecedor_id INT NOT NULL,
    quantidade INT NOT NULL,
    data_compra DATETIME NOT NULL,
    CONSTRAINT fk_compra_produto
        FOREIGN KEY (produto_id)
        REFERENCES Produtos(produto_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    CONSTRAINT fk_compra_fornecedor
        FOREIGN KEY (fornecedor_id)
        REFERENCES Fornecedores(fornecedor_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
INSERT INTO Fornecedores (nome, telefone, email, endereco)
VALUES 
('Ambev', '(27) 98171-1808', 'Ambev@gmail.com', 'Moacir avidos, 120'),
('Heineken', '(27) 67821-1236', 'Heineken@gmail.com', 'Joaquim Lirio, 152'),
('Coca-cola', '(27) 97385-5138', 'Cocacola@gmail.com', 'Vila Rubim, 45'),
('Campari', '(27) 93621-8153', 'Campari@gmail.com', 'Praia da Costa, 102'),
('Jack-Daniels', '(27) 73782-3124', 'JackDaniels@gmail.com', 'Castanheiras, 55'),
('Vinicola Salton', '(27) 82641-9172', 'SaltonVinhos@gmail.com', 'Reta da penha, 33'),
('RedBull', '(27) 89154-0192', 'Redbull@gmail.com', 'Rua das flores, 3'),
('Vinicola Miolo', '(27) 35613-7712', 'MiolosVinhos@gmail.com', 'Ozorio Brito, 284'),
('Fanta', '(27) 12463-8821', 'Fanta@gmail.com', 'Santo antonio, 320'),
('Del Valle', '(27) 99153-2190', 'DelValle@gmail.com', 'Barro vermelho, 201'),
('Stock', '(27) 26841-2252', 'Stock@gmail.com', 'Avenida Vitoria, 156'),
('Catucai', '(27) 84926-8413', 'Catucai@gmail.com', 'Savassi, 62');

INSERT INTO Produtos (nome, descricao, preco, quantidade_estoque, estoque_minimo, fornecedor_id)
VALUES
('Corona', 'Long neck corona', 6.50, 120, 10, 1),
('Skol', 'Lata de skol', 4.20, 76, 10, 1),
('Heineken 1L', 'Garrafa Heineken 1L', 14.00, 62, 10, 2),
('Heineken Long neck', 'Garrada Heineken 320ml', 6.00, 231, 10, 2),
('Coca-cola 1L', 'Garrafa Coca-cola 1L', 9.00, 61, 10, 3),
('Coca-cola 2L', 'Garrafa Coca-cola 2L', 13.00, 48, 10, 3),
('Campari', 'Garrafa de campari', 52.90, 60, 16, 4),
('Aperol', 'Garrafa de aperol', 59.90, 25, 28, 4),
('Jack-Daniels original', 'Garrafa sabor original', 119.90, 55, 10, 5),
('Jack-Daniels apple', 'Garrafa sabor maca', 119.90, 77, 10, 5),
('Vinho San Martin', 'Vinho chileno', 89.90, 83, 10, 6),
('Vinho Merlot', 'Vinho argentino', 59.90, 55, 10, 6),
('RedBull Original', 'Lata RedBull original', 8.90, 35, 10, 7),
('RedBull Melancia', 'Lata RedBull melancia', 8.90, 43, 10, 7),
('Vinho Origini', 'Vinho frances', 49.90, 52, 10, 8),
('Vinho Casa Blanca', 'Vinho espanhol', 40.00, 41, 10, 8),
('Fanta Uva', 'Lata fanta uva', 5.50, 112, 10, 9),
('Fanta Laranja', 'Lata fanta laranja', 5.50, 98, 10, 9),
('Suco de morango', 'Garrafa suco de laranja 1L', 9.50, 83, 10, 10),
('Suco de limao', 'Garrafa suco de limao 1L', 9.50, 68, 10, 10),
('Gin dry cat', 'Garrafa gin dry cat', 119.90, 45, 10, 11),
('Gin tropical', 'Garrafa gin tropical', 139.90, 64, 10, 11),
('Catucai 1L', 'Garrafa de catucai 1L', 15.90, 62, 10, 12),
('Catucai 500ml', 'Garrafa de catucai 500ml', 9.00, 55, 10, 12);

INSERT INTO Compras (produto_id, fornecedor_id, quantidade, data_compra)
VALUES
(1, 1, 60, '2025-10-15 10:30:28'),
(4, 2, 25, '2025-10-16 14:45:46'),
(6, 3, 20, '2025-10-17 09:20:57'),
(9, 5, 15, '2025-10-18 16:10:31'),
(12, 6, 30, '2025-10-18 16:37:32'),
(18, 9, 50, '2025-10-20 14:45:29'),
(23, 12, 25, '2025-10-20 14:52:54'),
(14, 7, 10, '2025-10-21 13:17:21');
