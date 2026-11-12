---
title: "GetLeaderSide Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetLeaderSide"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderSide.html"
---

# GetLeaderSide Method (IGtol)

Gets where the leader attaches to the symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLeaderSide() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim value As System.Integer

value = instance.GetLeaderSide()
```

### C#

```csharp
System.int GetLeaderSide()
```

### C++/CLI

```cpp
System.int GetLeaderSide();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Leader attachment information as defined in [swLeaderSide_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLeaderSide_e.html)

## VBA Syntax

See [Gtol::GetLeaderSide](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetLeaderSide.html).

## Remarks

| Use... | To... |
| --- | --- |
| IGtol::IsAttached | Determine if this symbol is using a leader |
| IGtol::HasExtraLeader | Determine if this symbol is using a bent leader |
| IGtol::GetAllAround | Determine if this symbol is using an all around symbol |
| IGtol::SetLeader | Set the characteristics of the leader on this symbol |

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetLeaderCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderCount.html)
[IGtol::GetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderInfo.html)
[IGtol::GetLeaderAtIndex2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderAtIndex2.html)
[IGtol::IGetLeaderAtIndex2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLeaderAtIndex2.html)
[IGtol::IGetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLeaderInfo.html)
