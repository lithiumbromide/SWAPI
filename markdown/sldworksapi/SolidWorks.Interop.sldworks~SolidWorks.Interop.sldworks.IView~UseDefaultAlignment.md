---
title: "UseDefaultAlignment Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "UseDefaultAlignment"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UseDefaultAlignment.html"
---

# UseDefaultAlignment Method (IView)

Restores the default alignment for this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Sub UseDefaultAlignment()
```

### Visual Basic (Usage)

```vb
Dim instance As IView

instance.UseDefaultAlignment()
```

### C#

```csharp
void UseDefaultAlignment()
```

### C++/CLI

```cpp
void UseDefaultAlignment();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [View::UseDefaultAlignment](ms-its:sldworksapivb6.chm::/sldworks~View~UseDefaultAlignment.html).

## Remarks

The default alignment for a view depends on the [view type](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~Type.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::AlignWithView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AlignWithView.html)
[IView::GetAlignment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAlignment.html)
[IView::RemoveAlignment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~RemoveAlignment.html)
