---
title: "RunDesignCheck Method (ISWDesignCheck)"
project: "SOLIDWORKS Design Checker API Help"
interface: "ISWDesignCheck"
member: "RunDesignCheck"
kind: "method"
source: "dsgnchkapi/SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck~RunDesignCheck.html"
---

# RunDesignCheck Method (ISWDesignCheck)

Obsolete. Superseded by [ISWDesignCheck::RunDesignCheck2](SOLIDWORKS.Interop.dsgnchk~SOLIDWORKS.Interop.dsgnchk.ISWDesignCheck~RunDesignCheck2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function RunDesignCheck( _
   ByVal StandardFileName As System.String, _
   ByVal ReportFolderName As System.String, _
   ByVal AddReportToDesignBinder As System.Boolean, _
   ByVal OverWriteReport As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISWDesignCheck
Dim StandardFileName As System.String
Dim ReportFolderName As System.String
Dim AddReportToDesignBinder As System.Boolean
Dim OverWriteReport As System.Boolean
Dim value As System.Integer

value = instance.RunDesignCheck(StandardFileName, ReportFolderName, AddReportToDesignBinder, OverWriteReport)
```

### C#

```csharp
System.int RunDesignCheck(
   System.string StandardFileName,
   System.string ReportFolderName,
   System.bool AddReportToDesignBinder,
   System.bool OverWriteReport
)
```

### C++/CLI

```cpp
System.int RunDesignCheck(
   System.String^ StandardFileName,
   System.String^ ReportFolderName,
   System.bool AddReportToDesignBinder,
   System.bool OverWriteReport
)
```

### Parameters

- `StandardFileName`:
- `ReportFolderName`:
- `AddReportToDesignBinder`:
- `OverWriteReport`:

## VBA Syntax

See [SWDesignCheck::RunDesignCheck](ms-its:dsgnchkapivb6.chm::/DesignCheckerLib~SWDesignCheck~RunDesignCheck.html).

## See Also

[ISWDesignCheck Interface](SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck.html)
[ISWDesignCheck Members](SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck_members.html)
