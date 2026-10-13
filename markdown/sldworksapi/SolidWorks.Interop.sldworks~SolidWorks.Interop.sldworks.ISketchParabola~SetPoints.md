---
title: "SetPoints Method (ISketchParabola)"
project: "SOLIDWORKS API Help"
interface: "ISketchParabola"
member: "SetPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola~SetPoints.html"
---

# SetPoints Method (ISketchParabola)

Sets all four sketch points for a parabola.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPoints( _
   ByVal CenterX As System.Double, _
   ByVal CenterY As System.Double, _
   ByVal CenterZ As System.Double, _
   ByVal ApexX As System.Double, _
   ByVal ApexY As System.Double, _
   ByVal ApexZ As System.Double, _
   ByVal StartX As System.Double, _
   ByVal StartY As System.Double, _
   ByVal StartZ As System.Double, _
   ByVal EndX As System.Double, _
   ByVal EndY As System.Double, _
   ByVal EndZ As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchParabola
Dim CenterX As System.Double
Dim CenterY As System.Double
Dim CenterZ As System.Double
Dim ApexX As System.Double
Dim ApexY As System.Double
Dim ApexZ As System.Double
Dim StartX As System.Double
Dim StartY As System.Double
Dim StartZ As System.Double
Dim EndX As System.Double
Dim EndY As System.Double
Dim EndZ As System.Double
Dim value As System.Boolean

value = instance.SetPoints(CenterX, CenterY, CenterZ, ApexX, ApexY, ApexZ, StartX, StartY, StartZ, EndX, EndY, EndZ)
```

### C#

```csharp
System.bool SetPoints(
   System.double CenterX,
   System.double CenterY,
   System.double CenterZ,
   System.double ApexX,
   System.double ApexY,
   System.double ApexZ,
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   System.double EndX,
   System.double EndY,
   System.double EndZ
)
```

### C++/CLI

```cpp
System.bool SetPoints(
   System.double CenterX,
   System.double CenterY,
   System.double CenterZ,
   System.double ApexX,
   System.double ApexY,
   System.double ApexZ,
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   System.double EndX,
   System.double EndY,
   System.double EndZ
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CenterX`: x coordinate of center (focal) sketch point
- `CenterY`: y coordinate of center (focal) sketch point
- `CenterZ`: z coordinate of center (focal) sketch point
- `ApexX`: x coordinate of apex sketch point
- `ApexY`: y coordinate of apex sketch point
- `ApexZ`: z coordinate of apex sketch point
- `StartX`: x coordinate of start sketch point
- `StartY`: y coordinate of start sketch point
- `StartZ`: z coordinate of start sketch point
- `EndX`: x coordinate of end sketch point
- `EndY`: y coordinate of end sketch point
- `EndZ`: z coordinate of end sketch point

### Return Value

True if all four sketch points are set, false if not

## VBA Syntax

See [SketchParabola::SetPoints](ms-its:sldworksapivb6.chm::/Sldworks~SketchParabola~SetPoints.html).

## See Also

[ISketchParabola Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola.html)
[ISketchParabola Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola_members.html)

## Availability

SOLIDWORKS 2007 SP5, Revision Number 15.5
