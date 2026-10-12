---
title: "ExportToExcel Method (IDimPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDimPatternFeatureData"
member: "ExportToExcel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~ExportToExcel.html"
---

# ExportToExcel Method (IDimPatternFeatureData)

Exports the pattern table to the specified Microsoft Excel file for this variable pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function ExportToExcel( _
   ByVal ExcelFile As System.String, _
   ByVal Overwrite As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimPatternFeatureData
Dim ExcelFile As System.String
Dim Overwrite As System.Boolean
Dim value As System.Integer

value = instance.ExportToExcel(ExcelFile, Overwrite)
```

### C#

```csharp
System.int ExportToExcel(
   System.string ExcelFile,
   System.bool Overwrite
)
```

### C++/CLI

```cpp
System.int ExportToExcel(
   System.String^ ExcelFile,
   System.bool Overwrite
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ExcelFile`: Path and Microsoft Excel file name to which to export the pattern table; valid filename extensions are **.xls**, **.xlsx**, and **.xlsm**
- `Overwrite`: True to overwrite a file in the specified path with the same file name, false to not

### Return Value

Status of exporting the pattern table to a Microsoft Excel file as defined in [swPatternFeatureImportExportError_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternFeatureImportExportError_e.html)

## VBA Syntax

See [DimPatternFeatureData::ExportToExcel](ms-its:sldworksapivb6.chm::/sldworks~DimPatternFeatureData~ExportToExcel.html).

## Examples

[Insert Variable Pattern Feature (C#)](Insert_Advanced_Variable_Pattern_Feature_Example_CSharp.htm)
[Insert Variable Pattern Feature (VB.NET)](Insert_Advanced_Variable_Pattern_Feature_Example_VBNET.htm)
[Insert Variable Pattern Feature (VBA)](Insert_Advanced_Variable_Pattern_Feature_Example_VB.htm)

## See Also

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.html)
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.html)
[IDimPatternFeatureData::ImportFromExcel Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~ImportFromExcel.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
