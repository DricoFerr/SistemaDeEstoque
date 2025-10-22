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
    valor_total DECIMAL(10,2) NOT NULL,
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
('Chocolates garoto', '(27) 98171-1808', 'Garoto@gmail.com', 'Moacir avidos, 120'),
('Bauduco', '(27) 67821-1236', 'Bauduco@gmail.com', 'Joaquim Lirio, 999'),
('Friboi', '(27) 97385-5138', 'Friboi@gmail.com', 'Vila Rubim, 45'),
('Danone', '(27) 93621-8153', 'Danone@gmail.com', 'Praia da Costa, 102'),
('Bebidas e cia', '(27) 19823-5321', 'Bebidas@gmail.com', 'Castanheiras , 55');

INSERT INTO Produtos (nome, descricao, preco, quantidade_estoque, estoque_minimo, fornecedor_id)
VALUES
('Kit-kat', 'barra kit kat', 5.50, 100, 10, 1),
('Bombom serenata', 'unidade de bombom serenata', 3.20, 120, 15, 1),
('Cookies', 'pacote de cookies', 8.00, 50, 5, 2),
('Bolo', 'Bolo de chocolate', 15.00, 20, 5, 2),
('Frango', 'Filé de frango', 18.00, 40, 10, 3),
('Carne', 'Carne moída', 25.00, 30, 5, 3),
('Leite', 'Leite 1L', 4.50, 60, 10, 4),
('Queijo', 'Queijo mussarela', 22.00, 25, 5, 4),
('Coca-cola', 'Garrafa 2L', 8.50, 80, 10, 5),
('Fanta', 'Garrafa fanta uva 1L', 6.00, 50, 10, 5);

INSERT INTO Compras (produto_id, fornecedor_id, quantidade, data_compra, valor_total)
VALUES
(1, 1, 50, '2025-10-15 10:30:00', 275.00),
(4, 2, 10, '2025-10-16 14:45:00', 150.00),
(6, 3, 15, '2025-10-17 09:20:00', 375.00),
(9, 5, 20, '2025-10-18 16:10:00', 170.00);