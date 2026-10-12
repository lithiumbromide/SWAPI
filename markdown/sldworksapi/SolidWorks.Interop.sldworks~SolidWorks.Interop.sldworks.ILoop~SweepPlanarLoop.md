---
title: "SweepPlanarLoop Method (ILoop)"
project: "SOLIDWORKS API Help"
interface: "ILoop"
member: "SweepPlanarLoop"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop~SweepPlanarLoop.html"
---

# SweepPlanarLoop Method (ILoop)

Obsolete. Superseded by [ILoop2::SweepPlanarLoop](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~SweepPlanarLoop.html).

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
Dim instance As ILoop
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

- `X`:
- `Y`:
- `Z`:
- `DraftAngle`:

## VBA Syntax

See [Loop::SweepPlanarLoop](ms-its:sldworksapivb6.chm::/sldworks~Loop~SweepPlanarLoop.html).

## See Also

[ILoop Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop.html)
[ILoop Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop_members.html)
