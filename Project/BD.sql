-- Table pour les Écoles
CREATE TABLE Ecoles (
    EcoleID INT PRIMARY KEY,
    Nom VARCHAR(255) NOT NULL,
    Adresse VARCHAR(255) NOT NULL,
    -- d'autres informations sur l'école
);

-- Table pour les Élèves
CREATE TABLE Eleves (
    EleveID INT PRIMARY KEY,
    EcoleID INT,
    Nom VARCHAR(255) NOT NULL,
    Classe VARCHAR(50) NOT NULL,
    -- d'autres informations sur les élèves
    FOREIGN KEY (EcoleID) REFERENCES Ecoles(EcoleID)
);

-- Table pour les Messages
CREATE TABLE Messages (
    MessageID INT PRIMARY KEY,
    EcoleID INT,
    ParentID INT, -- Si le message est adressé à un parent spécifique
    Classe VARCHAR(50), -- Si le message est adressé à une classe spécifique
    Contenu TEXT NOT NULL,
    DateEnvoi DATETIME NOT NULL,
    -- d'autres informations sur les messages
    FOREIGN KEY (EcoleID) REFERENCES Ecoles(EcoleID)
);

-- Table pour les Résultats des Examens
CREATE TABLE ResultatsExamens (
    ResultatID INT PRIMARY KEY,
    EleveID INT,
    Matiere VARCHAR(50) NOT NULL,
    Note DECIMAL(5, 2) NOT NULL,
    DateExamen DATE NOT NULL,
    -- d'autres informations sur les résultats des examens
    FOREIGN KEY (EleveID) REFERENCES Eleves(EleveID)
);

-- Table pour les Emplois du Temps
CREATE TABLE EmploisDuTemps (
    EmploiID INT PRIMARY KEY,
    Classe VARCHAR(50) NOT NULL,
    JourSemaine VARCHAR(20) NOT NULL,
    HeureDebut TIME NOT NULL,
    HeureFin TIME NOT NULL,
    Matiere VARCHAR(50) NOT NULL,
    -- d'autres informations sur les emplois du temps
);

-- Table pour le Calendrier Scolaire
CREATE TABLE CalendrierScolaire (
    CalendrierID INT PRIMARY KEY,
    Date DATE NOT NULL,
    Description TEXT NOT NULL,
    -- d'autres informations sur le calendrier scolaire
);

-- Table pour le Statut Financier des Élèves
CREATE TABLE StatutFinancier (
    StatutID INT PRIMARY KEY,
    EleveID INT,
    MontantDue DECIMAL(10, 2) NOT NULL,
    MontantPaye DECIMAL(10, 2) NOT NULL,
    DateMiseAJour DATE NOT NULL,
    -- d'autres informations sur le statut financier ici
    FOREIGN KEY (EleveID) REFERENCES Eleves(EleveID)
);

-- Table pour la Progression des Élèves
CREATE TABLE ProgressionEleves (
    ProgressionID INT PRIMARY KEY,
    EleveID INT,
    Matiere VARCHAR(50) NOT NULL,
    Progres DECIMAL(5, 2) NOT NULL,
    DateMiseAJour DATE NOT NULL,
    -- d'autres informations sur la progression des élèves
    FOREIGN KEY (EleveID) REFERENCES Eleves(EleveID)
);

-- Index pour accélérer les recherches, par exemple :
CREATE INDEX idx_Eleves_Classe ON Eleves(Classe);
CREATE INDEX idx_ResultatsExamens_EleveID ON ResultatsExamens(EleveID);

