---
title: "EdmRevComponentFlags Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmRevComponentFlags"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponentFlags.html"
---

# EdmRevComponentFlags Enumeration

Flags used to control the members of the struct [EdmRevComponent2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent2.html). [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmRevComponentFlags
   Inherits System.Enum
```

### C#

```csharp
public enum EdmRevComponentFlags : System.Enum
```

### C++/CLI

```cpp
public enum class EdmRevComponentFlags : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Edmrcf_EndOfListContinue | 4 = Continue to use the last list item when the end of the list is reached |
| Edmrcf_EndOfListRestart | 2 = Restart from the first list item when the end of the list is reached |
| Edmrcf_EndOfListSendMail | 16 = Send mail to a user or group when the end of the list is reached; the recipient ID is stored in the EdmRevcomponent2 mlRecipientID struct field |
| Edmrcf_EndOfListStop | 8 = Halt the operation when the end of the list is reached |
| Edmrcf_RecipientIsGroup | 1 = EdmRevcomponent2 mlRecipientID struct field is a group ID; this flag is only used in combination with Edmrcf_EndOflistSendMail |
| Edmrcf_TypeFormatString | 32 = Revision number is of type format string |
| Edmrcf_TypeList | 64 = Revision number is of type list |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
