---
title: "SetPaperSize Method (IImportDxfDwgData)"
project: "SOLIDWORKS API Help"
interface: "IImportDxfDwgData"
member: "SetPaperSize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetPaperSize.html"
---

# SetPaperSize Method (IImportDxfDwgData)

Sets the size of the paper in the drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPaperSize( _
   ByVal Sheet As System.String, _
   ByVal Size As System.Integer, _
   ByVal Height As System.Double, _
   ByVal Width As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim Size As System.Integer
Dim Height As System.Double
Dim Width As System.Double
Dim value As System.Boolean

value = instance.SetPaperSize(Sheet, Size, Height, Width)
```

### C#

```csharp
System.bool SetPaperSize(
   System.string Sheet,
   System.int Size,
   System.double Height,
   System.double Width
)
```

### C++/CLI

```cpp
System.bool SetPaperSize(
   System.String^ Sheet,
   System.int Size,
   System.double Height,
   System.double Width
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Sheet`: Sheet (layout) name of the input file or an empty string for all sheets
- `Size`: Size as defined in [swDwgPaperSizes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html)
- `Height`: If Size is swDwgPapersUserDefined, then the height of the paper in meters
- `Width`: If Size is swDwgPapersUserDefined, then the width of the paper in meters

### Return Value

True if paper size is set, false if not

## VBA Syntax

See [ImportDxfDwgData::SetPaperSize](ms-its:sldworksapivb6.chm::/sldworks~ImportDxfDwgData~SetPaperSize.html).

## Examples

[Import DXF File into Drawing (VBA)](Import_DXF_File_to_Drawing_Example_VB.htm)
[Insert and Position DXF/DWG File in Drawing (VBA)](Insert_and_Position_DXF_File_in_Drawing_Example_VB.htm)
[Insert and Position DXF/DWG File in Drawing (VB.NET)](Insert_and_Position_DXF_File_in_Drawing_Example_VBNET.htm)
[Insert and Position DXF/DWG File in Drawing (C#)](Insert_and_Position_DXF_File_in_Drawing_Example_CSharp.htm)

## Remarks

This method only supports importing to a drawing; it does not support importing to a part sketch.

## See Also

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.html)
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.html)
[IImportDxfDwgData::GetPaperSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetPaperSize.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
