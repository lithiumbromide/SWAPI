---
title: "ILineParams Property (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "ILineParams"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ILineParams.html"
---

# ILineParams Property (ICurve)

Gets the parameters of a curve that is a line.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ILineParams As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim value As System.Double

value = instance.ILineParams
```

### C#

```csharp
System.double ILineParams {get;}
```

### C++/CLI

```cpp
property System.double ILineParams {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to an array of doubles (see **Remarks**)

## VBA Syntax

See [Curve::ILineParams](ms-its:sldworksapivb6.chm::/sldworks~Curve~ILineParams.html).

## Remarks

The return value is an array of 6 double values:

[ rootPoint.x, rootPoint.y, rootPoint.z, direction.x, direction.y, direction.z ]

SOLIDWORKS stores rootPoint in meters.

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::LineParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~LineParams.html)
[ICurve::IsLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsLine.html)
[ICurve::Identity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.html)
