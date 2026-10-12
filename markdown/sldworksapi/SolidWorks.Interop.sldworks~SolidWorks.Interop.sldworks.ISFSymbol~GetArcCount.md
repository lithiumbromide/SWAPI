---
title: "GetArcCount Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "GetArcCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArcCount.html"
---

# GetArcCount Method (ISFSymbol)

Gets the number of arcs in this surface finish symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArcCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim value As System.Integer

value = instance.GetArcCount()
```

### C#

```csharp
System.int GetArcCount()
```

### C++/CLI

```cpp
System.int GetArcCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of arcs

## VBA Syntax

See [SFSymbol::GetArcCount](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~GetArcCount.html).

## Remarks

Call this method before calling [ISFSymbol::GetArcAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetArcAtIndex.html) and [ISFSymbol::IGetArcAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~IGetArcAtIndex.html) to find out the number of arcs in this surface finish symbol.

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)
