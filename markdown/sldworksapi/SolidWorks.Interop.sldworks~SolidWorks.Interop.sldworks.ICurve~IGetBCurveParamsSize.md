---
title: "IGetBCurveParamsSize Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "IGetBCurveParamsSize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParamsSize.html"
---

# IGetBCurveParamsSize Method (ICurve)

Obsolete. Superseded by [ICurve::IGetBCuvreParamsSize2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IGetBCurveParamsSize2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBCurveParamsSize( _
   ByVal WantCubicIn As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim WantCubicIn As System.Boolean
Dim value As System.Integer

value = instance.IGetBCurveParamsSize(WantCubicIn)
```

### C#

```csharp
System.int IGetBCurveParamsSize(
   System.bool WantCubicIn
)
```

### C++/CLI

```cpp
System.int IGetBCurveParamsSize(
   System.bool WantCubicIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WantCubicIn`:

## VBA Syntax

See [Curve::IGetBCurveParamsSize](ms-its:sldworksapivb6.chm::/sldworks~Curve~IGetBCurveParamsSize.html).

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
