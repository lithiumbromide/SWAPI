---
title: "swTaskPaneNotify_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swTaskPaneNotify_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTaskPaneNotify_e.html"
---

# swTaskPaneNotify_e Enumeration

Task Pane notifications.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swTaskPaneNotify_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swTaskPaneNotify_e
```

### C#

```csharp
public enum swTaskPaneNotify_e : System.Enum
```

### C++/CLI

```cpp
public enum class swTaskPaneNotify_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAppTaskPaneActivateNotify | 1 = ActivateNotify |
| swAppTaskPaneDeactivateNotify | 2 = DeactivateNotify |
| swAppTaskPaneDestroyNotify | 3 = DestroyNotify |
| swAppTaskPaneToolbarButtonClicked | 4 = ToolbarButtonClicked |

## Remarks

To receive notifications, a DLL application must register for the notifications by object type. This registration must be done for each instance of a particular object.

For example, in the file in the Visual C++ 6.0 wizard-generated add-in that supports Task Pane events (e.g., Taskpane.h, include:

```vb
DECLARE_REGISTRY_RESOURCEID(IDR_TaskPane)
BEGIN_SINK_MAP(CTaskPane)
SINK_ENTRY_EX(ID_TASKPANE_EVENTS, DIID_DTaskpaneViewEvents, swAppTaskPaneDestroyNotify, DestroyNotify)
SINK_ENTRY_EX(ID_TASKPANE_EVENTS, DIID_DTaskpaneViewEvents, swAppTaskPaneActivateNotify, ActivateNotify)
SINK_ENTRY_EX(ID_TASKPANE_EVENTS, DIID_DTaskpaneViewEvents, swAppTaskPaneDeactivateNotify, DeActivateNotify)
END_SINK_MAP()
```

If developing a C++ application, use these enumerators to [register for notifications](sldworksapiprogguide.chm::/Overview/events.htm) for the [ITaskpaneView](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITaskpaneView.html) events.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
