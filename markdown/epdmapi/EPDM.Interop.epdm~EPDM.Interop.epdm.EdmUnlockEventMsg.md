---
title: "EdmUnlockEventMsg Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmUnlockEventMsg"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUnlockEventMsg.html"
---

# EdmUnlockEventMsg Enumeration

Type of check-in commands passed to [IEdmUnlockOpCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback.html) while checking in files with the [IEdmBatchUnlock](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock.html) interface in order to notify the caller about the progress of the operation.

## Syntax

### Visual Basic

```vb
Public Enum EdmUnlockEventMsg
   Inherits System.Enum
```

### C#

```csharp
public enum EdmUnlockEventMsg : System.Enum
```

### C++/CLI

```cpp
public enum class EdmUnlockEventMsg : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Euev_ReadingDbFileInfo | 1 = Check-in command is reading information from the database about the selected files |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
