---
title: "EdmUnlockOpReply Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmUnlockOpReply"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUnlockOpReply.html"
---

# EdmUnlockOpReply Enumeration

Types of operations returned from your [IEdmUnlockOpCallback::MsgBox](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback~MsgBox.html) method if you implement an [IEdmUnlockOpCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback.html) interface to use with the [IEdmBatchUnlock](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock.html) interface.

## Syntax

### Visual Basic

```vb
Public Enum EdmUnlockOpReply
   Inherits System.Enum
```

### C#

```csharp
public enum EdmUnlockOpReply : System.Enum
```

### C++/CLI

```cpp
public enum class EdmUnlockOpReply : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Euor_Cancel | 1 = Cancel the entire operation |
| Euor_ClearVar | 10 = Clear the value of the conflicting unique variable |
| Euor_Error | -1 = Internal error code; typically not returned by you |
| Euor_OK | 0 = Continue the operation |
| Euor_Retry | 12 = Retry operation |
| Euor_SkipFile | 11 = Continue the operation, but skip this particular file |

## Remarks

The return value tells SOLIDWORKS PDM Professional what to do.

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
