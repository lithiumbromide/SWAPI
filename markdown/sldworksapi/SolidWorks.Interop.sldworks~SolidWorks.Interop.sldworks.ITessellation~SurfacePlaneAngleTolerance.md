---
title: "SurfacePlaneAngleTolerance Property (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "SurfacePlaneAngleTolerance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~SurfacePlaneAngleTolerance.html"
---

# SurfacePlaneAngleTolerance Property (ITessellation)

Gets or sets the surface plane angle tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Property SurfacePlaneAngleTolerance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim value As System.Double

instance.SurfacePlaneAngleTolerance = value

value = instance.SurfacePlaneAngleTolerance
```

### C#

```csharp
System.double SurfacePlaneAngleTolerance {get; set;}
```

### C++/CLI

```cpp
property System.double SurfacePlaneAngleTolerance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Surface plane angle tolerance

## VBA Syntax

See [Tessellation::SurfacePlaneAngleTolerance](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~SurfacePlaneAngleTolerance.html).

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellation::SurfacePlaneTolerance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~SurfacePlaneTolerance.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
