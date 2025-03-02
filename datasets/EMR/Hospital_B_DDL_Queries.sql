CREATE TABLE Departments(
	DeptID NVARCHAR(55) PRIMARY KEY,
	Name NVARCHAR(55)
);

CREATE TABLE Encounters(
	EncounterID NVARCHAR(55) PRIMARY KEY,
	PatientID NVARCHAR(55),
	EncounterDate DATE,
	EncounterType NVARCHAR(55),
	ProviderID NVARCHAR(55),
	DepartmentID NVARCHAR(55),
	ProcedureCode INTEGER,
	InsertedDate DATE,
	ModifiedDate DATE
);

CREATE TABLE Patients(
	ID NVARCHAR(55) PRIMARY KEY,
	F_Name NVARCHAR(55),
	L_Name NVARCHAR(55),
	M_Name NVARCHAR(55),
	SSN NVARCHAR(55),
	PhoneNumber NVARCHAR(55),
	Gender NVARCHAR(55),
	DOB DATE,
	Address NVARCHAR(255),
	Updated_Date DATE
);

CREATE TABLE Providers(
	ProviderID NVARCHAR(55) PRIMARY KEY,
	FirstName NVARCHAR(55),
	LastName NVARCHAR(55),
	Specialization NVARCHAR(55),
	DeptID NVARCHAR(55),
	NPI BIGINT
);

CREATE TABLE Transactions(
	TransactionID NVARCHAR(55) PRIMARY KEY,
	EncounterID NVARCHAR(55),
	PatientID NVARCHAR(55),
	ProviderID NVARCHAR(55),
	DeptID NVARCHAR(55),
	VisitDate DATE,
	ServiceDate DATE,
	PaidDate DATE,
	VisitType NVARCHAR(55),
	Amount FLOAT(20),
	AmountType NVARCHAR(55),
	PaidAmount FLOAT(20),
	ClaimID NVARCHAR(55),
	PayorID NVARCHAR(55),
	ProcedureCode NVARCHAR(55),
	ICDCode NVARCHAR(55),
	LineOfBusiness NVARCHAR(55),
	MedicaidID NVARCHAR(55),
	MedicareID NVARCHAR(55),
	InsertDate DATE,
	ModifiedDate DATE
);
