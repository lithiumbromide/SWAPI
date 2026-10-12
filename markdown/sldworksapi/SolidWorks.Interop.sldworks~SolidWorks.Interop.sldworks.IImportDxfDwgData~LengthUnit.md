---
title: "LengthUnit Property (IImportDxfDwgData)"
project: "SOLIDWORKS API Help"
interface: "IImportDxfDwgData"
member: "LengthUnit"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~LengthUnit.html"
---

# LengthUnit Property (IImportDxfDwgData)

Gets or sets the length units for the drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Property LengthUnit( _
   ByVal Sheet As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim value As System.Integer

instance.LengthUnit(Sheet) = value

value = instance.LengthUnit(Sheet)
```

### C#

```csharp
System.int LengthUnit(
   System.string Sheet
) {get; set;}
```

### C++/CLI

```cpp
property System.int LengthUnit {
   System.int get(System.String^ Sheet);
   void set (System.String^ Sheet, System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Sheet`: Sheet (layout) name of the input file or an empty string for all sheets

### Property Value

Length as defined in [swLengthUnit_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLengthUnit_e.html)

## VBA Syntax

See [ImportDxfDwgData::LengthUnit](ms-its:sldworksapivb6.chm::/sldworks~ImportDxfDwgData~LengthUnit.html).

## Examples

[Import DXF File into Drawing (VBA)](Import_DXF_File_to_Drawing_Example_VB.htm)
[Insert DXF/DWG File and Add Dimensions (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)
[Insert DXF/DWG File and Add Dimensions (VB.NET)](Insert_DXF_File_and_Add_Dimensions_Example_VBNET.htm)
[Insert DXF/DWG File and Add Dimensions (C#)](Insert_DXF_File_and_Add_Dimensions_Example_CSharp.htm)
[Insert and Position DXF/DWG File in Drawing (C#)](Insert_and_Position_DXF_File_in_Drawing_Example_CSharp.htm)
[Insert and Position DXF/DWG File in Drawing (VB.NET)](Insert_and_Position_DXF_File_in_Drawing_Example_VBNET.htm)
[Insert and Position DXF/DWG File in Drawing (VBA)](Insert_and_Position_DXF_File_in_Drawing_Example_VB.htm)

## Remarks

By default, the length is determined from the header of the input DWG/DXF file.

## See Also

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.html)
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
