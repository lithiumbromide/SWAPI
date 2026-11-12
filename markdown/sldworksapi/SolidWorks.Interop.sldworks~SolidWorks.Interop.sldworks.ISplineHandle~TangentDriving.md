---
title: "TangentDriving Property (ISplineHandle)"
project: "SOLIDWORKS API Help"
interface: "ISplineHandle"
member: "TangentDriving"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentDriving.html"
---

# TangentDriving Property (ISplineHandle)

Enables or disables spline control using tangent magnitude, [tangent radial direction](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineHandle~TangentRadialDirection.html), and [tangent polar direction](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineHandle~TangentPolarDirection.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property TangentDriving As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISplineHandle
Dim value As System.Boolean

instance.TangentDriving = value

value = instance.TangentDriving
```

### C#

```csharp
System.bool TangentDriving {get; set;}
```

### C++/CLI

```cpp
property System.bool TangentDriving {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enable spline control using tangent magnitude and tangent radial, false to not

## VBA Syntax

See [SplineHandle::TangentDriving](ms-its:sldworksapivb6.chm::/sldworks~SplineHandle~TangentDriving.html).

## Examples

See the [ISplineHandle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.html) examples.

## See Also

[ISplineHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.html)
[ISplineHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle_members.html)
[ISplineHandle::TangentMagnitude Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentMagnitude.html)
[ISplineHandle::TangentPolarDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentPolarDirection.html)
[ISplineHandle::TangentRadialDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentRadialDirection.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
