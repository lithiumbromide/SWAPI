---
title: "RadiusOfCurvature Property (ISplineHandle)"
project: "SOLIDWORKS API Help"
interface: "ISplineHandle"
member: "RadiusOfCurvature"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~RadiusOfCurvature.html"
---

# RadiusOfCurvature Property (ISplineHandle)

Gets or sets the radius of curvature at any spline point.

## Syntax

### Visual Basic (Declaration)

```vb
Property RadiusOfCurvature As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISplineHandle
Dim value As System.Double

instance.RadiusOfCurvature = value

value = instance.RadiusOfCurvature
```

### C#

```csharp
System.double RadiusOfCurvature {get; set;}
```

### C++/CLI

```cpp
property System.double RadiusOfCurvature {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Radius of curvature

## VBA Syntax

See [SplineHandle::RadiusOfCurvature](ms-its:sldworksapivb6.chm::/sldworks~SplineHandle~RadiusOfCurvature.html).

## Examples

See the [ISplineHandle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.html) examples.

## Remarks

Curvature control must be enabled for this property to have an effect. Use [ISplineHandle::CurvatureControlled](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineHandle~CurvatureControlled.html) to see if curvature control is enabled or to set curvature control for this spline handle.

## See Also

[ISplineHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.html)
[ISplineHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle_members.html)
[ISplineHandle::Curvature Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~Curvature.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
