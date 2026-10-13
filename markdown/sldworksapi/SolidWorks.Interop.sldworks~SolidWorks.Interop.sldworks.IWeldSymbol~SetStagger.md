---
title: "SetStagger Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "SetStagger"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetStagger.html"
---

# SetStagger Method (IWeldSymbol)

Sets the stagger property of this weld symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetStagger( _
   ByVal Stagger As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
Dim Stagger As System.Boolean
Dim value As System.Boolean

value = instance.SetStagger(Stagger)
```

### C#

```csharp
System.bool SetStagger(
   System.bool Stagger
)
```

### C++/CLI

```cpp
System.bool SetStagger(
   System.bool Stagger
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Stagger`: True if this is a stagger weld, false if not

### Return Value

True if the stagger weld setting is set successfully, false if not

## VBA Syntax

See [WeldSymbol::SetStagger](ms-its:sldworksapivb6.chm::/sldworks~WeldSymbol~SetStagger.html).

## Examples

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html) examples.

## Remarks

To retrieve the stagger property of a weld symbol, use [IWeldSymbol::GetStagger](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~GetStagger.html).

## See Also

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
