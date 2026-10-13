---
title: "ISweepPlanarLoop Method (ILoop)"
project: "SOLIDWORKS API Help"
interface: "ILoop"
member: "ISweepPlanarLoop"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop~ISweepPlanarLoop.html"
---

# ISweepPlanarLoop Method (ILoop)

Obsolete. Superseded by [ILoop2::ISweepPlanarLoop](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~ISweepPlanarLoop.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ISweepPlanarLoop( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal DraftAngle As System.Double, _
   ByRef StopFacesOut As Face _
) As Body
```

### Visual Basic (Usage)

```vb
Dim instance As ILoop
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim DraftAngle As System.Double
Dim StopFacesOut As Face
Dim value As Body

value = instance.ISweepPlanarLoop(X, Y, Z, DraftAngle, StopFacesOut)
```

### C#

```csharp
Body ISweepPlanarLoop(
   System.double X,
   System.double Y,
   System.double Z,
   System.double DraftAngle,
   ref Face StopFacesOut
)
```

### C++/CLI

```cpp
Body^ ISweepPlanarLoop(
   System.double X,
   System.double Y,
   System.double Z,
   System.double DraftAngle,
   Face^% StopFacesOut
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`:
- `Y`:
- `Z`:
- `DraftAngle`:
- `StopFacesOut`:

## VBA Syntax

See [Loop::ISweepPlanarLoop](ms-its:sldworksapivb6.chm::/sldworks~Loop~ISweepPlanarLoop.html).

## See Also

[ILoop Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop.html)
[ILoop Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop_members.html)
