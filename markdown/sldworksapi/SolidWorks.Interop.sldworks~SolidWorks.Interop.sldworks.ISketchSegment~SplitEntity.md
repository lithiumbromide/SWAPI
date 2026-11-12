---
title: "SplitEntity Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "SplitEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~SplitEntity.html"
---

# SplitEntity Method (ISketchSegment)

Splits the selected sketch entity at the specified point.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SplitEntity( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal ClosedX As System.Double, _
   ByVal ClosedY As System.Double, _
   ByVal ClosedZ As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim ClosedX As System.Double
Dim ClosedY As System.Double
Dim ClosedZ As System.Double

instance.SplitEntity(X, Y, Z, ClosedX, ClosedY, ClosedZ)
```

### C#

```csharp
void SplitEntity(
   System.double X,
   System.double Y,
   System.double Z,
   System.double ClosedX,
   System.double ClosedY,
   System.double ClosedZ
)
```

### C++/CLI

```cpp
void SplitEntity(
   System.double X,
   System.double Y,
   System.double Z,
   System.double ClosedX,
   System.double ClosedY,
   System.double ClosedZ
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: x coordinate where to split the selected entity
- `Y`: y coordinate where to split the selected entity
- `Z`: z coordinate where to split the selected entity
- `ClosedX`: x coordinate where to close the split entity
- `ClosedY`: y coordinate where to close the split entity
- `ClosedZ`: z coordinate where to close the split entity

## VBA Syntax

See [SketchSegment::SplitEntity](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~SplitEntity.html).

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 17.0
