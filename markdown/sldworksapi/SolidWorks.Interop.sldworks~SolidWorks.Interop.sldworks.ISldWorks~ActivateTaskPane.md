---
title: "ActivateTaskPane Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "ActivateTaskPane"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActivateTaskPane.html"
---

# ActivateTaskPane Method (ISldWorks)

Activates the specified task pane.

## Syntax

### Visual Basic (Declaration)

```vb
Function ActivateTaskPane( _
   ByVal TaskPaneID As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim TaskPaneID As System.Integer
Dim value As System.Boolean

value = instance.ActivateTaskPane(TaskPaneID)
```

### C#

```csharp
System.bool ActivateTaskPane(
   System.int TaskPaneID
)
```

### C++/CLI

```cpp
System.bool ActivateTaskPane(
   System.int TaskPaneID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TaskPaneID`: ID of task pane as defined in [swTaskPaneTab_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTaskPaneTab_e.html)

### Return Value

True if the specified task pane is activated, false if not

## VBA Syntax

See [SldWorks::ActivateTaskPane](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~ActivateTaskPane.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::CreateTaskpaneView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CreateTaskpaneView2.html)
[ISldWorks::RefreshTaskpaneContent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RefreshTaskpaneContent.html)
[ISldWorks::TaskPaneIsPinned Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~TaskPaneIsPinned.html)
[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
