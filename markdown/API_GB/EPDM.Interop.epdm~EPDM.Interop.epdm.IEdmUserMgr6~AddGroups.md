---
title: "AddGroups Method (IEdmUserMgr6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserMgr6"
member: "AddGroups"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr6~AddGroups.html"
---

# AddGroups Method (IEdmUserMgr6)

Obsolete. Superseded by [IEdmUserMgr7::AddGroups2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7~AddGroups2.html).

## Syntax

### Visual Basic

```vb
Sub AddGroups( _
   ByRef ppoGroupData As EdmGroupData() _
)
```

### C#

```csharp
void AddGroups(
   out EdmGroupData[] ppoGroupData
)
```

### C++/CLI

```cpp
void AddGroups(
   [Out] array<EdmGroupData> ppoGroupData
)
```

### Parameters

- `ppoGroupData`: Array of [EdmGroupData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData.html) structures; one structure for each user group

## Remarks

This method is superseded by [IEdmUserMgr7::AddGroups2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7~AddGroups2.html) which allows you to specify system permissions.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUserMgr6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr6.html)
[IEdmUserMgr6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr6_members.html)

## Availability

SOLIDWORKS PDM Professional 2007
