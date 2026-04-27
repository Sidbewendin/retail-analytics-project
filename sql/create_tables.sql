-- Create customer dimension table, one row represents one customer
CREATE TABLE DimCustomer (
    CustomerID REAL PRIMARY KEY,
    Frequency INTEGER,
    Monetary FLOAT,
    LastPurchaseDate DATETIME,
    Recency INTEGER,
    R_score INTEGER,
    F_score INTEGER,
    M_score INTEGER,
    RFM_Score INTEGER,
    CustomerSegment TEXT
);

-- Create sales fact table, one row represents one transaction line
CREATE TABLE FactSales (
    InvoiceNo TEXT,
    StockCode TEXT,
    Description TEXT,
    Quantity INTEGER,
    InvoiceDate DATETIME,
    UnitPrice FLOAT,
    CustomerID INTEGER,
    Country TEXT,
    TotalPrice FLOAT,
    Year INTEGER,
    Month INTEGER,
    Day INTEGER,
    Hour INTEGER
);