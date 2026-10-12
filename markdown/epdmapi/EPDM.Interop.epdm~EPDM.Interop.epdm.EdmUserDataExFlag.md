---
title: "EdmUserDataExFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmUserDataExFlag"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserDataExFlag.html"
---

# EdmUserDataExFlag Enumeration

Flags that tell which members of [EdmUserDataEx](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserDataEx.html) are valid. [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmUserDataExFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmUserDataExFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmUserDataExFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Edmudex_All | A combination of all the other flags NOTE : To get better performance, call IEdmUser10::GetUserDataEx and only specify the enumerators that you need. |
| Edmudex_CellPhone | 32 = mbsCellPhone of EdmUserDataEx is valid |
| Edmudex_CompleteName | 2 = mbsCompleteName of EdmUserDataEx is valid |
| Edmudex_Email | 8 = mbsEmail of EdmUserDataEx is valid |
| Edmudex_Initials | 1 = mbsInitials of EdmUserDataEx is valid |
| Edmudex_Nothing | 0 = None of EdmUserDataEx members are valid |
| Edmudex_Phone | 16 = mbsPhone of EdmUserDataEx is valid |
| Edmudex_PicturePath | 64 = mbsPicturePath of EdmUserDataEx is valid |
| Edmudex_PresenceNote | 2048 = mbsPresenceNote of EdmUserDataEx is valid |
| Edmudex_UserData | 4 = mbsUserData of EdmUserDataEx is valid |
| Edmudex_WebSite1 | 128 = mbsWebSite1 of EdmUserDataEx is valid |
| Edmudex_WebSite2 | 256 = mbsWebSite2 of EdmUserDataEx is valid |
| Edmudex_WebSite3 | 512 = mbsWebSite3 of EdmUserDataEx is valid |
| Edmudex_WebSite4 | 1024 = mbsWebSite4 of EdmUserDataEx is valid |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[IEdmUser10::SetUserDataEx Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser10~SetUserDataEx.html)
