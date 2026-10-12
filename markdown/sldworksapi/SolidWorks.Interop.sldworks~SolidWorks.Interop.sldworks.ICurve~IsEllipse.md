---
title: "IsEllipse Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "IsEllipse"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsEllipse.html"
---

# IsEllipse Method (ICurve)

Gets whether the curve is an ellipse.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsEllipse() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim value As System.Boolean

value = instance.IsEllipse()
```

### C#

```csharp
System.bool IsEllipse()
```

### C++/CLI

```cpp
System.bool IsEllipse();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if curve is an ellipse, false if other curve type

## VBA Syntax

See [Curve::IsEllipse](ms-its:sldworksapivb6.chm::/sldworks~Curve~IsEllipse.html).

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::GetEllipseParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetEllipseParams.html)
[ICurve::IGetEllipseParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetEllipseParams.html)
[ICurve::IsBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsBcurve.html)
[ICurve::Identity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.html)

## Availability

SOLIDWORKS 98Plus, datecode 1999042
