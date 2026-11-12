---
title: "EdmMsgType Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmMsgType"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMsgType.html"
---

# EdmMsgType Enumeration

Types of messages sent to a user.

## Syntax

### Visual Basic

```vb
Public Enum EdmMsgType
   Inherits System.Enum
```

### C#

```csharp
public enum EdmMsgType : System.Enum
```

### C++/CLI

```cpp
public enum class EdmMsgType : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmMsgType_ExternalNotification | 4 = The message is an external notification |
| EdmMsgType_FileNotification | 2 = The message is a file notification |
| EdmMsgType_FolderNotification | 3 = The message is a folder notification |
| EdmMsgType_Invalid | 0 = Invalid message (internal error code) |
| EdmMsgType_UserMessage | 1 = The message is a file notification |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[IEdmMessage5::MessageType](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMessage5~MessageType.html)
