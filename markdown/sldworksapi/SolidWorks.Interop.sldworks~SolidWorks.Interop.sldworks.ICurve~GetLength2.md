---
title: "GetLength2 Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "GetLength2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetLength2.html"
---

# GetLength2 Method (ICurve)

Obsolete. Superseded by [ICurve::GetLength3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~GetLength3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLength2( _
   ByVal StartParam As System.Double, _
   ByVal EndParam As System.Double _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim StartParam As System.Double
Dim EndParam As System.Double
Dim value As System.Double

value = instance.GetLength2(StartParam, EndParam)
```

### C#

```csharp
System.double GetLength2(
   System.double StartParam,
   System.double EndParam
)
```

### C++/CLI

```cpp
System.double GetLength2(
   System.double StartParam,
   System.double EndParam
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StartParam`: Start parameter
- `EndParam`: End parameter

### Return Value

Length of the curve between the two parameters

## VBA Syntax

See [Curve::GetLength2](ms-its:sldworksapivb6.chm::/sldworks~Curve~GetLength2.html).

## Examples

[Get Edge Curve Parameterization (VBA)](Get_Edge_Curve_Parameterization_Example_VB.htm)
[Get intersecting Faces (VBA)](Get_Intersecting_Faces_Example_VB.htm)
[Get Length of Edge (VBA)](Get_Length_of_Edge_Example_VB.htm)
[Get Reference Curve Information (VBA)](Get_Reference_Curve_Information_Example_VB.htm)
[Get Start and End Points of Spline (VBA)](Get_Start_and_End_Points_of_Spline_Example_VB.htm)

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
