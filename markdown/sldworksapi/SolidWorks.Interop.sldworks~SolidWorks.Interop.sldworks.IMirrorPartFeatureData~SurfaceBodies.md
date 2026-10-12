---
title: "SurfaceBodies Property (IMirrorPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPartFeatureData"
member: "SurfaceBodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~SurfaceBodies.html"
---

# SurfaceBodies Property (IMirrorPartFeatureData)

Gets or sets whether to import surface bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Property SurfaceBodies As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPartFeatureData
Dim value As System.Boolean

instance.SurfaceBodies = value

value = instance.SurfaceBodies
```

### C#

```csharp
System.bool SurfaceBodies {get; set;}
```

### C++/CLI

```cpp
property System.bool SurfaceBodies {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import surface bodies, false to not

## VBA Syntax

See [MirrorPartFeatureData::SurfaceBodies](ms-its:sldworksapivb6.chm::/sldworks~MirrorPartFeatureData~SurfaceBodies.html).

## Examples

See the [IMirrorPartFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMirrorPartFeatureData.html) examples.

## See Also

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html)
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
