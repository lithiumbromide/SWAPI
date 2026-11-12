---
title: "GetPeripheral Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "GetPeripheral"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetPeripheral.html"
---

# GetPeripheral Method (IWeldSymbol)

Gets whether this is a peripheral weld.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPeripheral() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
Dim value As System.Boolean

value = instance.GetPeripheral()
```

### C#

```csharp
System.bool GetPeripheral()
```

### C++/CLI

```cpp
System.bool GetPeripheral();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if a peripheral weld, false if not

## VBA Syntax

See [WeldSymbol::GetPeripheral](ms-its:sldworksapivb6.chm::/sldworks~WeldSymbol~GetPeripheral.html).

## Examples

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html) examples.

## Remarks

To set the peripheral property of a weld symbol, use [IWeldSymbol::SetPeripheral](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~SetPeripheral.html).

## See Also

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
