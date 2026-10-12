---
title: "SketchSpline Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SketchSpline"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchSpline.html"
---

# SketchSpline Method (IModelDoc2)

Starts a spline, or continues one, using the specified point.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SketchSpline( _
   ByVal MorePts As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim MorePts As System.Integer
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double

instance.SketchSpline(MorePts, X, Y, Z)
```

### C#

```csharp
void SketchSpline(
   System.int MorePts,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
void SketchSpline(
   System.int MorePts,
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MorePts`: Number of points left to specify the spline after this one (**see Remarks**)
- `X`: x coordinate in meters
- `Y`: y coordinate in meters
- `Z`: z coordinate in meters

## VBA Syntax

See [ModelDoc2::SketchSpline](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SketchSpline.html).

## Examples

[Create 2D Spline (VBA)](Create_2D_Spline_Example_VB.htm)
[Create 2D Spline (VB.NET)](Create_2D_Spline_Example_VBNET.htm)
[Create 2D Spline (C#)](Create_2D_Spline_Example_CSharp.htm)

## Remarks

MorePts goes from n to 0 in (`n`+1) calls of this method. When `n` = 0, the last call is made to this method, and the spline is created. For example, if specifying 5 points, then the value of MorePts ranges from 4 to 0.

In SOLIDWORKS 2005 SP1 and earlier, if a failure occurred in a previous call to ModelDoc2::SketchSpline, then subsequent calls to this method failed. In SOLIDWORKS 2005 SP2 and later, if you specify a negative value for MorePts prior to sending the actual data, then the method reinitializes.

In 2D sketches, z is ignored.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
