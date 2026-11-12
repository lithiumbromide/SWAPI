---
title: "GetAllOverThisSide Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetAllOverThisSide"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetAllOverThisSide.html"
---

# GetAllOverThisSide Method (IGtol)

Gets whether this GTol uses an All Over This Side leader.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAllOverThisSide() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim value As System.Boolean

value = instance.GetAllOverThisSide()
```

### C#

```csharp
System.bool GetAllOverThisSide()
```

### C++/CLI

```cpp
System.bool GetAllOverThisSide();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this GTol uses an All Over This Side leader, false if not

## VBA Syntax

See [Gtol::GetAllOverThisSide](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetAllOverThisSide.html).

## Remarks

This property is valid only for bent, perpendicular, and multi-jog leaders. Call [IGtol::GetLeaderAtIndex2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderAtIndex2.html) to determine which type of leader is set for this GTol.

Use:

- [IGtol::IsAttached](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~IsAttached.html) to determine whether this symbol is currently using a leader.
- [IGtol::HasExtraLeader](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~HasExtraLeader.html) to determine whether this symbol is using a bent leader.
- [IGtol::GetLeaderSide](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~GetLeaderSide.html) to determine where the leader is attached to the symbol.
- [IGtol::SetLeader](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~SetLeader.html) to set the characteristics of the leader on this symbol.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::SetAllOverThisSide Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetAllOverThisSide.html)
[IGtol::GetAllAroundThisSide Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetAllAroundThisSide.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
