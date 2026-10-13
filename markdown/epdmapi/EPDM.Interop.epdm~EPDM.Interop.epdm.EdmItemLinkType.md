---
title: "EdmItemLinkType Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmItemLinkType"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmItemLinkType.html"
---

# EdmItemLinkType Enumeration

Types of linked files to items.

## Syntax

### Visual Basic

```vb
Public Enum EdmItemLinkType
   Inherits System.Enum
```

### C#

```csharp
public enum EdmItemLinkType : System.Enum
```

### C++/CLI

```cpp
public enum class EdmItemLinkType : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmItemLnk_Attachment | 1 = Attachment links are referred to as static links in the user interface; a statically linked file does not drive the associated item; it is just an attachment |
| EdmItemLnk_Dynamic | 0 = Dynamic links are referred to as auto-update links in the user interface in SOLIDWORKS PDM Professional 2010 and later; this means that some changes in the linked file automatically propagates to the item |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[EdmGenItemInfo Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGenItemInfo.html)
