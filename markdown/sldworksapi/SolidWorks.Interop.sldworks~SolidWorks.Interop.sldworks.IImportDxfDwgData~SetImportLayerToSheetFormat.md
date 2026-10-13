---
title: "SetImportLayerToSheetFormat Method (IImportDxfDwgData)"
project: "SOLIDWORKS API Help"
interface: "IImportDxfDwgData"
member: "SetImportLayerToSheetFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetImportLayerToSheetFormat.html"
---

# SetImportLayerToSheetFormat Method (IImportDxfDwgData)

Sets whether the specified visible layers are imported to the sheet format or drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetImportLayerToSheetFormat( _
   ByVal Layers As System.Object, _
   ByVal SheetFormat As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImportDxfDwgData
Dim Layers As System.Object
Dim SheetFormat As System.Boolean
Dim value As System.Boolean

value = instance.SetImportLayerToSheetFormat(Layers, SheetFormat)
```

### C#

```csharp
System.bool SetImportLayerToSheetFormat(
   System.object Layers,
   System.bool SheetFormat
)
```

### C++/CLI

```cpp
System.bool SetImportLayerToSheetFormat(
   System.Object^ Layers,
   System.bool SheetFormat
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Layers`: Array of strings of the names of the layers (see **Remarks**)
- `SheetFormat`: True to import the specified visible layers to the sheet format, false to import them to the drawing sheet

### Return Value

True of importing the specified visible layers was successful, false if not

## VBA Syntax

See [ImportDxfDwgData::SetImportLayerToSheetFormat](ms-its:sldworksapivb6.chm::/sldworks~ImportDxfDwgData~SetImportLayerToSheetFormat.html).

## Remarks

This method only supports importing to a drawing; it does not support importing to a part sketch.

The Layers argument can contain either a string or an array of strings, where the strings are the layer names with which to work. You can also specify the argument as empty, which indicates all layers. If this method is not used, the default behavior is to import all layers to the drawing sheet.

The import to sheet or sheet format Boolean is the same for all sheets that are imported; you cannot specify it on a sheet-by-sheet basis.

##### Visual Basic for Applications (VBA) Example

To import all layers on all sheets to drawings sheets in SOLIDWORKS (this is the default behavior):

```vb
boolstatus = ImportDxfDwgData.SetImportLayerToSheetFormat (emptyVariant, false)
```

To import layers "A" and "B" to the drawing sheet and the remaining layers to the sheet format:

```vb
boolstatus = ImportDxfDwgData.SetImportLayerToSheetFormat (emptyVariant, True)
layerName(0) = "A"
layerName(1) = "B"
layerVariant = layerName
boolstatus = ImportDxfDwgData.SetImportLayerToSheetFormat ((layerVariant), false)
```

## See Also

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.html)
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.html)
[IImportDxfDwgData::GetImportLayerToSheetFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetImportLayerToSheetFormat.html)
[IImportDxfDwgData::GetImportLayerVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetImportLayerVisibility.html)
[IImportDxfDwgData::SetImportLayerVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetImportLayerVisibility.html)
[IImportDxfDwgData::ImportMethod Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~ImportMethod.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
