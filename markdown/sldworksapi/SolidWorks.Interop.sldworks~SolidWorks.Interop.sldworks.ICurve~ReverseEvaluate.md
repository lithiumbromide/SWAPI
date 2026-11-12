---
title: "ReverseEvaluate Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "ReverseEvaluate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ReverseEvaluate.html"
---

# ReverseEvaluate Method (ICurve)

Gets the U parameter for the given XYZ location on this curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReverseEvaluate( _
   ByVal PositionX As System.Double, _
   ByVal PositionY As System.Double, _
   ByVal PositionZ As System.Double _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim PositionX As System.Double
Dim PositionY As System.Double
Dim PositionZ As System.Double
Dim value As System.Double

value = instance.ReverseEvaluate(PositionX, PositionY, PositionZ)
```

### C#

```csharp
System.double ReverseEvaluate(
   System.double PositionX,
   System.double PositionY,
   System.double PositionZ
)
```

### C++/CLI

```cpp
System.double ReverseEvaluate(
   System.double PositionX,
   System.double PositionY,
   System.double PositionZ
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PositionX`: X coordinate of this location on the curve
- `PositionY`: Y coordinate of this location on the curve
- `PositionZ`: Z coordinate of this location on the curve

### Return Value

U parameter value for this location on the curve

## VBA Syntax

See [Curve::ReverseEvaluate](ms-its:sldworksapivb6.chm::/sldworks~Curve~ReverseEvaluate.html).

## Examples

[Get UV Parameters for XYZ Location (VBA)](Get_UV_Parameters_For_XYZ_Location_Example_VB.htm)
[Get UV Parameters for XYZ Location (VB.NET)](Get_UV_Parameters_For_XYZ_Location_Example_VBNET.htm)
[Get UV Parameters for XYZ Location (C#)](Get_UV_Parameters_For_XYZ_Location_Example_CSharp.htm)

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[IFace2::ReverseEvaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ReverseEvaluate.html)
[IFace2::IReverseEvaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IReverseEvaluate.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
