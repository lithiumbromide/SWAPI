---
title: "SetDatumTargetRotational Method (IDatumTargetSym)"
project: "SOLIDWORKS API Help"
interface: "IDatumTargetSym"
member: "SetDatumTargetRotational"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDatumTargetRotational.html"
---

# SetDatumTargetRotational Method (IDatumTargetSym)

Sets this datum target to moveable rotational.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDatumTargetRotational( _
   ByVal MoveableDatumDirection As System.Integer, _
   ByVal LockLeader As System.Boolean, _
   ByVal LockLeaderAngle As System.Double, _
   ByVal GeometryRef As System.Boolean, _
   ByRef RefGeometryError As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTargetSym
Dim MoveableDatumDirection As System.Integer
Dim LockLeader As System.Boolean
Dim LockLeaderAngle As System.Double
Dim GeometryRef As System.Boolean
Dim RefGeometryError As System.Integer
Dim value As System.Boolean

value = instance.SetDatumTargetRotational(MoveableDatumDirection, LockLeader, LockLeaderAngle, GeometryRef, RefGeometryError)
```

### C#

```csharp
System.bool SetDatumTargetRotational(
   System.int MoveableDatumDirection,
   System.bool LockLeader,
   System.double LockLeaderAngle,
   System.bool GeometryRef,
   out System.int RefGeometryError
)
```

### C++/CLI

```cpp
System.bool SetDatumTargetRotational(
   System.int MoveableDatumDirection,
   System.bool LockLeader,
   System.double LockLeaderAngle,
   System.bool GeometryRef,
   [Out] System.int RefGeometryError
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MoveableDatumDirection`: Moveable datum direction as defined in [swMoveableDatumDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMoveableDatumDirection_e.html)
- `LockLeader`: True to lock the leader, false to not
- `LockLeaderAngle`: Angle of locked leader; valid only if LockLeader is set to true
- `GeometryRef`: True to use a geometry reference, false to not; true is valid only if MoveableDatumDirection is set to swMoveableDatumDirection_e.swMoveableDatumDirectionBySelection
- `RefGeometryError`: Reference geometry error as defined in [swRefGeometryError_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRefGeometryError_e.html)

### Return Value

True if datum target successfully set, false if errors

## VBA Syntax

See [DatumTargetSym::SetDatumTargetRotational](ms-its:sldworksapivb6.chm::/sldworks~DatumTargetSym~SetDatumTargetRotational.html).

## Remarks

If GeometryRef is set to true, then select a geometry reference before calling this method.

## See Also

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.html)
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.html)
[IDatumTargetSym::SetDatumTargetNotMoveable Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDatumTargetNotMoveable.html)
[IDatumTargetSym::SetDatumTargetHorizontal Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDatumTargetHorizontal.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
