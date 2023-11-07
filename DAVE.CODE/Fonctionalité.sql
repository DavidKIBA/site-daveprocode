-- Création de la base de données
CREATE DATABASE fonctionnalité;
USE fonctionnalité

-- Création de la table Utilisateur
CREATE TABLE Utilisateur (
    ID_Utilisateur INT PRIMARY KEY(ID_Utilisateur),
    Nom VARCHAR(255),
    Email VARCHAR(255),
    Mot_de_passe VARCHAR(255)
    
);

-- Création de la table Produit
CREATE TABLE Produit (
    ID_Produit INT PRIMARY KEY(ID_Produit),
    Nom VARCHAR(255),
    Description TEXT,
    Prix DECIMAL(10, 2),
    Stock INT
    
);

-- Création de la table Service
CREATE TABLE Service (
    ID_Service INT PRIMARY KEY(ID_Service),
    Nom VARCHAR(255),
    Description TEXT,
    Prix DECIMAL(10, 2)
    
);

-- Création de la table Commande
CREATE TABLE Commande (
    ID_Commande INT PRIMARY KEY,
    Date DATE,
    ID_Utilisateur INT,
    FOREIGN KEY (ID_Utilisateur) REFERENCES Utilisateur(ID_Utilisateur)
    
);

-- Création de la table Produit_Commande pour la relation entre Commande et Produit
CREATE TABLE Produit_Commande (
    ID_Produit INT,
    ID_Commande INT,
    Quantite INT,
    FOREIGN KEY (ID_Produit) REFERENCES Produit(ID_Produit),
    FOREIGN KEY (ID_Commande) REFERENCES Commande(ID_Commande),
    PRIMARY KEY (ID_Produit, ID_Commande)
);

-- Création de la table Commentaire
CREATE TABLE Commentaire (
    ID_Commentaire INT PRIMARY KEY,
    ID_Utilisateur INT,
    ID_ProduitService INT,
    Contenu TEXT,
    Date DATE,
    FOREIGN KEY (ID_Utilisateur) REFERENCES Utilisateur(ID_Utilisateur)
    
);



