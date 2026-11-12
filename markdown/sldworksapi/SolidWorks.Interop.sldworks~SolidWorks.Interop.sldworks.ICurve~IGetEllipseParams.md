---
title: "IGetEllipseParams Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "IGetEllipseParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetEllipseParams.html"
---

# IGetEllipseParams Method (ICurve)

Gets the parameters for this elliptical curve.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetEllipseParams( _
   ByRef ParamArray As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim ParamArray As System.Double

instance.IGetEllipseParams(ParamArray)
```

### C#

```csharp
void IGetEllipseParams(
   ref System.double ParamArray
)
```

### C++/CLI

```cpp
void IGetEllipseParams(
   System.double% ParamArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ParamArray`: - in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Use [ICurve::IsEllipse](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IsEllipse.html) to determine if a curve is an ellipse.

The return value is an array of doubles with the following format:

**[** `centerptX, centerptY, centerptZ, majorRad, majorAxisX, majorAxisY, majorAxisZ, minorRad, minorAxisX, minorAxisY, minorAxisZ` **]**

where:

- `centerptX, centerptY, centerptZ` = location of ellipse center
- `majorRad` = major radius
- `majorAxisX`, `majorAxisY`, `majorAxisZ` = major axis values
- `minorRad` = minor radius
- `minorAxisX`, `minorAxisY`, `minorAxisZ` = minor axis values

You must pass an array of 11 doubles that has already been allocated. If you pass a NULL
pointer or the curve is not an ellipse, then SOLIDWORKS returns S_false.

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::GetEllipseParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetEllipseParams.html)
[ICurve::Identity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.html)
