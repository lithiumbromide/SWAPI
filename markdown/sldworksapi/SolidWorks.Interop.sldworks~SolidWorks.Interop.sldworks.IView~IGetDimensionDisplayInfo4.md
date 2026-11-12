---
title: "IGetDimensionDisplayInfo4 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetDimensionDisplayInfo4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionDisplayInfo4.html"
---

# IGetDimensionDisplayInfo4 Method (IView)

Obsolete. Superseded by [IView::GetDimensionDisplayInfo5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetDimensionDisplayInfo5.html) and [IView::IGetDimensionDisplayInfo5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetDimensionDisplayInfo5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDimensionDisplayInfo4( _
   ByVal ArraySize As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim ArraySize As System.Integer
Dim value As System.Double

value = instance.IGetDimensionDisplayInfo4(ArraySize)
```

### C#

```csharp
System.double IGetDimensionDisplayInfo4(
   System.int ArraySize
)
```

### C++/CLI

```cpp
System.double IGetDimensionDisplayInfo4(
   System.int ArraySize
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ArraySize`:

## VBA Syntax

See [View::IGetDimensionDisplayInfo4](ms-its:sldworksapivb6.chm::/sldworks~View~IGetDimensionDisplayInfo4.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
