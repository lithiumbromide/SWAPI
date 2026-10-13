---
title: "GetAlignment Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetAlignment"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAlignment.html"
---

# GetAlignment Method (IView)

Gets the alignment information of this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAlignment() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetAlignment()
```

### C#

```csharp
System.int GetAlignment()
```

### C++/CLI

```cpp
System.int GetAlignment();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Alignment information as defined in [swViewAlignment_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewAlignment_e.html)

## VBA Syntax

See [View::GetAlignment](ms-its:sldworksapivb6.chm::/sldworks~View~GetAlignment.html).

## Remarks

The alignment information returned indicates if:

- This view is aligned with a parent view.
- There are child views that are aligned with this view.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::AlignWithView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AlignWithView.html)
[IView::RemoveAlignment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~RemoveAlignment.html)
[IView::UseDefaultAlignment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UseDefaultAlignment.html)
