---
title: "IGetOutline Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetOutline"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetOutline.html"
---

# IGetOutline Method (IView)

Gets the bounding box for a view (sheet or drawing) in meters on the drawing page.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetOutline() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Double

value = instance.IGetOutline()
```

### C#

```csharp
System.double IGetOutline()
```

### C++/CLI

```cpp
System.double IGetOutline();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [View::IGetOutline](ms-its:sldworksapivb6.chm::/sldworks~View~IGetOutline.html).

## Remarks

The return value is an array of 4 doubles with the following format:

- 0, X min
- 1, Y min
- 2, X max
- 3, Y max

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetOutline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetOutline.html)
