---
title: "ShowView Method (ITaskpaneView)"
project: "SOLIDWORKS API Help"
interface: "ITaskpaneView"
member: "ShowView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~ShowView.html"
---

# ShowView Method (ITaskpaneView)

Activates the application-level tab of the Task Pane view and makes the view visible.

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowView() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITaskpaneView
Dim value As System.Boolean

value = instance.ShowView()
```

### C#

```csharp
System.bool ShowView()
```

### C++/CLI

```cpp
System.bool ShowView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if application-level tab of the Task Pane view is visible, false if not

## VBA Syntax

See [TaskpaneView::ShowView](ms-its:sldworksapivb6.chm::/sldworks~TaskpaneView~ShowView.html).

## See Also

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.html)
[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.html)
[ITaskpaneView::HideView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~HideView.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
