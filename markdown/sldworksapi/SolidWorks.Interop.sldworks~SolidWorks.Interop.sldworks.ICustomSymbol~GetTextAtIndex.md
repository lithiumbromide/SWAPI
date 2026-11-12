---
title: "GetTextAtIndex Method (ICustomSymbol)"
project: "SOLIDWORKS API Help"
interface: "ICustomSymbol"
member: "GetTextAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol~GetTextAtIndex.html"
---

# GetTextAtIndex Method (ICustomSymbol)

Obsolete. Superseded by [INote::GetTextAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetTextAtIndex.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextAtIndex( _
   ByVal Index As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomSymbol
Dim Index As System.Integer
Dim value As System.String

value = instance.GetTextAtIndex(Index)
```

### C#

```csharp
System.string GetTextAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.String^ GetTextAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`:

## VBA Syntax

See [CustomSymbol::GetTextAtIndex](ms-its:sldworksapivb6.chm::/sldworks~CustomSymbol~GetTextAtIndex.html).

## See Also

[ICustomSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol.html)
[ICustomSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol_members.html)
