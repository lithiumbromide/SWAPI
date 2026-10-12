---
title: "SweepPlanarLoop Method (ILoop2)"
project: "SOLIDWORKS API Help"
interface: "ILoop2"
member: "SweepPlanarLoop"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~SweepPlanarLoop.html"
---

# SweepPlanarLoop Method (ILoop2)

Creates a temporary body by sweeping a planar loop along a vector.

## Syntax

### Visual Basic (Declaration)

```vb
Function SweepPlanarLoop( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal DraftAngle As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILoop2
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim DraftAngle As System.Double
Dim value As System.Object

value = instance.SweepPlanarLoop(X, Y, Z, DraftAngle)
```

### C#

```csharp
System.object SweepPlanarLoop(
   System.double X,
   System.double Y,
   System.double Z,
   System.double DraftAngle
)
```

### C++/CLI

```cpp
System.Object^ SweepPlanarLoop(
   System.double X,
   System.double Y,
   System.double Z,
   System.double DraftAngle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X component of the sweep vector
- `Y`: Y component of the sweep vector
- `Z`: Z component of the sweep vector
- `DraftAngle`: Draft angle for the faces on the side of this swept body

### Return Value

Array containing new swept [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) (element 1) and two stop [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) (elements 2 and 3)

## VBA Syntax

See [Loop2::SweepPlanarLoop](ms-its:sldworksapivb6.chm::/sldworks~Loop2~SweepPlanarLoop.html).

## Examples

[Sweep Planar Loop Along Vector (VBA)](Sweep_Planar_Loop_Along_Vector_Example_VB.htm)

## Remarks

This method requires simplification of the imported body.

## See Also

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.html)
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.html)
[ILoop2::ISweepPlanarLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~ISweepPlanarLoop.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
