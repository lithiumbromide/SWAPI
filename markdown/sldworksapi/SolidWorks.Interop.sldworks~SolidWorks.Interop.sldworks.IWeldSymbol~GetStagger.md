---
title: "GetStagger Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "GetStagger"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetStagger.html"
---

# GetStagger Method (IWeldSymbol)

Gets whether this weld symbol is a stagger weld.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStagger() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
Dim value As System.Boolean

value = instance.GetStagger()
```

### C#

```csharp
System.bool GetStagger()
```

### C++/CLI

```cpp
System.bool GetStagger();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this is a stagger weld, false if not

## VBA Syntax

See [WeldSymbol::GetStagger](ms-its:sldworksapivb6.chm::/sldworks~WeldSymbol~GetStagger.html).

## Examples

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html) examples.

## Remarks

To set the weld symbol to a stagger weld, use [IWeldSymbol::SetStagger](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~SetStagger.html).

## See Also

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
