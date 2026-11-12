---
title: "SetSymmetric Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "SetSymmetric"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetSymmetric.html"
---

# SetSymmetric Method (IWeldSymbol)

Sets whether this weld symbol is a symmetric weld.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSymmetric( _
   ByVal Symmetric As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
Dim Symmetric As System.Integer
Dim value As System.Boolean

value = instance.SetSymmetric(Symmetric)
```

### C#

```csharp
System.bool SetSymmetric(
   System.int Symmetric
)
```

### C++/CLI

```cpp
System.bool SetSymmetric(
   System.int Symmetric
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Symmetric`: Value indicating whether this should be a symmetric weld, and if not, whether the dashed line is above or below the horizontal line as defined in [swWeldSymbolSymmetric_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldSymbolSymmetric_e.html)

## VBA Syntax

See [WeldSymbol::SetSymmetric](ms-its:sldworksapivb6.chm::/sldworks~WeldSymbol~SetSymmetric.html).

## Examples

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html) examples.

## Remarks

To get whether a weld symbol is a symmetric weld, use [IWeldSymbol::GetSymmetric](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~GetSymmetric.html).

## See Also

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
