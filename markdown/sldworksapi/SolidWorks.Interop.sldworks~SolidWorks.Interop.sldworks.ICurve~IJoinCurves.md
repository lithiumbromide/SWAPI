---
title: "IJoinCurves Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "IJoinCurves"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IJoinCurves.html"
---

# IJoinCurves Method (ICurve)

Joins the specified curves.

## Syntax

### Visual Basic (Declaration)

```vb
Function IJoinCurves( _
   ByVal NCurves As System.Integer, _
   ByRef Curves As Curve _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim NCurves As System.Integer
Dim Curves As Curve
Dim value As Curve

value = instance.IJoinCurves(NCurves, Curves)
```

### C#

```csharp
Curve IJoinCurves(
   System.int NCurves,
   ref Curve Curves
)
```

### C++/CLI

```cpp
Curve^ IJoinCurves(
   System.int NCurves,
   Curve^% Curves
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NCurves`: Number of curves to join
- `Curves`: - in-process, unmanaged C++: Pointer to an array of [curves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) to join

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

Newly created joined [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::JoinCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~JoinCurves.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
