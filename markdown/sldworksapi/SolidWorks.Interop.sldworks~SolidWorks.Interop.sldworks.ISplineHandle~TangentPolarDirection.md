---
title: "TangentPolarDirection Property (ISplineHandle)"
project: "SOLIDWORKS API Help"
interface: "ISplineHandle"
member: "TangentPolarDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentPolarDirection.html"
---

# TangentPolarDirection Property (ISplineHandle)

Gets or sets the tangent polar direction, which is the elevation angle of the tangent vector to a plane placed at a point perpendicular to a spline point.

## Syntax

### Visual Basic (Declaration)

```vb
Property TangentPolarDirection As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISplineHandle
Dim value As System.Double

instance.TangentPolarDirection = value

value = instance.TangentPolarDirection
```

### C#

```csharp
System.double TangentPolarDirection {get; set;}
```

### C++/CLI

```cpp
property System.double TangentPolarDirection {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Tangent polar direction

## VBA Syntax

See [SplineHandle::TangentPolarDirection](ms-its:sldworksapivb6.chm::/sldworks~SplineHandle~TangentPolarDirection.html).

## See Also

[ISplineHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.html)
[ISplineHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle_members.html)
[ISplineHandle::TangentDriving Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentDriving.html)
[ISplineHandle::TangentMagnitude Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentMagnitude.html)
[ISplineHandle::TangentRadialDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentRadialDirection.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
