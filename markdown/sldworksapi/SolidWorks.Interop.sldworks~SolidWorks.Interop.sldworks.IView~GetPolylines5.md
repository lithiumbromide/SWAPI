---
title: "GetPolylines5 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetPolylines5"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolylines5.html"
---

# GetPolylines5 Method (IView)

Obsolete. Superseded by [IView::GetPolyLines6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetPolylines6.html) and [IView::IGetPolyLines6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetPolylines6.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPolylines5( _
   ByVal CrossHatchOption As System.Short _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim CrossHatchOption As System.Short
Dim value As System.Object

value = instance.GetPolylines5(CrossHatchOption)
```

### C#

```csharp
System.object GetPolylines5(
   System.short CrossHatchOption
)
```

### C++/CLI

```cpp
System.Object^ GetPolylines5(
   System.short CrossHatchOption
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CrossHatchOption`:

## VBA Syntax

See [View::GetPolylines5](ms-its:sldworksapivb6.chm::/sldworks~View~GetPolylines5.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
