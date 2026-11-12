---
title: "SetAllOver Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "SetAllOver"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetAllOver.html"
---

# SetAllOver Method (IGtol)

Sets whether this Gtol uses an All Over leader.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetAllOver( _
   ByVal AllOver As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim AllOver As System.Boolean

instance.SetAllOver(AllOver)
```

### C#

```csharp
void SetAllOver(
   System.bool AllOver
)
```

### C++/CLI

```cpp
void SetAllOver(
   System.bool AllOver
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AllOver`: True to use an All Over leader, false to not

## VBA Syntax

See [Gtol::SetAllOver](ms-its:sldworksapivb6.chm::/sldworks~Gtol~SetAllOverThisSide.html).

## Remarks

This property is valid only for bent, perpendicular, and multi-jog leaders.

Use:

- [IGtol::IsAttached](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~IsAttached.html) to determine whether this symbol is currently using a leader.
- [IGtol::HasExtraLeader](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~HasExtraLeader.html) to determine whether this symbol is using a bent leader.
- [IGtol::GetLeaderSide](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~GetLeaderSide.html) to determine where the leader is attached to the symbol.
- [IGtol::SetLeader](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~SetLeader.html) to set the characteristics of the leader on this symbol.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGTol::GetAllOver Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetAllOver.html)
[IGTol::SetAllAroundThisSide Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetAllAroundThisSide.html)
[IGTol::SetAllOverThisSide Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetAllOverThisSide.html)

## Availability

SOLIDWORKS 2026 SP2, Revision Number 34.2
