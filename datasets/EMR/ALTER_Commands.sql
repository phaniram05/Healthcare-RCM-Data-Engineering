/*
ALTER TABLE [dbo].[Patients]
ALTER COLUMN PhoneNumber VARCHAR(55);
*/

SELECT * FROM [dbo].[Patients];

SELECT * FROM [dbo].[Providers];

ALTER TABLE [dbo].[Transactions]
ALTER COLUMN Amount FLOAT(20);

ALTER TABLE [dbo].[Transactions]
ALTER COLUMN PaidAmount FLOAT(20);


SELECT * FROM [dbo].[Transactions];