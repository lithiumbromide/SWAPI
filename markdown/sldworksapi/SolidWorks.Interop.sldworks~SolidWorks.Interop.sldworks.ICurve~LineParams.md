---
title: "LineParams Property (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "LineParams"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~LineParams.html"
---

# LineParams Property (ICurve)

Gets the parameters of a curve that is a line.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property LineParams As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim value As System.Object

value = instance.LineParams
```

### C#

```csharp
System.object LineParams {get;}
```

### C++/CLI

```cpp
property System.Object^ LineParams {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [Curve::LineParams](ms-its:sldworksapivb6.chm::/sldworks~Curve~LineParams.html).

## Examples

[Get Angle Between Plane and Line (VBA)](Get_Angle_Between_Plane_and_Line_Example_VB.htm)
[Get Line Parameters (VBA)](Get_Line_Parameters_Example_VB.htm)

## Remarks

The return value is an array of 6 double values:

[ rootPoint.x, rootPoint.y, rootPoint.z, direction.x, direction.y, direction.z ]

SOLIDWORKS stores rootPoint in meters.

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::ILineParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ILineParams.html)
[ICurve::IsLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsLine.html)
[ICurve::Identity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.html)
