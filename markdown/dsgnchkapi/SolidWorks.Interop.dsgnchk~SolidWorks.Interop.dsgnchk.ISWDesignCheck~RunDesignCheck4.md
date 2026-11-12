---
title: "RunDesignCheck4 Method (ISWDesignCheck)"
project: "SOLIDWORKS Design Checker API Help"
interface: "ISWDesignCheck"
member: "RunDesignCheck4"
kind: "method"
source: "dsgnchkapi/SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck~RunDesignCheck4.html"
---

# RunDesignCheck4 Method (ISWDesignCheck)

Obsolete. Superseded by [ISWDesignCheck::RunDesignCheck5](SOLIDWORKS.Interop.dsgnchk~SOLIDWORKS.Interop.dsgnchk.ISWDesignCheck~RunDesignCheck5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function RunDesignCheck4( _
   ByVal StandardFileName As System.String, _
   ByVal ReportFolderName As System.String, _
   ByVal AddReportToDesignBinder As System.Boolean, _
   ByVal OverWriteReport As System.Boolean, _
   ByVal AutoCorrect As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISWDesignCheck
Dim StandardFileName As System.String
Dim ReportFolderName As System.String
Dim AddReportToDesignBinder As System.Boolean
Dim OverWriteReport As System.Boolean
Dim AutoCorrect As System.Boolean
Dim value As System.Integer

value = instance.RunDesignCheck4(StandardFileName, ReportFolderName, AddReportToDesignBinder, OverWriteReport, AutoCorrect)
```

### C#

```csharp
System.int RunDesignCheck4(
   System.string StandardFileName,
   System.string ReportFolderName,
   System.bool AddReportToDesignBinder,
   System.bool OverWriteReport,
   System.bool AutoCorrect
)
```

### C++/CLI

```cpp
System.int RunDesignCheck4(
   System.String^ StandardFileName,
   System.String^ ReportFolderName,
   System.bool AddReportToDesignBinder,
   System.bool OverWriteReport,
   System.bool AutoCorrect
)
```

### Parameters

- `StandardFileName`: Path and filename of SOLIDWORKS Design Checker standards document
- `ReportFolderName`: Path and folder name for pre- and post-condition reports (see **Remarks**)
- `AddReportToDesignBinder`: True to add the report to the Design Binder, false to not
- `OverWriteReport`: True to overwrite any existing report of the same name in the Design Binder, false to not
- `AutoCorrect`: True to autocorrect all failures discovered by Design Checker, false to not

### Return Value

Error code as defined in [dsgnchkError_e](SOLIDWORKS.Interop.dsgnchk~SOLIDWORKS.Interop.dsgnchk.dsgnchkError_e.html)

## VBA Syntax

See [SWDesignCheck::RunDesignCheck4](ms-its:dsgnchkapivb6.chm::/DesignCheckerLib~SWDesignCheck~RunDesignCheck4.html).

## Examples

[Run SOLIDWORKS Design Checker (C#)](Run_SOLIDWORKS_Design_Checker_Example_CSharp.htm)
[Run SOLIDWORKS Design Checker (VB.NET)](Run_SOLIDWORKS_Design_Checker_Example_VBNET.htm)
[Run SOLIDWORKS Design Checker (VBA)](Run_SOLIDWORKS_Design_Checker_Example_VB.htm)

## Remarks

The date and time are automatically appended to the name of the folder specified for ReportFolderName. For example, if you specified **"c:\test\Food Processor"** for ReportFolderName and you ran your macro on July 28, 2009 at 8:30 a.m., then **c:\test\Food Processor_7_28_2009_8:30** is the name of the folder created. **Post-Correction Result** and **Pre-Correction Result** subfolders are also created, depending on the value specified for AutoCorrect. The post- and pre-condition reports are created in these subfolders.

| If AutoCorrect is set to... | Then these reports are created... |
| --- | --- |
| True | Design Binder: Post-Correction Result.dxp and Pre-Correction Result.dxp Post-Correction Result and Pre-Correction Result subfolders: SWDCReport.xml |
| False | Design Binder: Pre-Correction Result.dxp Pre-Correction Result subfolder: SWDCReport.xml |

## See Also

[ISWDesignCheck Interface](SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck.html)
[ISWDesignCheck Members](SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
