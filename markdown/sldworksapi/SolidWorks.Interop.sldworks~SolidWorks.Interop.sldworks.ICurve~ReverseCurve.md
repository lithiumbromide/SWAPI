---
title: "ReverseCurve Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "ReverseCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ReverseCurve.html"
---

# ReverseCurve Method (ICurve)

Gets the reversed copy of this curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReverseCurve() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim value As System.Object

value = instance.ReverseCurve()
```

### C#

```csharp
System.object ReverseCurve()
```

### C++/CLI

```cpp
System.Object^ ReverseCurve();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Reversed curve

## VBA Syntax

See [Curve::ReverseCurve](ms-its:sldworksapivb6.chm::/sldworks~Curve~ReverseCurve.html).

## Remarks

If this is a trimmed curve, then the underlying curve is reversed and a new trimmed curve is made from the reversed curve. This method returns the new trimmed curve.

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::IReverseCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IReverseCurve.html)
[ICurve::IsTrimmedCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsTrimmedCurve.html)
