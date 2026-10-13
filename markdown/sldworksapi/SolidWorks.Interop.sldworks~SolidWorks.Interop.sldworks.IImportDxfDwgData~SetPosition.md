---
title: "SetPosition Method (IImportDxfDwgData)"
project: "SOLIDWORKS API Help"
interface: "IImportDxfDwgData"
member: "SetPosition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetPosition.html"
---

# SetPosition Method (IImportDxfDwgData)

Sets the position of the entities created in the drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPosition( _
   ByVal Sheet As System.String, _
   ByVal Positioning As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim Positioning As System.Integer
Dim X As System.Double
Dim Y As System.Double
Dim value As System.Boolean

value = instance.SetPosition(Sheet, Positioning, X, Y)
```

### C#

```csharp
System.bool SetPosition(
   System.string Sheet,
   System.int Positioning,
   System.double X,
   System.double Y
)
```

### C++/CLI

```cpp
System.bool SetPosition(
   System.String^ Sheet,
   System.int Positioning,
   System.double X,
   System.double Y
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Sheet`: Sheet (layout) name of the input file or an empty string for all sheets
- `Positioning`: Position as defined in [swDwgImportEntitiesPositioning_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgImportEntitiesPositioning_e.html)
- `X`: X coordinate of the origin of the imported drawing
- `Y`: Y coordinate of the origin of the imported drawing

### Return Value

True if the position is set, false if not

## VBA Syntax

See [ImportDxfDwgData::SetPosition](ms-its:sldworksapivb6.chm::/sldworks~ImportDxfDwgData~SetPosition.html).

## Examples

[Insert and Position DXF/DWG File in Drawing (C#)](Insert_and_Position_DXF_File_in_Drawing_Example_CSharp.htm)
[Insert and Position DXF/DWG File in Drawing (VB.NET)](Insert_and_Position_DXF_File_in_Drawing_Example_VBNET.htm)
[Insert and Position DXF/DWG File in Drawing (VBA)](Insert_and_Position_DXF_File_in_Drawing_Example_VB.htm)

## Remarks

This method only supports importing to a drawing; it does not support importing to a part sketch.

## See Also

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.html)
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.html)
[IImportDxfDwgData::GetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetPosition.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
