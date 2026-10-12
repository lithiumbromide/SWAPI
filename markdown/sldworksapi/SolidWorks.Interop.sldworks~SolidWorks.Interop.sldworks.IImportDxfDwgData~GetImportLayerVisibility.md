---
title: "GetImportLayerVisibility Method (IImportDxfDwgData)"
project: "SOLIDWORKS API Help"
interface: "IImportDxfDwgData"
member: "GetImportLayerVisibility"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetImportLayerVisibility.html"
---

# GetImportLayerVisibility Method (IImportDxfDwgData)

Gets whether the specified layer is imported hidden or visible.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetImportLayerVisibility( _
   ByVal Layer As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IImportDxfDwgData
Dim Layer As System.String
Dim value As System.Integer

value = instance.GetImportLayerVisibility(Layer)
```

### C#

```csharp
System.int GetImportLayerVisibility(
   System.string Layer
)
```

### C++/CLI

```cpp
System.int GetImportLayerVisibility(
   System.String^ Layer
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Layer`: Name of the layer

### Return Value

Visibility state as defined in [swImportDxfDwg_LayerVisibility_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swImportDxfDwg_LayerVisibility_e.html)

## VBA Syntax

See [ImportDxfDwgData::GetImportLayerVisibility](ms-its:sldworksapivb6.chm::/sldworks~ImportDxfDwgData~GetImportLayerVisibility.html).

## Remarks

This method only supports importing to a drawing; it does not support importing to a part sketch.

## See Also

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.html)
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.html)
[IImportDxfDwgData::GetImportLayerToSheetFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetImportLayerToSheetFormat.html)
[IImportDxfDwgData::SetImportLayerToSheetFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetImportLayerToSheetFormat.html)
[IImportDxfDwgData::SetImportLayerVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetImportLayerVisibility.html)
[IImportDxfDwgData::ImportMethod Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~ImportMethod.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
