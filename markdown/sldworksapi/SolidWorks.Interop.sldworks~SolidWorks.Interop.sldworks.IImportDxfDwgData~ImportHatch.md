---
title: "ImportHatch Property (IImportDxfDwgData)"
project: "SOLIDWORKS API Help"
interface: "IImportDxfDwgData"
member: "ImportHatch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~ImportHatch.html"
---

# ImportHatch Property (IImportDxfDwgData)

Gets or sets whether to import hatch into this part sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Property ImportHatch( _
   ByVal Sheet As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim value As System.Boolean

instance.ImportHatch(Sheet) = value

value = instance.ImportHatch(Sheet)
```

### C#

```csharp
System.bool ImportHatch(
   System.string Sheet
) {get; set;}
```

### C++/CLI

```cpp
property System.bool ImportHatch {
   System.bool get(System.String^ Sheet);
   void set (System.String^ Sheet, System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Sheet`: Sheet (layout) name of the input file or an empty string for all sheets

### Property Value

True to import hatch, false to not

## VBA Syntax

See [ImportDxfDwgData::ImportHatch](ms-its:sldworksapivb6.chm::/sldworks~ImportDxfDwgData~ImportHatch.html).

## Examples

[Import DXF File into Part Sketch (VBA)](Import_DXF_File_into_Part_Sketch_Example_VB.htm)

## Remarks

This property only supports importing to a part sketch; it does not support importing to a drawing.

By default, hatch will be imported.

## See Also

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.html)
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
