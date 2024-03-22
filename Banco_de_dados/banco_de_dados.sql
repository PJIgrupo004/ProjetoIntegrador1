-- Tabela Administrador
CREATE TABLE Administrador (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    senha VARCHAR(255)
);

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
    status ENUM('pendente', 'confirmado', 'realizado', 'cancelado'),
    observacoes TEXT,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (id_procedimento) REFERENCES Procedimentos(id_procedimento)
);

-- Tabela Histórico de Agendamentos
CREATE TABLE Historico_Agendamentos (
    id_historico INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_agendamento INT,
    data_realizacao DATE,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (id_agendamento) REFERENCES Agendamentos(id_agendamento)
);

-- Tabela posts_do_instagram
CREATE TABLE Posts_Instagram (
    ID_post INT AUTO_INCREMENT PRIMARY KEY,
    Status VARCHAR(50),
    Embedded TEXT,
    Data_inicial_exibicao DATE,
    Data_final_exibicao DATE
);

