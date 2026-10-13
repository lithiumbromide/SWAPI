---
title: "IgnorePolylineWidth Property (IImportDxfDwgData)"
project: "SOLIDWORKS API Help"
interface: "IImportDxfDwgData"
member: "IgnorePolylineWidth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~IgnorePolylineWidth.html"
---

# IgnorePolylineWidth Property (IImportDxfDwgData)

Gets or sets whether to convert width polylines to solid fill hatches when importing to the part sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Property IgnorePolylineWidth As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImportDxfDwgData
Dim value As System.Boolean

instance.IgnorePolylineWidth = value

value = instance.IgnorePolylineWidth
```

### C#

```csharp
System.bool IgnorePolylineWidth {get; set;}
```

### C++/CLI

```cpp
property System.bool IgnorePolylineWidth {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to convert width polylines to solid fill hatches, false to not

## VBA Syntax

See [ImportDxfDwgData::IgnorePolylineWidth](ms-its:sldworksapivb6.chm::/sldworks~ImportDxfDwgData~IgnorePolylineWidth.html).

## See Also

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.html)
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
