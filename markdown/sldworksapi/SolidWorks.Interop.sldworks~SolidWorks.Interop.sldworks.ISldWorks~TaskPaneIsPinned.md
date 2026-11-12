---
title: "TaskPaneIsPinned Property (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "TaskPaneIsPinned"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~TaskPaneIsPinned.html"
---

# TaskPaneIsPinned Property (ISldWorks)

Gets or sets whether the SOLIDWORKS Task Pane is pinned.

## Syntax

### Visual Basic (Declaration)

```vb
Property TaskPaneIsPinned As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Boolean

instance.TaskPaneIsPinned = value

value = instance.TaskPaneIsPinned
```

### C#

```csharp
System.bool TaskPaneIsPinned {get; set;}
```

### C++/CLI

```cpp
property System.bool TaskPaneIsPinned {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if SOLIDWORKS Task Pane is pinned, false if not

## VBA Syntax

See [SldWorks::TaskPaneIsPinned](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~TaskPaneIsPinned.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::ActivateTaskPane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActivateTaskPane.html)
[ISldWorks::CreateTaskpaneView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CreateTaskpaneView2.html)
[ISldWorks::RefreshTaskpaneContent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RefreshTaskpaneContent.html)
[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
