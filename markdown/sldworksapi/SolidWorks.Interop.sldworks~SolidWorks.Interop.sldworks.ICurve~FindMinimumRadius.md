---
title: "FindMinimumRadius Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "FindMinimumRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~FindMinimumRadius.html"
---

# FindMinimumRadius Method (ICurve)

Finds the minimum radius of curvature of the selected curve and its position and u-v parameters.

## Syntax

### Visual Basic (Declaration)

```vb
Function FindMinimumRadius( _
   ByVal Bound As System.Object, _
   ByRef NumOfRadius As System.Integer, _
   ByRef Radius As System.Object, _
   ByRef Location As System.Object, _
   ByRef Parameter As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim Bound As System.Object
Dim NumOfRadius As System.Integer
Dim Radius As System.Object
Dim Location As System.Object
Dim Parameter As System.Object
Dim value As System.Boolean

value = instance.FindMinimumRadius(Bound, NumOfRadius, Radius, Location, Parameter)
```

### C#

```csharp
System.bool FindMinimumRadius(
   System.object Bound,
   out System.int NumOfRadius,
   out System.object Radius,
   out System.object Location,
   out System.object Parameter
)
```

### C++/CLI

```cpp
System.bool FindMinimumRadius(
   System.Object^ Bound,
   [Out] System.int NumOfRadius,
   [Out] System.Object^ Radius,
   [Out] System.Object^ Location,
   [Out] System.Object^ Parameter
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Bound`: Array of doubles containing the start and end boundaries (see **Remarks**)
- `NumOfRadius`: Number of radius returned; can be 0 or 1
- `Radius`: Minimum radius of curvature (see **Remarks**)
- `Location`: Position where minimum radius curvature occurred (see **Remarks**)
- `Parameter`: Curve parameter (see **Remarks**)

### Return Value

True if operation succeeds, false if it fails

## VBA Syntax

See [Curve::FindMinimumRadius](ms-its:sldworksapivb6.chm::/sldworks~Curve~FindMinimumRadius.html).

## Examples

[Find Minimum Radius of Curve (VBA)](Find_Minimum_Radius_of_Curve_Example_VB.htm)

## Remarks

The search is confined to the portion of the selected curve lying inside of Bound.

COM returns these data types for these parameters:

- Radius: VARIANT of SafeDoubleArray
- Location: VARIANT of SafeDispatchArray of [IMathpoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html)
- Parameter: VARIANT of SafeDoubleArray

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::IFindMinimumRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IFindMinimumRadius.html)
[ISurface::FindMinimumRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~FindMinimumRadius.html)
[ISurface::IFindMinimumRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IFindMinimumRadius.html)
[ICurve::GetEndParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetEndParams.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
