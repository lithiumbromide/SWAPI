---
title: "IsAttached Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "IsAttached"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IsAttached.html"
---

# IsAttached Method (IGtol)

Gets whether this GTol is attached.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsAttached() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
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

True if GTol is attached with a leaderline, false if not

## VBA Syntax

See [Gtol::IsAttached](ms-its:sldworksapivb6.chm::/sldworks~Gtol~IsAttached.html).

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetLeaderAtIndex2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderAtIndex2.html)
[IGtol::GetLeaderCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderCount.html)
[IGtol::GetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderInfo.html)
[IGtol::GetLeaderSide Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderSide.html)
[IGtol::HasExtraLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~HasExtraLeader.html)
[IGtol::IGetLeaderAtIndex2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLeaderAtIndex2.html)
[IGtol::IGetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLeaderInfo.html)
[IGtol::IGetLineAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLineAtIndex.html)
