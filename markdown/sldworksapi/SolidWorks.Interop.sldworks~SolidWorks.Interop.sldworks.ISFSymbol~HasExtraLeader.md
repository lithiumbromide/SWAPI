---
title: "HasExtraLeader Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "HasExtraLeader"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~HasExtraLeader.html"
---

# HasExtraLeader Method (ISFSymbol)

Gets whether this surface finish symbol has an extra leader line.

## Syntax

### Visual Basic (Declaration)

```vb
Function HasExtraLeader() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
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

True if extra leader line exists, false if not

## VBA Syntax

See [SFSymbol::HasExtraLeader](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~HasExtraLeader.html).

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)
[ISFSymbol::GetLeaderAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetLeaderAtIndex.html)
[ISFSymbol::IGetLeaderAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetLeaderAtIndex.html)
[ISFSymbol::IsAttached Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IsAttached.html)
