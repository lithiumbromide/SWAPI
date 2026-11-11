---
title: "dsSelectionManagerEvent_id_e Enumeration"
project: ""
interface: "dsSelectionManagerEvent_id_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsSelectionManagerEvent_id_e.html"
---

# dsSelectionManagerEvent_id_e Enumeration

Types of selection events.

## Syntax

### Visual Basic

```vb
Public Enum dsSelectionManagerEvent_id_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsSelectionManagerEvent_id_e : System.Enum
```

### JScript

```
public enum dsSelectionManagerEvent_id_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsSelectionManagerEvent_id_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsSelectionManagerEvent_id_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsSelectionManager_SelectionChangedNotify_id | 1 = SelectionChangedNotify |
| dsSelectionManager_SelectionPreNotify_id | 2 = SelectionPreNotify |

## Remarks

To receive notifications, a DLL application must register for the notifications by object type. This registration must be done for each instance of a particular object.

For example, to register the ISelectionManager SelectionChangedNotify event in a COM native C++ interface add-in project:

BEGIN_SINK_MAP(CDsAddinSelectionManager)
SINK_ENTRY_EX(IDC_DSAPPLICATIONEVENT, DIID__ISelectionManagerEvents, dsSelectionManager_SelectionChangedNotify_id, OnSelectionChangedNotify)

END_SINK_MAP()

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
