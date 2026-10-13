---
title: "EdmProgressType Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmProgressType"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmProgressType.html"
---

# EdmProgressType Enumeration

Types of progress bars that are affected by certain operations.

## Syntax

### Visual Basic

```vb
Public Enum EdmProgressType
   Inherits System.Enum
```

### C#

```csharp
public enum EdmProgressType : System.Enum
```

### C++/CLI

```cpp
public enum class EdmProgressType : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Ept_FileTransfer | 2 = Progress bar for copying the data of a single file |
| Ept_Operation | 1 = Progress bar for the entire operation |
| Ept_UpdateReference | 3 = Progress bar for updating file references |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[IEdmGetOpCallback::ProgressBegin Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback~ProgressBegin.html)
[IEdmGetOpCallback::ProgressEnd Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback~ProgressEnd.html)
[IEdmGetOpCallback::ProgressStep Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback~ProgressStep.html)
[IEdmUnlockOpCallback::ProgressBegin Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback~ProgressBegin.html)
[IEdmUnlockOpCallback::ProgressEnd Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback~ProgressEnd.html)
[IEdmUnlockOpCallback::ProgressStep Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback~ProgressStep.html)
[IEdmUnlockOpCallback::ProgressStepEvent Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback~ProgressStepEvent.html)
