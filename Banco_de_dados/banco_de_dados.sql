-- Tabela Clientes
CREATE TABLE Clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    telefone VARCHAR(20),
    data_nascimento DATE,
    endereco VARCHAR(255),
    facebook VARCHAR(255),
    instagram VARCHAR(255)
);

-- Tabela Usuários
CREATE TABLE usuarios (
  id_usuario INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  usuario VARCHAR(255) NULL,
  senha VARCHAR(45) NULL
);

-- Tabela Procedimentos
CREATE TABLE Procedimentos (
    id_procedimento INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    tempo TIME,
    valor DECIMAL(10,2),
    descricao TEXT
);

-- Tabela Produtos
CREATE TABLE Produtos (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    marca VARCHAR(255),
    valor DECIMAL(10,2),
    data_validade DATE,
    quant_estoque INT
);

-- Tabela Agendamentos
CREATE TABLE Agendamentos (
    id_agendamento INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_procedimento INT,
    data_agendamento DATE,
    hora_agendamento TIME,
    data_realizacao DATE,
    status ENUM('pendente', 'confirmado', 'realizado', 'cancelado'),
    observacoes TEXT,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (id_procedimento) REFERENCES Procedimentos(id_procedimento)
);

-- Tabela posts_do_instagram
CREATE TABLE Posts_Instagram (
    ID_post INT AUTO_INCREMENT PRIMARY KEY,
    Status VARCHAR(50),
    Embedded TEXT,
    Data_inicial_exibicao DATE,
    Data_final_exibicao DATE
);

