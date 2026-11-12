---
title: "HasExtraLeader Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "HasExtraLeader"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~HasExtraLeader.html"
---

# HasExtraLeader Method (IWeldSymbol)

Gets whether this symbol has an extra leader.

## Syntax

### Visual Basic (Declaration)

```vb
Function HasExtraLeader() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
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

See [WeldSymbol::HasExtraLeader](ms-its:sldworksapivb6.chm::/sldworks~WeldSymbol~HasExtraLeader.html).

## Examples

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html) examples.

## See Also

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html)
[IWeldSymbol::GetLeaderAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetLeaderAtIndex.html)
[IWeldSymbol::GetLeaderCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetLeaderCount.html)
[IWeldSymbol::IGetLeaderAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetLeaderAtIndex.html)
