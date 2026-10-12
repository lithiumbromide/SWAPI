---
title: "GetFieldWeld Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "GetFieldWeld"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetFieldWeld.html"
---

# GetFieldWeld Method (IWeldSymbol)

Gets the field or site weld property of this weld symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFieldWeld() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
Dim value As System.Integer

value = instance.GetFieldWeld()
```

### C#

```csharp
System.int GetFieldWeld()
```

### C++/CLI

```cpp
System.int GetFieldWeld();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Value indicating whether this is a field or site weld, and, if so, whether the flag points up or down as defined in [swWeldSymbolField_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldSymbolField_e.html)

## VBA Syntax

See [WeldSymbol::GetFieldWeld](ms-its:sldworksapivb6.chm::/sldworks~WeldSymbol~GetFieldWeld.html).

## Examples

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html) examples.

## Remarks

To set the field or site weld property of a weld symbol, use [IWeldSymbol::SetFieldWeld](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~SetFieldWeld.html).

## See Also

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
