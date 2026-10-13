---
title: "CreateTrimmedCurve2 Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "CreateTrimmedCurve2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve2.html"
---

# CreateTrimmedCurve2 Method (ICurve)

Creates a trimmed curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateTrimmedCurve2( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Z1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim Z2 As System.Double
Dim value As Curve

value = instance.CreateTrimmedCurve2(X1, Y1, Z1, X2, Y2, Z2)
```

### C#

```csharp
Curve CreateTrimmedCurve2(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

### C++/CLI

```cpp
Curve^ CreateTrimmedCurve2(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X1`: x start point
- `Y1`: y start point
- `Z1`: z end point
- `X2`: x end point
- `Y2`: y end point
- `Z2`: z end point

### Return Value

Pointer to the [ICurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) object (see **Remarks**)

## VBA Syntax

See [Curve::CreateTrimmedCurve2](ms-its:sldworksapivb6.chm::/sldworks~Curve~CreateTrimmedCurve2.html).

## Examples

[Create Temporary Extruded Body (VBA)](Create_Temporary_Extruded_Body_Example_VB.htm)
[Create Temporary Elliptical Extrusion (VBA)](Create_Temporary_Elliptical_Extrusion_Example_VB.htm)
[Create Temporary Elliptical Extrusion (VB.NET)](Create_Temporary_Elliptical_Extrusion_VBNET.htm)
[Create Temporary Elliptical Extrusion (C#)](Create_Temporary_Elliptical_Extrusion_CSharp.htm)
[Create Trimmed Curve (VBA)](Return_Untrimmed_Curve_Example_VB.htm)
[Create Trimmed Curve (VB.NET)](Return_Untrimmed_Curve_Example_VBNET.htm)
[Create Trimmed Curve (C#)](Return_Untrimmed_Curve_Example_CSharp.htm)

## Remarks

This method trims the curve from the start point to the end point in a parametric direction. It returns NULL if the curve is discontinued or non-linear between the points.

If your application calls [ISurface::CreateTrimmedSheet4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~CreateTrimmedSheet4.html) or [ISurface::ICreateTrimmedSheet4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~ICreateTrimmedSheet4.html) to create a sheet with a boundary defined by arcs ([IModeler::CreateArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateArc.html) or [IModeler::ICreateArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateArc.html)) or lines ([IModeler::CreateLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateLine.html) or [IModeler::ICreateLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateLine.html)), then your application must first call this method to trim the arc and line curves before passing them to ISurface::CreateTrimmedSheet4 or ISurface::ICreateTrimmedSheet4.

If your application calls ISurface::CreateTrimmedSheet4 or ISurface::ICreateTrimmedSheet4 to create a sheet with an elliptical boundary ([IModeler::CreateEllipse](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateEllipse.html) or [IModeler::ICreateEllipse](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateEllipse.html)), then you do not need to trim the elliptical curve before passing it to ISurface::CreateTrimmedSheet4 or ISurface::ICreateTrimmedSheet4.

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::ExtentCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ExtentCurve.html)
[ICurve::IConvertPcurveToBcurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertPcurveToBcurveSize.html)
[ICurve::IsTrimmedCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsTrimmedCurve.html)
[ICurve::JoinCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~JoinCurves.html)
[ICurve::ReverseCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ReverseCurve.html)
[ICurve::SimplifyBCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~SimplifyBCurve.html)
[ICurve::JoinCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~JoinCurves.html)

## Availability

SOLIDWORKS 2003 SP5, Revision Number 11.5
