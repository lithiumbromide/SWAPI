---
title: "ImportFromExcel Method (IDimPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDimPatternFeatureData"
member: "ImportFromExcel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~ImportFromExcel.html"
---

# ImportFromExcel Method (IDimPatternFeatureData)

Imports a table from the specified Microsoft Excel file for this variable pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function ImportFromExcel( _
   ByVal ExcelFile As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimPatternFeatureData
Dim ExcelFile As System.String
Dim value As System.Integer

value = instance.ImportFromExcel(ExcelFile)
```

### C#

```csharp
System.int ImportFromExcel(
   System.string ExcelFile
)
```

### C++/CLI

```cpp
System.int ImportFromExcel(
   System.String^ ExcelFile
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ExcelFile`: Path and Microsoft Excel file name from which to import a table; valid filename extensions are **.xls**, **.xlsx**, and **.xlsm**

### Return Value

Status of importing a table from a Microsoft Excel file as defined in [swPatternFeatureImportExportError_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternFeatureImportExportError_e.html)

## VBA Syntax

See [DimPatternFeatureData::ImportFromExcel](ms-its:sldworksapivb6.chm::/sldworks~DimPatternFeatureData~ImportFromExcel.html).

## See Also

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.html)
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.html)
[IDimPatternFeatureData::ExportToExcel Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~ExportToExcel.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
