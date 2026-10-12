---
title: "GetNext Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "GetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetNext.html"
---

# GetNext Method (ISFSymbol)

Gets the next surface finish symbol in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNext() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim value As System.Object

value = instance.GetNext()
```

### C#

```csharp
System.object GetNext()
```

### C++/CLI

```cpp
System.Object^ GetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Next [surface finish symbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol.html)

## VBA Syntax

See [SFSymbol::GetNext](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~GetNext.html).

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)
[ISFSymbol::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetNext.html)
[IView::IGetFirstSFSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstSFSymbol.html)
[IView::GetFirstSFSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstSFSymbol.html)
