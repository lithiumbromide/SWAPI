---
title: "GetDirectionOfLay Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "GetDirectionOfLay"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetDirectionOfLay.html"
---

# GetDirectionOfLay Method (ISFSymbol)

Gets the direction of lay value for this surface finish symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDirectionOfLay() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim value As System.Integer

value = instance.GetDirectionOfLay()
```

### C#

```csharp
System.int GetDirectionOfLay()
```

### C++/CLI

```cpp
System.int GetDirectionOfLay();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Direction of lay as defined in [swSFLaySym_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSFLaySym_e.html)

## VBA Syntax

See [SFSymbol::GetDirectionOfLay](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~GetDirectionOfLay.html).

## Remarks

To set the direction of lay value, use [ISFSymbol::SetDirectionOfLay](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~SetDirectionOfLay.html).

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)
