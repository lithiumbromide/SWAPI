---
title: "HasExtraLeader Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "HasExtraLeader"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~HasExtraLeader.html"
---

# HasExtraLeader Method (INote)

Gets whether this note has a bent or straight leaderline.

## Syntax

### Visual Basic (Declaration)

```vb
Function HasExtraLeader() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Boolean

value = instance.HasExtraLeader()
```

### C#

```csharp
System.bool HasExtraLeader()
```

### C++/CLI

```cpp
System.bool HasExtraLeader();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if leaderline bent, false if straight

## VBA Syntax

See [Note::HasExtraLeader](ms-its:sldworksapivb6.chm::/sldworks~Note~HasExtraLeader.html).

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::GetLeaderAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderAtIndex.html)
[INote::GetLeaderCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderCount.html)
[INote::GetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderInfo.html)
[INote::IGetLeaderAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetLeaderAtIndex.html)
[INote::IGetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetLeaderInfo.html)
[INote::SetZeroLengthLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetZeroLengthLeader.html)
[INote::GetLeaderNumPointsAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderNumPointsAt.html)
