---
title: "GuideEdges Property (ISurfaceFlattenFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceFlattenFeatureData"
member: "GuideEdges"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~GuideEdges.html"
---

# GuideEdges Property (ISurfaceFlattenFeatureData)

Gets or sets the edges to guide the shape and length of the flattened surface.

## Syntax

### Visual Basic (Declaration)

```vb
Property GuideEdges As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceFlattenFeatureData
Dim value As System.Object

instance.GuideEdges = value

value = instance.GuideEdges
```

### C#

```csharp
System.object GuideEdges {get; set;}
```

### C++/CLI

```cpp
property System.Object^ GuideEdges {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of the [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html) to control the shape and length of the flattened surface

## VBA Syntax

See [SurfaceFlattenFeatureData::GuideEdges](ms-its:sldworksapivb6.chm::/sldworks~SurfaceFlattenFeatureData~GuideEdges.html).

## See Also

[ISurfaceFlattenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData.html)
[ISurfaceFlattenFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
