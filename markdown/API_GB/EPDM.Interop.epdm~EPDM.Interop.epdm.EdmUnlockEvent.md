---
title: "EdmUnlockEvent Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmUnlockEvent"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUnlockEvent.html"
---

# EdmUnlockEvent Enumeration

Types of check-in command passed to the [IEdmUnlockOpCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback.html) interface to notify the caller about what is happening while checking in files with the [IEdmBatchUnlock](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock.html) interface.

## Syntax

### Visual Basic

```vb
Public Enum EdmUnlockEvent
   Inherits System.Enum
```

### C#

```csharp
public enum EdmUnlockEvent : System.Enum
```

### C++/CLI

```cpp
public enum class EdmUnlockEvent : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Euev_CompressingTree | 3 = Check-in command is compressing the reference tree |
| Euev_ReadingFileRefs | 1 = Check-in command is reading external references from the file |
| Euev_UnlockFile | 2 = Check-in command is checking in a file |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
