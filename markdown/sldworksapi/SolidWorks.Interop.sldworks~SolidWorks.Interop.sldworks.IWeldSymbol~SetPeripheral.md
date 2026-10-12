---
title: "SetPeripheral Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "SetPeripheral"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetPeripheral.html"
---

# SetPeripheral Method (IWeldSymbol)

Sets the peripheral property of this weld symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPeripheral( _
   ByVal Peripheral As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
Dim Peripheral As System.Boolean
Dim value As System.Boolean

value = instance.SetPeripheral(Peripheral)
```

### C#

```csharp
System.bool SetPeripheral(
   System.bool Peripheral
)
```

### C++/CLI

```cpp
System.bool SetPeripheral(
   System.bool Peripheral
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Peripheral`: True if a peripheral weld, false if not

### Return Value

True if the peripheral weld setting is set successfully, false if not

## VBA Syntax

See [WeldSymbol::SetPeripheral](ms-its:sldworksapivb6.chm::/sldworks~WeldSymbol~SetPeripheral.html).

## Examples

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html) examples.

## Remarks

To retrieve the peripheral property of a weld symbol, use [IWeldSymbol::GetPeripheral](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~GetPeripheral.html).

## See Also

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
