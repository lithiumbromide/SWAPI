---
title: "EdmCreateListExFlags Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmCreateListExFlags"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCreateListExFlags.html"
---

# EdmCreateListExFlags Enumeration

Options for creating lists used in calls to [IEdmBatchListing2::CreateListEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing2~CreateListEx.html). [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmCreateListExFlags
   Inherits System.Enum
```

### C#

```csharp
public enum EdmCreateListExFlags : System.Enum
```

### C++/CLI

```cpp
public enum class EdmCreateListExFlags : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Edmclef_AllConfigurations | 2 = Return separate nodes for configurations |
| Edmclef_AsBuilt | 16 = Use as-built reference versions instead of the latest version |
| Edmclef_DontGetLatest | 64 = Do not get the latest version |
| Edmclef_GetDrawings | 8 = Return drawings of added files |
| Edmclef_GetReferences | 4 = Return references of added files |
| Edmclef_MayReadFiles | 1 = Permit the API to read variables from the cached files; if this flag is not set, values are read from the database |
| Edmclef_Nothing | 0 = Default behavior |
| Edmclef_ReturnReferences | 32 = Return file references for every node that is passed in |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
