---
title: "ExportToExcel Method (InspectionProject)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionProject"
member: "ExportToExcel"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProject~ExportToExcel.html"
---

# ExportToExcel Method (InspectionProject)

Exports the inspection report to Microsoft Excel.

## Syntax

### Visual Basic (Declaration)

```vb
Function ExportToExcel( _
   ByVal TemplatePath As System.String, _
   ByVal FilePath As System.String, _
   ByVal Multisheet As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionProject
Dim TemplatePath As System.String
Dim FilePath As System.String
Dim Multisheet As System.Boolean
Dim value As System.Boolean

value = instance.ExportToExcel(TemplatePath, FilePath, Multisheet)
```

### C#

```csharp
System.bool ExportToExcel(
   System.string TemplatePath,
   System.string FilePath,
   System.bool Multisheet
)
```

### C++/CLI

```cpp
System.bool ExportToExcel(
   System.String^ TemplatePath,
   System.String^ FilePath,
   System.bool Multisheet
)
```

### Parameters

- `TemplatePath`: Full path name of the inspection report template to use (see **Remarks**)
- `FilePath`: Full path name of the Microsoft Excel file to export
- `Multisheet`: True if multisheet, false if not

### Return Value

True if export is successful, false if not

## VBA Syntax

See [InspectionProject](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProject_members.html) methods.

## Remarks

The templates are installed in **c:\ProgramData\SOLIDWORKS\SOLIDWORKS Inspection 2022 Addin\Templates**.

## See Also

[InspectionProject Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProject.html)
[InspectionProject Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProject_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
