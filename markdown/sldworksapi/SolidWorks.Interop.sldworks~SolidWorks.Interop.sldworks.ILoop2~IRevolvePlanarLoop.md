---
title: "IRevolvePlanarLoop Method (ILoop2)"
project: "SOLIDWORKS API Help"
interface: "ILoop2"
member: "IRevolvePlanarLoop"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IRevolvePlanarLoop.html"
---

# IRevolvePlanarLoop Method (ILoop2)

Creates a body by revolving a planar loop around an axis.

## Syntax

### Visual Basic (Declaration)

```vb
Function IRevolvePlanarLoop( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal Axisx As System.Double, _
   ByVal Axisy As System.Double, _
   ByVal Axisz As System.Double, _
   ByVal RevAngle As System.Double, _
   ByRef StopFacesOut As Face2 _
) As Body2
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
Dim StopFacesOut As Face2
Dim value As Body2

value = instance.IRevolvePlanarLoop(X, Y, Z, Axisx, Axisy, Axisz, RevAngle, StopFacesOut)
```

### C#

```csharp
Body2 IRevolvePlanarLoop(
   System.double X,
   System.double Y,
   System.double Z,
   System.double Axisx,
   System.double Axisy,
   System.double Axisz,
   System.double RevAngle,
   out Face2 StopFacesOut
)
```

### C++/CLI

```cpp
Body2^ IRevolvePlanarLoop(
   System.double X,
   System.double Y,
   System.double Z,
   System.double Axisx,
   System.double Axisy,
   System.double Axisz,
   System.double RevAngle,
   [Out] Face2^ StopFacesOut
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
- `StopFacesOut`: Array of two stop [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

### Return Value

New [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Loop2::IRevolvePlanarLoop](ms-its:sldworksapivb6.chm::/sldworks~Loop2~IRevolvePlanarLoop.html).

## See Also

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.html)
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.html)
[ILoop2::RevolvePlanarLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~RevolvePlanarLoop.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
