---
title: "IsActiveTab Method (ITaskpaneView)"
project: "SOLIDWORKS API Help"
interface: "ITaskpaneView"
member: "IsActiveTab"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~IsActiveTab.html"
---

# IsActiveTab Method (ITaskpaneView)

Gets whether this Task Pane view is active.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsActiveTab() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITaskpaneView
Dim value As System.Boolean

value = instance.IsActiveTab()
```

### C#

```csharp
System.bool IsActiveTab()
```

### C++/CLI

```cpp
System.bool IsActiveTab();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

True if this Task Pane view is active, false if not

## VBA Syntax

See

[TaskpaneView::IsActiveTab](ms-its:sldworksapivb6.chm::/sldworks~TaskpaneView~IsActiveTab.html)

.

## Examples

[Create Task Pane View Add-in (C#)](Create_TaskPaneView_Add-in_Example_CSharp.htm)

## See Also

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.html)

[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.html)

## Availability

SOLIDWORKS 2024 SP02, Revision Number 32.2
