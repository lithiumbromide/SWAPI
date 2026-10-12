---
title: "SetSheetScale Method (IImportDxfDwgData)"
project: "SOLIDWORKS API Help"
interface: "IImportDxfDwgData"
member: "SetSheetScale"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetSheetScale.html"
---

# SetSheetScale Method (IImportDxfDwgData)

Sets the sheet scale for the drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSheetScale( _
   ByVal Sheet As System.String, _
   ByVal Numerator As System.Double, _
   ByVal Denominator As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim Numerator As System.Double
Dim Denominator As System.Double
Dim value As System.Boolean

value = instance.SetSheetScale(Sheet, Numerator, Denominator)
```

### C#

```csharp
System.bool SetSheetScale(
   System.string Sheet,
   System.double Numerator,
   System.double Denominator
)
```

### C++/CLI

```cpp
System.bool SetSheetScale(
   System.String^ Sheet,
   System.double Numerator,
   System.double Denominator
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Sheet`: Sheet (layout) name of the input file or an empty string for all sheets
- `Numerator`: Numerator of the scale
- `Denominator`: Denominator of the scale

### Return Value

True if the sheet scale is set, false if not

## VBA Syntax

See [ImportDxfDwgData::SetSheetScale](ms-its:sldworksapivb6.chm::/sldworks~ImportDxfDwgData~SetSheetScale.html).

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
[IImportDxfDwgData::GetSheetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetSheetScale.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
