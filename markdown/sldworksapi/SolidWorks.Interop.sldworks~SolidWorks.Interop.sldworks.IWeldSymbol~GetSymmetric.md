---
title: "GetSymmetric Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "GetSymmetric"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetSymmetric.html"
---

# GetSymmetric Method (IWeldSymbol)

Gets whether this weld symbol is a symmetric weld.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSymmetric() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
Dim value As System.Integer

value = instance.GetSymmetric()
```

### C#

```csharp
System.int GetSymmetric()
```

### C++/CLI

```cpp
System.int GetSymmetric();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Value indicating whether this is a symmetric weld, and if not, whether the dashed line is above or below the horizontal line as defined in [swWeldSymbolSymmetric_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldSymbolSymmetric_e.html)

## VBA Syntax

See [WeldSymbol::GetSymmetric](ms-its:sldworksapivb6.chm::/sldworks~WeldSymbol~GetSymmetric.html).

## Examples

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html) examples.

## Remarks

To set a weld symbol to a symmetric weld, use [IWeldSymbol::SetSymmetric](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~SetSymmetric.html).

## See Also

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
