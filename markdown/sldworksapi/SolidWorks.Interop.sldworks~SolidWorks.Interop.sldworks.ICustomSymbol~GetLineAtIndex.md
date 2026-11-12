---
title: "GetLineAtIndex Method (ICustomSymbol)"
project: "SOLIDWORKS API Help"
interface: "ICustomSymbol"
member: "GetLineAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol~GetLineAtIndex.html"
---

# GetLineAtIndex Method (ICustomSymbol)

Obsolete. Superseded by [INote::GetLineAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetLineAtIndex.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLineAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomSymbol
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetLineAtIndex(Index)
```

### C#

```csharp
System.object GetLineAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetLineAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`:

## VBA Syntax

See [CustomSymbol::GetLineAtIndex](ms-its:sldworksapivb6.chm::/sldworks~CustomSymbol~GetLineAtIndex.html).

## See Also

[ICustomSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol.html)
[ICustomSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol_members.html)
