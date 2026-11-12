---
title: "SetFieldWeld Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "SetFieldWeld"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetFieldWeld.html"
---

# SetFieldWeld Method (IWeldSymbol)

Sets the field or site weld property of this weld symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFieldWeld( _
   ByVal FieldWeld As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
Dim FieldWeld As System.Integer
Dim value As System.Boolean

value = instance.SetFieldWeld(FieldWeld)
```

### C#

```csharp
System.bool SetFieldWeld(
   System.int FieldWeld
)
```

### C++/CLI

```cpp
System.bool SetFieldWeld(
   System.int FieldWeld
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FieldWeld`: Value indicating whether this is to be a field or site weld, and, if so, whether the flag points up or down as defined in [swWeldSymbolField_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldSymbolField_e.html)

### Return Value

True if the field or site weld setting is set successfully, false if not

## VBA Syntax

See [WeldSymbol::SetFieldWeld](ms-its:sldworksapivb6.chm::/sldworks~WeldSymbol~SetFieldWeld.html).

## Examples

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html) examples.

## Remarks

To retrieve the field or site weld property of a weld symbol, use [IWeldSymbol::GetFieldWeld](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~GetFieldWeld.html).

## See Also

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
