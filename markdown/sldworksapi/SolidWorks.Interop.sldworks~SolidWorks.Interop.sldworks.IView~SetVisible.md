---
title: "SetVisible Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "SetVisible"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetVisible.html"
---

# SetVisible Method (IView)

Sets the visibility of this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetVisible( _
   ByVal Visible As System.Boolean, _
   ByVal DependentsToo As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Visible As System.Boolean
Dim DependentsToo As System.Boolean

instance.SetVisible(Visible, DependentsToo)
```

### C#

```csharp
void SetVisible(
   System.bool Visible,
   System.bool DependentsToo
)
```

### C++/CLI

```cpp
void SetVisible(
   System.bool Visible,
   System.bool DependentsToo
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Visible`: True to set the view to visible, false to not
- `DependentsToo`: True to set the dependents of this view to visible, false to not

## VBA Syntax

See [View::SetVisible](ms-its:sldworksapivb6.chm::/sldworks~View~SetVisible.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetVisible Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisible.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 10.0
