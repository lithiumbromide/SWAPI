---
title: "SheetName Property (IImportDxfDwgData)"
project: "SOLIDWORKS API Help"
interface: "IImportDxfDwgData"
member: "SheetName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SheetName.html"
---

# SheetName Property (IImportDxfDwgData)

Gets or sets the name of the sheet for the drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Property SheetName( _
   ByVal Sheet As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim value As System.String

instance.SheetName(Sheet) = value

value = instance.SheetName(Sheet)
```

### C#

```csharp
System.string SheetName(
   System.string Sheet
) {get; set;}
```

### C++/CLI

```cpp
property System.String^ SheetName {
   System.String^ get(System.String^ Sheet);
   void set (System.String^ Sheet, System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Sheet`: Sheet (layout) name of the input file or an empty string for all sheets

### Property Value

Name of sheet

## VBA Syntax

See [ImportDxfDwgData::SheetName](ms-its:sldworksapivb6.chm::/sldworks~ImportDxfDwgData~SheetName.html).

## Examples

[Import DXF File into Drawing (VBA)](Import_DXF_File_to_Drawing_Example_VB.htm)

## Remarks

This method only supports importing to a drawing; it does not support importing to a part sketch.

## See Also

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.html)
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
