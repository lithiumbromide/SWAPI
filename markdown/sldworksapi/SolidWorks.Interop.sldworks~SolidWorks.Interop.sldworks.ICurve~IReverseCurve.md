---
title: "IReverseCurve Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "IReverseCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IReverseCurve.html"
---

# IReverseCurve Method (ICurve)

Gets the reversed copy of this curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function IReverseCurve() As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim value As Curve

value = instance.IReverseCurve()
```

### C#

```csharp
Curve IReverseCurve()
```

### C++/CLI

```cpp
Curve^ IReverseCurve();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the reversed [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Curve::IReverseCurve](ms-its:sldworksapivb6.chm::/sldworks~Curve~IReverseCurve.html).

## Remarks

If this is a trimmed curve, then the underlying curve is reversed and a new trimmed curve is made from the reversed curve. This method returns the new trimmed curve.

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::ReverseCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ReverseCurve.html)
[ICurve::IsTrimmedCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsTrimmedCurve.html)
