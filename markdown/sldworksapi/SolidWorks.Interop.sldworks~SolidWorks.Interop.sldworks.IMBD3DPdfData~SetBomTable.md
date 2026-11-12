---
title: "SetBomTable Method (IMBD3DPdfData)"
project: "SOLIDWORKS API Help"
interface: "IMBD3DPdfData"
member: "SetBomTable"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetBomTable.html"
---

# SetBomTable Method (IMBD3DPdfData)

Maps a BOM Table Area in the [theme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ThemeName.html) with a BOM table in the model and sets the columns in the BOM table to export to the BOM Table Area in a SOLIDWORKS MBD 3D PDF.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetBomTable( _
   ByVal Index As System.Integer, _
   ByVal BomTableName As System.String, _
   ByVal Columns As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMBD3DPdfData
Dim Index As System.Integer
Dim BomTableName As System.String
Dim Columns As System.Object
Dim value As System.Integer

value = instance.SetBomTable(Index, BomTableName, Columns)
```

### C#

```csharp
System.int SetBomTable(
   System.int Index,
   System.string BomTableName,
   System.object Columns
)
```

### C++/CLI

```cpp
System.int SetBomTable(
   System.int Index,
   System.String^ BomTableName,
   System.Object^ Columns
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index of the BOM Table Area in the theme (see **Remarks**)
- `BomTableName`: Name of the BOM table to map to the BOM Table Area specified by Index (see **Remarks**)
- `Columns`: Array of strings of the names of the columns to export from the BOM table specified in BomTableName (see **Remarks**)

### Return Value

0 = success; BOM table mapped

1 = failure; specified BomTableName not found in model

## VBA Syntax

See [MBD3DPdfData::SetBomTable](ms-its:sldworksapivb6.chm::/sldworks~MBD3DPdfData~SetBomTable.html).

## Examples

[Export BOM's Second Column to BOM Table Area (C#)](Export_BOM's_Second_Column_to_BOM_Table_Area_Example_CSharp.htm)
[Export BOM's Second Column to BOM Table Area (VB.NET)](Export_BOM's_Second_Column_to_BOM_Table_Area_Example_VBNET.htm)
[Export BOM's Second Column to BOM Table Area (VBA)](Export_BOM's_Second_Column_to_BOM_Table_Area_Example_VB.htm)

## Remarks

| To get... | Call... |
| --- | --- |
| Index | IMBD3PdfData::GetBomAreaCount to find out the number of BOM Table Areas in the theme |
| BOMTableName | IBomFeature::Name |
| Columns | ITableAnnotation::ColumnCount to get the number of columns in the BOM table ITableAnnotation::GetColumnTitle for each column you want to export after getting the table annotation for the BOM table annotation |

## See Also

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html)
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.html)
[IMBD3DPdfData::ExcludeFromAnnotationView Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ExcludeFromAnnotationView.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
