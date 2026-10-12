---
title: "ApplyTransform Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "ApplyTransform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ApplyTransform.html"
---

# ApplyTransform Method (ICurve)

Applies the transform to a curve.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ApplyTransform( _
   ByVal Xform As MathTransform _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim Xform As MathTransform

instance.ApplyTransform(Xform)
```

### C#

```csharp
void ApplyTransform(
   MathTransform Xform
)
```

### C++/CLI

```cpp
void ApplyTransform(
   MathTransform^ Xform
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Xform`: Pointer to [IMathTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) object

## VBA Syntax

See [Curve::ApplyTransform](ms-its:sldworksapivb6.chm::/sldworks~Curve~ApplyTransform.html).

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
