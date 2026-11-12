---
title: "IGetPolylines5 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetPolylines5"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetPolylines5.html"
---

# IGetPolylines5 Method (IView)

Obsolete. Superseded by [IView::GetPolyLines6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetPolylines6.html) and [IView::IGetPolyLines6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetPolylines6.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPolylines5( _
   ByVal CrossHatchOption As System.Short, _
   ByVal ArraySize As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim CrossHatchOption As System.Short
Dim ArraySize As System.Integer
Dim value As System.Double

value = instance.IGetPolylines5(CrossHatchOption, ArraySize)
```

### C#

```csharp
System.double IGetPolylines5(
   System.short CrossHatchOption,
   System.int ArraySize
)
```

### C++/CLI

```cpp
System.double IGetPolylines5(
   System.short CrossHatchOption,
   System.int ArraySize
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CrossHatchOption`:
- `ArraySize`:

## VBA Syntax

See [View::IGetPolylines5](ms-its:sldworksapivb6.chm::/sldworks~View~IGetPolylines5.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
