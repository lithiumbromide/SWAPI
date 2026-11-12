---
title: "FindMinimumRadius Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "FindMinimumRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~FindMinimumRadius.html"
---

# FindMinimumRadius Method (ISurface)

Gets the minimum radius of curvature for the selected surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function FindMinimumRadius( _
   ByVal UBound As System.Object, _
   ByVal VBound As System.Object, _
   ByRef NumOfRadius As System.Integer, _
   ByRef Radius As System.Object, _
   ByRef Location As System.Object, _
   ByRef UVParameter As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim UBound As System.Object
Dim VBound As System.Object
Dim NumOfRadius As System.Integer
Dim Radius As System.Object
Dim Location As System.Object
Dim UVParameter As System.Object
Dim value As System.Boolean

value = instance.FindMinimumRadius(UBound, VBound, NumOfRadius, Radius, Location, UVParameter)
```

### C#

```csharp
System.bool FindMinimumRadius(
   System.object UBound,
   System.object VBound,
   out System.int NumOfRadius,
   out System.object Radius,
   out System.object Location,
   out System.object UVParameter
)
```

### C++/CLI

```cpp
System.bool FindMinimumRadius(
   System.Object^ UBound,
   System.Object^ VBound,
   [Out] System.int NumOfRadius,
   [Out] System.Object^ Radius,
   [Out] System.Object^ Location,
   [Out] System.Object^ UVParameter
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UBound`: MinMax UParameter
- `VBound`: MinMax VParameter
- `NumOfRadius`: Number of radius; can be 0, 1, or 2
- `Radius`: Minimum radius of curvature (see **Remarks**)
- `Location`: [Position](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) where the minimum radius curvature occurred (see **Remarks**)
- `UVParameter`: [UV parameters](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html); because points are UV, third ordinates are 0 (see **Remarks**)

### Return Value

True if operation succeeds, false if it fails

## VBA Syntax

See [Surface::FindMinimumRadius](ms-its:sldworksapivb6.chm::/sldworks~Surface~FindMinimumRadius.html).

## Examples

[Find Minimum Radius Curvature of Surface (VBA)](Find_Minimum_Radius_Curvature_of_Surface_Example_VB.htm)

## Remarks

The search is confined to the portion of the selected curve lying inside of UBound and VBound.

COM returns these data types for these parameters:

- Radius: VARIANT of SafeDoubleArray
- Location: VARIANT of SafeDispatchArray of [IMathpoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html)
- UVParameter: VARIANT of SafeDispatchArray of [IMathpoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html)

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::IFindMinimumRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IFindMinimumRadius.html)
[ISurface::Parameterization Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~Parameterization.html)
[ISurface::IParameterization Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IParameterization.html)
[ICurve::FindMinimumRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~FindMinimumRadius.html)
[ICurve::IFindMinimumRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IFindMinimumRadius.html)
[IFace2::GetUVBounds Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetUVBounds.html)
[IFace2::IGetUVBounds Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetUVBounds.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
