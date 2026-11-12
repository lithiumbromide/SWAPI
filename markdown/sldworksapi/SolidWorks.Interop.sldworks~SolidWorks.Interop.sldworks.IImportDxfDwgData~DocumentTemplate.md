---
title: "DocumentTemplate Property (IImportDxfDwgData)"
project: "SOLIDWORKS API Help"
interface: "IImportDxfDwgData"
member: "DocumentTemplate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~DocumentTemplate.html"
---

# DocumentTemplate Property (IImportDxfDwgData)

Gets or sets the filename of the document template.

## Syntax

### Visual Basic (Declaration)

```vb
Property DocumentTemplate As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IImportDxfDwgData
Dim value As System.String

instance.DocumentTemplate = value

value = instance.DocumentTemplate
```

### C#

```csharp
System.string DocumentTemplate {get; set;}
```

### C++/CLI

```cpp
property System.String^ DocumentTemplate {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Filename of document template

## VBA Syntax

See [ImportDxfDwgData::DocumentTemplate](ms-its:sldworksapivb6.chm::/sldworks~ImportDxfDwgData~DocumentTemplate.html).

## Remarks

This method only supports importing to a drawing; it does not support importing to a part sketch.

## See Also

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.html)
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
