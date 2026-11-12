---
title: "ImportMethod Property (IImportDxfDwgData)"
project: "SOLIDWORKS API Help"
interface: "IImportDxfDwgData"
member: "ImportMethod"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~ImportMethod.html"
---

# ImportMethod Property (IImportDxfDwgData)

Gets or sets whether to import this sheet (layout).

## Syntax

### Visual Basic (Declaration)

```vb
Property ImportMethod( _
   ByVal Sheet As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim value As System.Integer

instance.ImportMethod(Sheet) = value

value = instance.ImportMethod(Sheet)
```

### C#

```csharp
System.int ImportMethod(
   System.string Sheet
) {get; set;}
```

### C++/CLI

```cpp
property System.int ImportMethod {
   System.int get(System.String^ Sheet);
   void set (System.String^ Sheet, System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Sheet`: Sheet (layout) name of the input file or an empty string for all sheets (see **Remarks**)

### Property Value

Import method as defined in [swImportDxfDwg_ImportMethod_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swImportDxfDwg_ImportMethod_e.html)

## VBA Syntax

See [ImportDxfDwgData::ImportMethod](ms-its:sldworksapivb6.chm::/sldworks~ImportDxfDwgData~ImportMethod.html).

## Examples

[Import DXF File into Part Sketch (VBA)](Import_DXF_File_into_Part_Sketch_Example_VB.htm)
[Insert DXF/DWG File and Add Dimensions (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)
[Insert DXF/DWG File and Add Dimensions (VB.NET)](Insert_DXF_File_and_Add_Dimensions_Example_VBNET.htm)
[Insert DXF/DWG File and Add Dimensions (C#)](Insert_DXF_File_and_Add_Dimensions_Example_CSharp.htm)
[Insert and Position DXF/DWG File in Drawing (VBA)](Insert_and_Position_DXF_File_in_Drawing_Example_VB.htm)
[Insert and Position DXF/DWG File in Drawing (VB.NET)](Insert_and_Position_DXF_File_in_Drawing_Example_VBNET.htm)
[Insert and Position DXF/DWG File in Drawing (C#)](Insert_and_Position_DXF_File_in_Drawing_Example_CSharp.htm)

## Remarks

By default, all sheets are imported into a new drawing.

| If you want to import... | Then set... |
| --- | --- |
| All sheets except for a specific one into a new drawing | ImportDxfDwgData.ImportMethod("< sheet to exclude >") = swImportDxfDwg_DoNotImportSheet |
| Only a single sheet into a sketch in a new part | ImportDxfDwgData.ImportMethod("") = swImportDxfDwg_DoNotImportSheet to make the default not to import sheets. Then set: ImportDxfDwgData.ImportMethod("< sheet to import >") = swImportDxfDwg_ImportToPartSketch to import only this sheet. |

## See Also

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.html)
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.html)
[IImportDxfDwgData::GetImportLayerToSheetFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~ImportMethod.html)
[IImportDxfDwgData::GetImportLayerVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetImportLayerVisibility.html)
[IImportDxfDwgData::SetImportLayerToSheetFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetImportLayerToSheetFormat.html)
[IImportDxfDwgData::SetImportLayerVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetImportLayerVisibility.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
