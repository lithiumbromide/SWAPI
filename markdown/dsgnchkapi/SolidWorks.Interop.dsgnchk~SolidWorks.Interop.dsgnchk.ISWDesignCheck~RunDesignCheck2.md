---
title: "RunDesignCheck2 Method (ISWDesignCheck)"
project: "SOLIDWORKS Design Checker API Help"
interface: "ISWDesignCheck"
member: "RunDesignCheck2"
kind: "method"
source: "dsgnchkapi/SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck~RunDesignCheck2.html"
---

# RunDesignCheck2 Method (ISWDesignCheck)

Obsolete. Superseded by [ISWDesignCheck::RunDesignCheck3](SOLIDWORKS.Interop.dsgnchk~SOLIDWORKS.Interop.dsgnchk.ISWDesignCheck~RunDesignCheck3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function RunDesignCheck2( _
   ByVal StandardFileName As System.String, _
   ByVal ReportFolderName As System.String, _
   ByVal AddReportToDesignBinder As System.Boolean, _
   ByVal OverWriteReport As System.Boolean, _
   ByVal bCanViewReportOnSave As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISWDesignCheck
Dim StandardFileName As System.String
Dim ReportFolderName As System.String
Dim AddReportToDesignBinder As System.Boolean
Dim OverWriteReport As System.Boolean
Dim bCanViewReportOnSave As System.Boolean
Dim value As System.Integer

value = instance.RunDesignCheck2(StandardFileName, ReportFolderName, AddReportToDesignBinder, OverWriteReport, bCanViewReportOnSave)
```

### C#

```csharp
System.int RunDesignCheck2(
   System.string StandardFileName,
   System.string ReportFolderName,
   System.bool AddReportToDesignBinder,
   System.bool OverWriteReport,
   System.bool bCanViewReportOnSave
)
```

### C++/CLI

```cpp
System.int RunDesignCheck2(
   System.String^ StandardFileName,
   System.String^ ReportFolderName,
   System.bool AddReportToDesignBinder,
   System.bool OverWriteReport,
   System.bool bCanViewReportOnSave
)
```

### Parameters

- `StandardFileName`: Path and filename of SOLIDWORKS Design Checker standards document
- `ReportFolderName`: Name of report

  **NOTE:** A filename extension of **.dxp** is automatically appended to the specified filename. The report is an XML file.
- `AddReportToDesignBinder`: True to add the report to the Design Binder, false to not
- `OverWriteReport`: True to overwrite any existing report of the same name in the Design Binder, false to not
- `bCanViewReportOnSave`: True to display the report when saved, false to not

### Return Value

Error code as defined in [dsgnchkError_e](SOLIDWORKS.Interop.dsgnchk~SOLIDWORKS.Interop.dsgnchk.dsgnchkError_e.html)

## VBA Syntax

See [SWDesignCheck::RunDesignCheck2](ms-its:dsgnchkapivb6.chm::/DesignCheckerLib~SWDesignCheck~RunDesignCheck2.html).

## Remarks

This method can also add a new, or overwrite an existing, report to the Design Binder.

## See Also

[ISWDesignCheck Interface](SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck.html)
[ISWDesignCheck Members](SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
