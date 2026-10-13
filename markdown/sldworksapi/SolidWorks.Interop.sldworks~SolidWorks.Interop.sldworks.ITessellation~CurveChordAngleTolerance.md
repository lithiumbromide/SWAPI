---
title: "CurveChordAngleTolerance Property (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "CurveChordAngleTolerance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~CurveChordAngleTolerance.html"
---

# CurveChordAngleTolerance Property (ITessellation)

Gets or sets the maximum angle, in radians, that is allowed between a chord and its originating curve.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurveChordAngleTolerance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim value As System.Double

instance.CurveChordAngleTolerance = value

value = instance.CurveChordAngleTolerance
```

### C#

```csharp
System.double CurveChordAngleTolerance {get; set;}
```

### C++/CLI

```cpp
property System.double CurveChordAngleTolerance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value for the curve chord angle tolerance

## VBA Syntax

See [Tessellation::CurveChordAngleTolerance](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~CurveChordAngleTolerance.html).

## Remarks

This angle is calculated as the sum of the two angles between a chord and the curve tangents, measured at the chord ends.

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
