---
title: "IsTaskPaneVisible Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IsTaskPaneVisible"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsTaskPaneVisible.html"
---

# IsTaskPaneVisible Method (ISldWorks)

Gets whether the Task Pane is visible.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsTaskPaneVisible() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Boolean

value = instance.IsTaskPaneVisible()
```

### C#

```csharp
System.bool IsTaskPaneVisible()
```

### C++/CLI

```cpp
System.bool IsTaskPaneVisible();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

True if the Task Pane is visible, false if not

## VBA Syntax

See

[SldWorks::IsTaskPaneVisible](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IsTaskPaneVisible.html)

.

## Examples

[Create Task Pane View Add-in (C#)](Create_TaskPaneView_Add-in_Example_CSharp.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)

[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

[ITaskpaneView::IsActiveTab Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~IsActiveTab.html)

[ISldWorks::IsTaskPaneExpanded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsTaskPaneExpanded.html)

## Availability

SOLIDWORKS 2024 SP02, Revision Number 32.2
