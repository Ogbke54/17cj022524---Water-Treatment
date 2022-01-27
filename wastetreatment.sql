/****** Object:  Table [dbo].[watertreatment]    Script Date: 1/27/2022 1:08:36 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[watertreatment]') AND type in (N'U'))
DROP TABLE [dbo].[watertreatment]
GO

/****** Object:  Table [dbo].[watertreatment]    Script Date: 1/27/2022 1:08:36 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[watertreatment](
	[Country or Area] [text] NULL,
	[Year] [numeric](18, 0) NULL,
	[Value] [numeric](18, 0) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
SET QUOTED_IDENTIFIER ON

SELECT TOP (1000) [Country or Area]
    ,[Year]
    ,[Value]
FROM [dbo].[watertreatment]
