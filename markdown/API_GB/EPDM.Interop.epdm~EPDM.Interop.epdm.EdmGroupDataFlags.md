---
title: "EdmGroupDataFlags Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmGroupDataFlags"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupDataFlags.html"
---

# EdmGroupDataFlags Enumeration

Options specified in [EdmGroupData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData.html) used by [IEdmUserMgr6::AddGroups](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr6~AddGroups.html) to create new groups.

## Syntax

### Visual Basic

```vb
Public Enum EdmGroupDataFlags
   Inherits System.Enum
```

### C#

```csharp
public enum EdmGroupDataFlags : System.Enum
```

### C++/CLI

```cpp
public enum class EdmGroupDataFlags : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Edmgdf_ForceAdd | 4 = Add this group even if validation of the other groups in the array failed |
| Edmgdf_GetInterface | 1 = Retrieve the interface of the group and return it in EdmGroupData::mpoGroup |
| Edmgdf_Nothing | 0 = No options |
| Edmgdf_Replace | 2 = Replace the existing group |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
