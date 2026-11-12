---
title: "dsCustomPropertyControlEvent_id_e Enumeration"
project: ""
interface: "dsCustomPropertyControlEvent_id_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsCustomPropertyControlEvent_id_e.html"
---

# dsCustomPropertyControlEvent_id_e Enumeration

Types of custom property control events.

## Syntax

### Visual Basic

```vb
Public Enum dsCustomPropertyControlEvent_id_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsCustomPropertyControlEvent_id_e : System.Enum
```

### JScript

```
public enum dsCustomPropertyControlEvent_id_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsCustomPropertyControlEvent_id_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsCustomPropertyControlEvent_id_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsCustomPropertyControl_SizeChangedNotify_id | 1 = SizeChangedNotify |

## Remarks

To receive notifications, a DLL application must register for the notifications by object type. This registration must be done for each instance of a particular object.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
