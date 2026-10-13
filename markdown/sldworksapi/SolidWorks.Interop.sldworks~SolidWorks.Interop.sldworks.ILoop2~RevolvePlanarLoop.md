---
title: "RevolvePlanarLoop Method (ILoop2)"
project: "SOLIDWORKS API Help"
interface: "ILoop2"
member: "RevolvePlanarLoop"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~RevolvePlanarLoop.html"
---

# RevolvePlanarLoop Method (ILoop2)

Creates a body by revolving a planar loop around an axis.

## Syntax

### Visual Basic (Declaration)

```vb
Function RevolvePlanarLoop( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal Axisx As System.Double, _
   ByVal Axisy As System.Double, _
   ByVal Axisz As System.Double, _
   ByVal RevAngle As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILoop2
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Axisx As System.Double
Dim Axisy As System.Double
Dim Axisz As System.Double
Dim RevAngle As System.Double
Dim value As System.Object

value = instance.RevolvePlanarLoop(X, Y, Z, Axisx, Axisy, Axisz, RevAngle)
```

### C#

```csharp
System.object RevolvePlanarLoop(
   System.double X,
   System.double Y,
   System.double Z,
   System.double Axisx,
   System.double Axisy,
   System.double Axisz,
   System.double RevAngle
)
```

### C++/CLI

```cpp
System.Object^ RevolvePlanarLoop(
   System.double X,
   System.double Y,
   System.double Z,
   System.double Axisx,
   System.double Axisy,
   System.double Axisz,
   System.double RevAngle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: x coordinate of the axis point
- `Y`: y coordinate of the axis point
- `Z`: z coordinate of the axis point
- `Axisx`: Direction along x
- `Axisy`: Direction along y
- `Axisz`: Direction along z
- `RevAngle`: Angle of revolution in radians

### Return Value

Array containing new [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) (element 1) and two stop [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) (elements 2 and 3)

## VBA Syntax

See [Loop2::RevolvePlanarLoop](ms-its:sldworksapivb6.chm::/sldworks~Loop2~RevolvePlanarLoop.html).

## See Also

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.html)
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.html)
[ILoop2::IRevolvePlanarLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IRevolvePlanarLoop.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
