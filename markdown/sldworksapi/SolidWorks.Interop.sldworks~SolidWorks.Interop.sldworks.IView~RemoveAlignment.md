---
title: "RemoveAlignment Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "RemoveAlignment"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~RemoveAlignment.html"
---

# RemoveAlignment Method (IView)

Removes the alignment from this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveAlignment()
```

### Visual Basic (Usage)

```vb
Dim instance As IView

instance.RemoveAlignment()
```

### C#

```csharp
void RemoveAlignment()
```

### C++/CLI

```cpp
void RemoveAlignment();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [View::RemoveAlignment](ms-its:sldworksapivb6.chm::/sldworks~View~RemoveAlignment.html).

## Remarks

Using this method on a view only removes the alignment information from that view. It does not remove the alignments any child views have with this view.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::AlignWithView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AlignWithView.html)
[IView::UseDefaultAlignment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UseDefaultAlignment.html)
[IView::GetAlignment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAlignment.html)
