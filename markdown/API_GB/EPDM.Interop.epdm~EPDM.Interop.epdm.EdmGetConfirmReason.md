---
title: "EdmGetConfirmReason Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmGetConfirmReason"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetConfirmReason.html"
---

# EdmGetConfirmReason Enumeration

Types of confirmation to specify when calling [IEdmGetOpCallback::ConfirmReplace](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback~ConfirmReplace.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmGetConfirmReason
   Inherits System.Enum
```

### C#

```csharp
public enum EdmGetConfirmReason : System.Enum
```

### C++/CLI

```cpp
public enum class EdmGetConfirmReason : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Egcr_Locked | 1 = File is checked out |
| Egcr_UnlockedWritable | 2 = File is checkd in but writable |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
