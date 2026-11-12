---
title: "EdmGetOpError Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmGetOpError"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetOpError.html"
---

# EdmGetOpError Enumeration

Cold storage file retrieval error codes; used in calls to [IEdmGetOpCallback2::ReportFailureEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback2~ReportFailureEx.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmGetOpError
   Inherits System.Enum
```

### C#

```csharp
public enum EdmGetOpError : System.Enum
```

### C++/CLI

```cpp
public enum class EdmGetOpError : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmGetErr_InColdStorageAvailable | 1 = The version you are attempting to retrieve is in cold storage and needs to be retrieved from the backup media |
| EdmGetErr_InColdStorageDeleted | 2 = The version you are attempting to retrieve was sent to cold storage and deleted |
| EdmGetErr_InColdStoragePermissionDenied | 3 = The version you are attempting to retrieve is in cold storage, and you lack permission to restore it |
| EdmGetErr_InColdStorageRestoreFailed | 4 = Could not retrieve the file from cold storage |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
