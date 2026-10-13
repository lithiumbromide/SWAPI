---
title: "FixPointVertex Property (ISurfaceFlattenFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceFlattenFeatureData"
member: "FixPointVertex"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~FixPointVertex.html"
---

# FixPointVertex Property (ISurfaceFlattenFeatureData)

Gets or sets the anchor point for flattening the selected faces or surfaces.

## Syntax

### Visual Basic (Declaration)

```vb
Property FixPointVertex As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceFlattenFeatureData
Dim value As System.Object

instance.FixPointVertex = value

value = instance.FixPointVertex
```

### C#

```csharp
System.object FixPointVertex {get; set;}
```

### C++/CLI

```cpp
property System.Object^ FixPointVertex {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Anchor point ([vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html) or a point on an [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)) for flattening

## VBA Syntax

See [SurfaceFlattenFeatureData::FixPointVertex](ms-its:sldworksapivb6.chm::/sldworks~SurfaceFlattenFeatureData~FixPointVertex.html).

## See Also

[ISurfaceFlattenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData.html)
[ISurfaceFlattenFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
