/*
CREATE TABLE dbo.Departments (
    DepartmentID NVARCHAR(20) PRIMARY KEY,
    Name NVARCHAR(100) NOT NULL
);


CREATE TABLE dbo.Encounters(
	EncounterID NVARCHAR(20) PRIMARY KEY,
	PatientID NVARCHAR(20),
	EncounterDate DATE,
	EncounterType NVARCHAR(20),
	ProviderID NVARCHAR(20),
	DepartmentID NVARCHAR(20),
	ProcedureCode INTEGER,
	InsertedDate DATE,
	ModifiedDate DATE
);



CREATE TABLE dbo.Patients(
	PatientID NVARCHAR(20) PRIMARY KEY,
	FirstName NVARCHAR(55),
	LastName NVARCHAR(55),
	MiddleName NVARCHAR(55),
	SSN NVARCHAR(11),
	PhoneNumber NVARCHAR(20),
	Gender CHAR(6),
	DOB DATE,
	Address VARCHAR(255),
	ModifiedDate DATE
);



CREATE TABLE dbo.Providers(
	ProviderID NVARCHAR(20) PRIMARY KEY,
	FirstName NVARCHAR(55),
	LastName NVARCHAR(55),
	Specialization VARCHAR(55),
	DepartmentID NVARCHAR(55),
	NPI VARCHAR(55)
);




CREATE TABLE dbo.Transactions(
	TransactionID NVARCHAR(20) PRIMARY KEY,
	EncounterID NVARCHAR(20),
	PatientID NVARCHAR(20),
	ProviderID NVARCHAR(20),
	DepartmentID NVARCHAR(20),
	VisitDate DATE,
	ServiceDate DATE,
	PaidDate DATE,
	VisitType VARCHAR(55),
	Amount DECIMAL(20, 20),
	AmountType VARCHAR(55),
	PaidAmount DECIMAL(20, 20),
	ClaimID VARCHAR(55),
	PayorID VARCHAR(55),
	ProcedureCode INTEGER,
	ICDCode NVARCHAR(55),
	LineOfBusiness VARCHAR(55),
	MedicaidID VARCHAR(55),
	MedicareID VARCHAR(55),
	InsertDate DATE,
	ModifiedDate DATE
);

*/
