---
title: "SetImportLayerVisibility Method (IImportDxfDwgData)"
project: "SOLIDWORKS API Help"
interface: "IImportDxfDwgData"
member: "SetImportLayerVisibility"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetImportLayerVisibility.html"
---

# SetImportLayerVisibility Method (IImportDxfDwgData)

Sets whether the specified layers are imported hidden or visible.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetImportLayerVisibility( _
   ByVal Layers As System.Object, _
   ByVal Visibility As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImportDxfDwgData
Dim Layers As System.Object
Dim Visibility As System.Integer
Dim value As System.Boolean

value = instance.SetImportLayerVisibility(Layers, Visibility)
```

### C#

```csharp
System.bool SetImportLayerVisibility(
   System.object Layers,
   System.int Visibility
)
```

### C++/CLI

```cpp
System.bool SetImportLayerVisibility(
   System.Object^ Layers,
   System.int Visibility
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Layers`: Array of strings of the names of the layers (see **Remarks**)
- `Visibility`: Visibility of the layers as defined in [swImportDxfDwg_LayerVisibility_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swImportDxfDwg_LayerVisibility_e.html)

### Return Value

True if setting the visibility of these layers is successful, false if not

## VBA Syntax

See [ImportDxfDwgData::SetImportLayerVisibility](ms-its:sldworksapivb6.chm::/sldworks~ImportDxfDwgData~SetImportLayerVisibility.html).

## Remarks

This method only supports importing to a drawing; it does not support importing to a part sketch.

The Layers argument can contain either a string or an array of strings, where the strings are the layer names with which to work. You can also specify the argument as empty, which indicates all layers. If this method is not used, the default behavior is to import all layers with the same visibility as they have in the DXF/DWG file.

The layer visibility is the same for all sheets that are imported; you cannot specify the layer visibility on a sheet-by-sheet basis.

Hidden layers are always imported to the drawing sheet.

You should first specify the behavior that applies to all layers, using an empty VARIANT, because this overrides any information you have previously entered for specific layers. Then, you should use this method with layer names in the VARIANT, to override that default behavior on a layer-by-layer basis.

##### Visual Basic for Applications (VBA) Example

To import all layers with the same visibility as in the DXF/DWG file (this is the default behavior):

```vb
boolstatus = ImportDxfDwgData.SetImportLayerVisibility (emptyVariant, swImportDxfDwg_LayerMaintain)
```

To import layer "A" hidden and the remaining layers visible:

```vb
boolstatus = ImportDxfDwgData.SetImportLayerVisibility (emptyVariant, swImportDxfDwg_LayerVisible)
layerName = "A"
layerVariant = layerName

boolstatus = ImportDxfDwgData.SetImportLayerVisibility ((layerVariant), swImportDxfDwg_LayerHidden)
```

## See Also

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.html)
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.html)
[IImportDxfDwgData::GetImportLayerToSheetFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetImportLayerToSheetFormat.html)
[IImportDxfDwgData::GetImportLayerVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetImportLayerVisibility.html)
[IImportDxfDwgData::SetImportLayerToSheetFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetImportLayerToSheetFormat.html)
[IImportDxfDwgData::ImportMethod Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~ImportMethod.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
