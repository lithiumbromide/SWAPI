---
title: "SetLeader Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "SetLeader"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetLeader.html"
---

# SetLeader Method (IGtol)

Sets the characteristics of the leader for this symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetLeader( _
   ByVal Leader As System.Boolean, _
   ByVal LeaderSide As System.Integer, _
   ByVal BentLeader As System.Boolean, _
   ByVal AllAround As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim Leader As System.Boolean
Dim LeaderSide As System.Integer
Dim BentLeader As System.Boolean
Dim AllAround As System.Boolean

instance.SetLeader(Leader, LeaderSide, BentLeader, AllAround)
```

### C#

```csharp
void SetLeader(
   System.bool Leader,
   System.int LeaderSide,
   System.bool BentLeader,
   System.bool AllAround
)
```

### C++/CLI

```cpp
void SetLeader(
   System.bool Leader,
   System.int LeaderSide,
   System.bool BentLeader,
   System.bool AllAround
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Leader`: True enables a leader on this symbol, false disables it
- `LeaderSide`: Leader attachment information as defined in [swLeaderSide_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLeaderSide_e.html)
- `BentLeader`: True enables a bent leader on this symbol, false disables it
- `AllAround`: True enables the all around symbol on the leader, false disables it

## VBA Syntax

See [Gtol::SetLeader](ms-its:sldworksapivb6.chm::/sldworks~Gtol~SetLeader.html).

## Remarks

This method ignores:

- LeaderSide, BentLeader, and AllAround values if the leader value is false. Use [IGtol::IsAttached](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~IsAttached.html) to determine if this symbol is currently using a leader.
- AllAround value if the BentLeader value is false. Use [IGtol::HasExtraLeader](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~HasExtraLeader.html) to determine if this symbol is using a bent leader.

Use:

- [IGtol::GetLeaderSide](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~GetLeaderSide.html) to determine where the leader is attached to the symbol
- [IGtol::GetAllAround](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~GetAllAround.html) to determine if this leader is using the all around symbol

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetLeaderAtIndex2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderAtIndex2.html)
[IGtol::GetLeaderCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderCount.html)
[IGtol::GetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderInfo.html)
[IGtol::IGetLeaderAtIndex2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLeaderAtIndex2.html)
[IGtol::IGetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLeaderInfo.html)
