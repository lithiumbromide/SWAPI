---
title: "ImportDimensions Property (IImportDxfDwgData)"
project: "SOLIDWORKS API Help"
interface: "IImportDxfDwgData"
member: "ImportDimensions"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~ImportDimensions.html"
---

# ImportDimensions Property (IImportDxfDwgData)

Gets or sets whether to import dimension into the part sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Property ImportDimensions( _
   ByVal Sheet As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim value As System.Boolean

instance.ImportDimensions(Sheet) = value

value = instance.ImportDimensions(Sheet)
```

### C#

```csharp
System.bool ImportDimensions(
   System.string Sheet
) {get; set;}
```

### C++/CLI

```cpp
property System.bool ImportDimensions {
   System.bool get(System.String^ Sheet);
   void set (System.String^ Sheet, System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Sheet`: Sheet (layout) name of the input file or an empty string for all sheets

### Property Value

True to import dimension, false to not

## VBA Syntax

See [ImportDxfDwgData::ImportDimensions](ms-its:sldworksapivb6.chm::/sldworks~ImportDxfDwgData~ImportDimensions.html).

## Examples

[Import DXF File into Part Sketch (VBA)](Import_DXF_File_into_Part_Sketch_Example_VB.htm)

## Remarks

This property only supports importing to a part sketch; it does not support importing to a drawing.

By default, dimensions are not imported.

## See Also

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.html)
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
