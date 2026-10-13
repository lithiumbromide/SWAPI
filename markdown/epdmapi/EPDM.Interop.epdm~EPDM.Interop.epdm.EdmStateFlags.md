---
title: "EdmStateFlags Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmStateFlags"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmStateFlags.html"
---

# EdmStateFlags Enumeration

Flags used in calls to [IEdmFile5::ChangeState](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~ChangeState.html) to set options for the operation. [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmStateFlags
   Inherits System.Enum
```

### C#

```csharp
public enum EdmStateFlags : System.Enum
```

### C++/CLI

```cpp
public enum class EdmStateFlags : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmState_Refs | 1 = Include references when changing state |
| EdmState_Simple | 0 = Default behavior of the operation |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
