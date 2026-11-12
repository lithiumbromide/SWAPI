---
title: "HideView Method (ITaskpaneView)"
project: "SOLIDWORKS API Help"
interface: "ITaskpaneView"
member: "HideView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~HideView.html"
---

# HideView Method (ITaskpaneView)

Hides the application-level tab on the Task Pane.

## Syntax

### Visual Basic (Declaration)

```vb
Function HideView() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITaskpaneView
Dim value As System.Boolean

value = instance.HideView()
```

### C#

```csharp
System.bool HideView()
```

### C++/CLI

```cpp
System.bool HideView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the application-level tab is hidden, false if not

## VBA Syntax

See [TaskpaneView::HideView](ms-its:sldworksapivb6.chm::/sldworks~TaskpaneView~HideView.html).

## See Also

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.html)
[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.html)
[ITaskpaneView::ShowView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~ShowView.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
