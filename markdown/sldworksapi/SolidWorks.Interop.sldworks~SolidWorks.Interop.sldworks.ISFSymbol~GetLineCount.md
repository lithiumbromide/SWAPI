---
title: "GetLineCount Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "GetLineCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetLineCount.html"
---

# GetLineCount Method (ISFSymbol)

Gets number of line items in this surface finish symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLineCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim value As System.Integer

value = instance.GetLineCount()
```

### C#

```csharp
System.int GetLineCount()
```

### C++/CLI

```cpp
System.int GetLineCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of lines

## VBA Syntax

See [SFSymbol::GetLineCount](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~GetLineCount.html).

## Remarks

Call this method before calling [ISFSymbol::GetLineAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetLineAtIndex.html) and [ISFSymbol::IGetLineAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetLineAtIndex.html) to get the number of lines in this surface finish symbol.

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)
