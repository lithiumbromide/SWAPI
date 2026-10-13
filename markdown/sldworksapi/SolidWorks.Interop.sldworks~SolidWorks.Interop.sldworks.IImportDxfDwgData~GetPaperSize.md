---
title: "GetPaperSize Method (IImportDxfDwgData)"
project: "SOLIDWORKS API Help"
interface: "IImportDxfDwgData"
member: "GetPaperSize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetPaperSize.html"
---

# GetPaperSize Method (IImportDxfDwgData)

Gets the size of the paper for the drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetPaperSize( _
   ByVal Sheet As System.String, _
   ByRef Size As System.Integer, _
   ByRef Height As System.Double, _
   ByRef Width As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim Size As System.Integer
Dim Height As System.Double
Dim Width As System.Double

instance.GetPaperSize(Sheet, Size, Height, Width)
```

### C#

```csharp
void GetPaperSize(
   System.string Sheet,
   out System.int Size,
   out System.double Height,
   out System.double Width
)
```

### C++/CLI

```cpp
void GetPaperSize(
   System.String^ Sheet,
   [Out] System.int Size,
   [Out] System.double Height,
   [Out] System.double Width
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Sheet`: Sheet (layout) name of the input file or an empty string for all sheets
- `Size`: Size as defined in [swDwgPaperSizes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html)
- `Height`: If Size is swDwgPapersUserDefined, then the height of the paper in meters
- `Width`: If Size is swDwgPapersUserDefined, then the width of the paper in meters

## VBA Syntax

See [ImportDxfDwgData::GetPaperSize](ms-its:sldworksapivb6.chm::/sldworks~ImportDxfDwgData~GetPaperSize.html).

## Remarks

This method only supports importing to a drawing; it does not support importing to a part sketch.

## See Also

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.html)
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.html)
[IImportDxfDwgData::SetPaperSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetPaperSize.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
