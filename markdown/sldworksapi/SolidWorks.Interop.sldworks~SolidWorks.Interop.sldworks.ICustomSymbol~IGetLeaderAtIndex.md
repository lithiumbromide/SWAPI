---
title: "IGetLeaderAtIndex Method (ICustomSymbol)"
project: "SOLIDWORKS API Help"
interface: "ICustomSymbol"
member: "IGetLeaderAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol~IGetLeaderAtIndex.html"
---

# IGetLeaderAtIndex Method (ICustomSymbol)

Obsolete. Superseded by [INote::IGetLeaderAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~IGetLeaderAtIndex.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetLeaderAtIndex( _
   ByVal Index As System.Integer, _
   ByRef PointCount As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomSymbol
Dim Index As System.Integer
Dim PointCount As System.Integer
Dim value As System.Double

value = instance.IGetLeaderAtIndex(Index, PointCount)
```

### C#

```csharp
System.double IGetLeaderAtIndex(
   System.int Index,
   out System.int PointCount
)
```

### C++/CLI

```cpp
System.double IGetLeaderAtIndex(
   System.int Index,
   [Out] System.int PointCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`:
- `PointCount`:

## VBA Syntax

See [CustomSymbol::IGetLeaderAtIndex](ms-its:sldworksapivb6.chm::/sldworks~CustomSymbol~IGetLeaderAtIndex.html).

## See Also

[ICustomSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol.html)
[ICustomSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol_members.html)
