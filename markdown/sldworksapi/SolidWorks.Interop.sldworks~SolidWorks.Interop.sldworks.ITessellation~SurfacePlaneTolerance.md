---
title: "SurfacePlaneTolerance Property (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "SurfacePlaneTolerance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~SurfacePlaneTolerance.html"
---

# SurfacePlaneTolerance Property (ITessellation)

Gets or sets the surface plane tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Property SurfacePlaneTolerance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim value As System.Double

instance.SurfacePlaneTolerance = value

value = instance.SurfacePlaneTolerance
```

### C#

```csharp
System.double SurfacePlaneTolerance {get; set;}
```

### C++/CLI

```cpp
property System.double SurfacePlaneTolerance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Surface plane tolerance

## VBA Syntax

See [Tessellation::SurfacePlaneTolerance](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~SurfacePlaneTolerance.html).

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellate::SurfacePlaneAngleTolerance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~SurfacePlaneAngleTolerance.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
