---
title: "ISweepPlanarLoop Method (ILoop2)"
project: "SOLIDWORKS API Help"
interface: "ILoop2"
member: "ISweepPlanarLoop"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~ISweepPlanarLoop.html"
---

# ISweepPlanarLoop Method (ILoop2)

Creates a temporary body by sweeping a planar loop along a vector.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISweepPlanarLoop( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal DraftAngle As System.Double, _
   ByRef StopFacesOut As Face2 _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As ILoop2
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim DraftAngle As System.Double
Dim StopFacesOut As Face2
Dim value As Body2

value = instance.ISweepPlanarLoop(X, Y, Z, DraftAngle, StopFacesOut)
```

### C#

```csharp
Body2 ISweepPlanarLoop(
   System.double X,
   System.double Y,
   System.double Z,
   System.double DraftAngle,
   ref Face2 StopFacesOut
)
```

### C++/CLI

```cpp
Body2^ ISweepPlanarLoop(
   System.double X,
   System.double Y,
   System.double Z,
   System.double DraftAngle,
   Face2^% StopFacesOut
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X component of the sweep vector
- `Y`: Y component of the sweep vector
- `Z`: Z component of the sweep vector
- `DraftAngle`: Draft angle for the faces on the side of this swept body
- `StopFacesOut`: Array of two stop [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

### Return Value

New swept [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Loop2::ISweepPlanarLoop](ms-its:sldworksapivb6.chm::/sldworks~Loop2~ISweepPlanarLoop.html).

## Remarks

This method requires simplification of the imported body.

## See Also

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.html)
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.html)
[ILoop2::SweepPlanarLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~SweepPlanarLoop.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
