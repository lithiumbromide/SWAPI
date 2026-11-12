---
title: "IsAttached Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "IsAttached"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IsAttached.html"
---

# IsAttached Method (ISFSymbol)

Gets whether the leader line for this surface finish symbol is attached.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsAttached() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
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

True if a leaderline is attached, false if not

## VBA Syntax

See [SFSymbol::IsAttached](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~IsAttached.html).

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)
[ISFSymbol::HasExtraLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~HasExtraLeader.html)
[ISFSymbol::GetLeaderAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetLeaderAtIndex.html)
[ISFSymbol::GetLeaderCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetLeaderCount.html)
[ISFSymbol::IGetLeaderAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetLeaderAtIndex.html)
