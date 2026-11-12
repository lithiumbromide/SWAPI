---
title: "IsAttached Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "IsAttached"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsAttached.html"
---

# IsAttached Method (INote)

Gets whether the note is attached.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsAttached() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Boolean

value = instance.IsAttached()
```

### C#

```csharp
System.bool IsAttached()
```

### C++/CLI

```cpp
System.bool IsAttached();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if note is attached with a leaderline, false otherwise

## VBA Syntax

See [Note::IsAttached](ms-its:sldworksapivb6.chm::/sldworks~Note~IsAttached.html).

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::GetAttachPos Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetAttachPos.html)
[INote::GetLeaderCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderCount.html)
[INote::GetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderInfo.html)
[INote::GetLeaderAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderAtIndex.html)
[INote::HasExtraLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~HasExtraLeader.html)
[INote::IGetAttachPos Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetAttachPos.html)
[INote::IGetLeaderAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetLeaderAtIndex.html)
[INote::IGetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetLeaderInfo.html)
[INote::GetLeaderNumPointsAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderNumPointsAt.html)
