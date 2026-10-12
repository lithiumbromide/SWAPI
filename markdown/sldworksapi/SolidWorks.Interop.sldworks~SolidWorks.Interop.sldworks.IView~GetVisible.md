---
title: "GetVisible Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetVisible"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisible.html"
---

# GetVisible Method (IView)

Gets the visibility of this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVisible() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

value = instance.GetVisible()
```

### C#

```csharp
System.bool GetVisible()
```

### C++/CLI

```cpp
System.bool GetVisible();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the view is be visible, false if not

## VBA Syntax

See [View::GetVisible](ms-its:sldworksapivb6.chm::/sldworks~View~GetVisible.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::SetVisible Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetVisible.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
