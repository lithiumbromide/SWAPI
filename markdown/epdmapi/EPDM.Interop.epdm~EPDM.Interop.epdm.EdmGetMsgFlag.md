---
title: "EdmGetMsgFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmGetMsgFlag"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetMsgFlag.html"
---

# EdmGetMsgFlag Enumeration

Types of message returned used in calls to [IEdmInbox5::GetFirstMessagePosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmInbox5~GetFirstMessagePosition.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmGetMsgFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmGetMsgFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmGetMsgFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmGetMsg_Notifications | 4 = Return only file or folder notifications |
| EdmGetMsg_OnlyNew | 1 = Return only messages that have not been processed before |
| EdmGetMsg_OnlyUnread | 8 = Return only messages having the IEdmMessage5::IsRead flag set to true |
| EdmGetMsg_UserMessages | 2 = Return only messages sent from users |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
