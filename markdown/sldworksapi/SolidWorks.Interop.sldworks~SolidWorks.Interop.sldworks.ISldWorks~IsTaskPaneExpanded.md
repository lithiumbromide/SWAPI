---
title: "IsTaskPaneExpanded Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IsTaskPaneExpanded"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsTaskPaneExpanded.html"
---

# IsTaskPaneExpanded Method (ISldWorks)

Gets whether the Task Pane is expanded.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsTaskPaneExpanded() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Boolean

value = instance.IsTaskPaneExpanded()
```

### C#

```csharp
System.bool IsTaskPaneExpanded()
```

### C++/CLI

```cpp
System.bool IsTaskPaneExpanded();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

True if the Task Pane is expanded, false if not

## VBA Syntax

See

[SldWorks::IsTaskPaneExpanded](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IsTaskPaneExpanded.html)

.

## Examples

[Create Task Pane View Add-in (C#)](Create_TaskPaneView_Add-in_Example_CSharp.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)

[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

[ITaskpaneView::IsActiveTab Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~IsActiveTab.html)

[ISldWorks::IsTaskPaneVisible Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsTaskPaneVisible.html)

## Availability

SOLIDWORKS 2024 SP02, Revision Number 32.2
