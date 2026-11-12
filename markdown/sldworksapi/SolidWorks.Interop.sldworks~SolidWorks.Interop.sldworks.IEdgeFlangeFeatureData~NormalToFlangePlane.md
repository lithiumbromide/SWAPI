---
title: "NormalToFlangePlane Property (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "NormalToFlangePlane"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~NormalToFlangePlane.html"
---

# NormalToFlangePlane Property (IEdgeFlangeFeatureData)

Gets or sets whether the Up To Vertex is on a plane that is normal to the end face of this edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property NormalToFlangePlane As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim value As System.Boolean

instance.NormalToFlangePlane = value

value = instance.NormalToFlangePlane
```

### C#

```csharp
System.bool NormalToFlangePlane {get; set;}
```

### C++/CLI

```cpp
property System.bool NormalToFlangePlane {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the Up To Vertex is on a plane that is normal to the end face of the edge flange (default), false if the Up To Vertex passes through a plane that is parallel to the face of the base flange

## VBA Syntax

See [EdgeFlangeFeatureData::NormalToFlangePlane](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~NormalToFlangePlane.html).

## Remarks

This property is valid only if [IEdgeFlangeFeatureData::OffsetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~OffsetType.html) is set to [swFlangeOffsetTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFlangeOffsetTypes_e.html).swFlangeOffsetUpToVertex.

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
