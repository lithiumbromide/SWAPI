---
title: "GetEllipseParams Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "GetEllipseParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetEllipseParams.html"
---

# GetEllipseParams Method (ICurve)

Gets the parameters for this elliptical curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEllipseParams() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim value As System.Object

value = instance.GetEllipseParams()
```

### C#

```csharp
System.object GetEllipseParams()
```

### C++/CLI

```cpp
System.Object^ GetEllipseParams();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Object (see **Remarks**)

## VBA Syntax

See [Curve::GetEllipseParams](ms-its:sldworksapivb6.chm::/sldworks~Curve~GetEllipseParams.html).

## Remarks

Use [ICurve::IsEllipse](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IsEllipse.html) to determine if a curve is an ellipse.

The return value is an array of doubles with the following format:

**[** `centerptX, centerptY, centerptZ, majorRad, majorAxisX, majorAxisY, majorAxisZ, minorRad, minorAxisX, minorAxisY, minorAxisZ` **]**

where:

- `centerptX`, `centerptY`, `centerptZ` = location of ellipse center
- `majorRad` = major radius
- `majorAxisX`, `majorAxisY`, `majorAxisZ` = major axis values
- `minorRad` = minor radius
- `minorAxisX`, `minorAxisY`, `minorAxisZ` = minor axis values

For Dispatch users, if this curve is not an ellipse, then SOLIDWORKS returns an empty
VARIANT. Otherwise, SOLIDWORKS returns a SafeArray in Visual Basic for Applications (VBA).

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::Identity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.html)
[ICurve::IGetEllipseParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetEllipseParams.html)
[ICurve::IsEllipse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsEllipse.html)

## Availability

SOLIDWORKS 98Plus, datecode 1999042
