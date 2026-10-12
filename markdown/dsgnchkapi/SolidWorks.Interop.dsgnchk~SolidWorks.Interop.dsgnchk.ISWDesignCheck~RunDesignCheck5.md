---
title: "RunDesignCheck5 Method (ISWDesignCheck)"
project: "SOLIDWORKS Design Checker API Help"
interface: "ISWDesignCheck"
member: "RunDesignCheck5"
kind: "method"
source: "dsgnchkapi/SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck~RunDesignCheck5.html"
---

# RunDesignCheck5 Method (ISWDesignCheck)

Runs the SOLIDWORKS Design Checker using the specified standards document.

## Syntax

### Visual Basic (Declaration)

```vb
Function RunDesignCheck5( _
   ByVal StandardFileName As System.String, _
   ByVal ReportFolderName As System.String, _
   ByVal AddReportToDesignBinder As System.Boolean, _
   ByVal OverWriteReport As System.Boolean, _
   ByVal AutoCorrect As System.Boolean, _
   ByRef lReportFormat As System.Integer, _
   ByRef ResultSummary As System.String _
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
Dim lReportFormat As System.Integer
Dim ResultSummary As System.String
Dim value As System.Integer

value = instance.RunDesignCheck5(StandardFileName, ReportFolderName, AddReportToDesignBinder, OverWriteReport, AutoCorrect, lReportFormat, ResultSummary)
```

### C#

```csharp
System.int RunDesignCheck5(
   System.string StandardFileName,
   System.string ReportFolderName,
   System.bool AddReportToDesignBinder,
   System.bool OverWriteReport,
   System.bool AutoCorrect,
   out System.int lReportFormat,
   out System.string ResultSummary
)
```

### C++/CLI

```cpp
System.int RunDesignCheck5(
   System.String^ StandardFileName,
   System.String^ ReportFolderName,
   System.bool AddReportToDesignBinder,
   System.bool OverWriteReport,
   System.bool AutoCorrect,
   [Out] System.int lReportFormat,
   [Out] System.String^ ResultSummary
)
```

### Parameters

- `StandardFileName`: Path and filename of SOLIDWORKS Design Checker standards document
- `ReportFolderName`: Path and folder name for report
- `AddReportToDesignBinder`: True to add the report to the Design Binder, false to not (see **Remarks**)
- `OverWriteReport`: True to overwrite any existing report of the same name in the Design Binder, false to not
- `AutoCorrect`: True to autocorrect all failures discovered by Design Checker, false to not (see **Remarks**)
- `lReportFormat`: 0=XML format, 1=Microsoft Word format (see **Remarks**)
- `ResultSummary`: Failure counts

### Return Value

Error code as defined in [dsgnchkError_e](SOLIDWORKS.Interop.dsgnchk~SOLIDWORKS.Interop.dsgnchk.dsgnchkError_e.html)

## VBA Syntax

See [SWDesignCheck::RunDesignCheck5](ms-its:dsgnchkapivb6.chm::/DesignCheckerLib~SWDesignCheck~RunDesignCheck5.html).

## Examples

[Run SOLIDWORKS Design Checker Example (VBA)](Run_SOLIDWORKS_Design_Checker_Example_VB.htm)
[Run SOLIDWORKS Design Checker Example (VB.NET)](Run_SOLIDWORKS_Design_Checker_Example_VBNET.htm)
[Run SOLIDWORKS Design Checker Example (C#)](Run_SOLIDWORKS_Design_Checker_Example_CSharp.htm)

## Remarks

| If lReportFormat is set to... | Then ReportFolderName directory contains... | lReportFormat returns... |
| --- | --- | --- |
| 0 | SWDCReport.xml and SWDCReport.xsl | 0 |
| 1 | SWDCReport.doc (if Microsoft Word is installed) SWDCReport.xml and SWDCReport.xsl (if Microsoft Word is not installed) | 1 0 |

| If AutoCorrect is set to... | Then ResultSummary contains... |
| --- | --- |
| False | Failure counts delimited by the at symbol (@): Critical#@High#@Medium#@Low# |
| True | Pre- and post-correction failure counts delimited by the at symbol (@): Critical#(pre)@High#(pre)@Medium#(pre)@Low#(pre)@Critical#(post)@High#(post)@Medium#(post)@Low#(post) Only failures that were found after the correction cycle display in the report. |

If AddReportToDesignBinder is set to true, then the SOLIDWORKS FeatureManager Design Binder contains **`<ReportFolderName>`.drp.**

## See Also

[ISWDesignCheck Interface](SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck.html)
[ISWDesignCheck Members](SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
