---
title: "GetImportLayerToSheetFormat Method (IImportDxfDwgData)"
project: "SOLIDWORKS API Help"
interface: "IImportDxfDwgData"
member: "GetImportLayerToSheetFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetImportLayerToSheetFormat.html"
---

# GetImportLayerToSheetFormat Method (IImportDxfDwgData)

Gets whether the specified visible layer is imported to the drawing sheet or sheet format.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetImportLayerToSheetFormat( _
   ByVal Layer As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImportDxfDwgData
Dim Layer As System.String
Dim value As System.Boolean

value = instance.GetImportLayerToSheetFormat(Layer)
```

### C#

```csharp
System.bool GetImportLayerToSheetFormat(
   System.string Layer
)
```

### C++/CLI

```cpp
System.bool GetImportLayerToSheetFormat(
   System.String^ Layer
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Layer`: Name of the layer

### Return Value

True to import the specified visible layer to the sheet format, false to import it to the drawing sheet

## VBA Syntax

See [ImportDxfDwgData::GetImportLayerToSheetFormat](ms-its:sldworksapivb6.chm::/sldworks~ImportDxfDwgData~GetImportLayerToSheetFormat.html).

## Remarks

This method only supports importing to a drawing; it does not support importing to a part sketch.

## See Also

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.html)
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.html)
[IImportDxfDwgData::GetImportLayerVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetImportLayerVisibility.html)
[IImportDxfDwgData::SetImportLayerToSheetFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetImportLayerToSheetFormat.html)
[IImportDxfDwgData::SetImportLayerVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetImportLayerVisibility.html)
[IImportDxfDwgData::ImportMethod Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~ImportMethod.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
