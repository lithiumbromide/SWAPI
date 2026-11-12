---
title: "SetDatumTargetHorizontal Method (IDatumTargetSym)"
project: "SOLIDWORKS API Help"
interface: "IDatumTargetSym"
member: "SetDatumTargetHorizontal"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDatumTargetHorizontal.html"
---

# SetDatumTargetHorizontal Method (IDatumTargetSym)

Sets this datum target to moveable horizontal.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDatumTargetHorizontal( _
   ByVal MoveableDatumDirection As System.Integer, _
   ByVal LockLeader As System.Boolean, _
   ByVal LockLeaderAngle As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTargetSym
Dim MoveableDatumDirection As System.Integer
Dim LockLeader As System.Boolean
Dim LockLeaderAngle As System.Double
Dim value As System.Boolean

value = instance.SetDatumTargetHorizontal(MoveableDatumDirection, LockLeader, LockLeaderAngle)
```

### C#

```csharp
System.bool SetDatumTargetHorizontal(
   System.int MoveableDatumDirection,
   System.bool LockLeader,
   System.double LockLeaderAngle
)
```

### C++/CLI

```cpp
System.bool SetDatumTargetHorizontal(
   System.int MoveableDatumDirection,
   System.bool LockLeader,
   System.double LockLeaderAngle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MoveableDatumDirection`: Moveable datum direction as defined in [swMoveableDatumDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMoveableDatumDirection_e.html)
- `LockLeader`: True to lock the leader, false to not
- `LockLeaderAngle`: Angle of locked leader; valid only if LockLeader is set to true

### Return Value

True if this datum target is successfully set, false if not

## VBA Syntax

See [DatumTargetSym::SetDatumTargetHorizontal](ms-its:sldworksapivb6.chm::/sldworks~DatumTargetSym~SetDatumTargetHorizontal.html).

## See Also

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.html)
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.html)
[IDatumTargetSym::SetDatumTargetNotMoveable Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDatumTargetNotMoveable.html)
[IDatumTargetSym::SetDatumTargetRotational Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDatumTargetRotational.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
