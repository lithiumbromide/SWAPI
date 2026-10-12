---
title: "GetArrowHeadCount Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "GetArrowHeadCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArrowHeadCount.html"
---

# GetArrowHeadCount Method (ISFSymbol)

Gets the number of arrow heads in the surface finish symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArrowHeadCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim value As System.Integer

value = instance.GetArrowHeadCount()
```

### C#

```csharp
System.int GetArrowHeadCount()
```

### C++/CLI

```cpp
System.int GetArrowHeadCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of arrow heads

## VBA Syntax

See [SFSymbol::GetArrowHeadCount](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~GetArrowHeadCount.html).

## Remarks

Call this method before calling [ISFSymbol::GetArrowHeadAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetArrowHeadAtIndex.html) and [ISFSymbol::IGetArrowHeadAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~IGetArrowHeadAtIndex.html) to find out the number of arrow heads for this surface finish symbol.

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)
[ISFSymbol::GetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArrowHeadInfo.html)
[ISFSymbol::IGetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetArrowHeadInfo.html)
