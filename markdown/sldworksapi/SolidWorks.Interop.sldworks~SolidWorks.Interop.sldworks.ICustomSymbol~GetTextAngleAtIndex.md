---
title: "GetTextAngleAtIndex Method (ICustomSymbol)"
project: "SOLIDWORKS API Help"
interface: "ICustomSymbol"
member: "GetTextAngleAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol~GetTextAngleAtIndex.html"
---

# GetTextAngleAtIndex Method (ICustomSymbol)

Obsolete. Superseded by [INote::GetTextAngleAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetTextAngleAtIndex.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextAngleAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomSymbol
Dim Index As System.Integer
Dim value As System.Double

value = instance.GetTextAngleAtIndex(Index)
```

### C#

```csharp
System.double GetTextAngleAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double GetTextAngleAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`:

## VBA Syntax

See [CustomSymbol::GetTextAngleAtIndex](ms-its:sldworksapivb6.chm::/sldworks~CustomSymbol~GetTextAngleAtIndex.html).

## See Also

[ICustomSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol.html)
[ICustomSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol_members.html)
