---
title: "JoinCurves Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "JoinCurves"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~JoinCurves.html"
---

# JoinCurves Method (ICurve)

Joins the specified curves.

## Syntax

### Visual Basic (Declaration)

```vb
Function JoinCurves( _
   ByVal Curves As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim Curves As System.Object
Dim value As System.Object

value = instance.JoinCurves(Curves)
```

### C#

```csharp
System.object JoinCurves(
   System.object Curves
)
```

### C++/CLI

```cpp
System.Object^ JoinCurves(
   System.Object^ Curves
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Curves`: Curves to join

### Return Value

Newly created joined curve

## VBA Syntax

See [Curve::JoinCurves](ms-its:sldworksapivb6.chm::/sldworks~Curve~JoinCurves.html).

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::IJoinCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IJoinCurves.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
