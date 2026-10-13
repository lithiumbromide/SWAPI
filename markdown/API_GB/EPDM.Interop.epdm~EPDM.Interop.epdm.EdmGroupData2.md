---
title: "EdmGroupData2 Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmGroupData2"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2.html"
---

# EdmGroupData2 Structure

Contains information about a user group.

## Syntax

### Visual Basic

```vb
Public Structure EdmGroupData2
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmGroupData2 : System.ValueType
```

### C++/CLI

```cpp
public value class EdmGroupData2 : public System.ValueType
```

## Examples

struct EdmGroupData2{
string [mbsName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2~mbsName.html);
string [mbsDescription](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2~mbsDescription.html);
integer [mlFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2~mlFlags.html);
array([enum EdmSysPerm](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSysPerm.html)) [moSysPerms](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2~moSysPerms.html);
short [mbAutoAdd](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2~mbAutoAdd.html);
array(integer) [moMembers](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2~moMembers.html);
integer [mlGroupID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2~mlGroupID.html);
integer [mhStatus](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2~mhStatus.html);
[IEdmUserGroup5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5.html) *[mpoGroup](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2~mpoGroup.html);
};

## Examples

[Vault Utilities (VB.NET)](Vault_Utilities_Example_VBNET.htm)
[Vault Utilities (C#)](Vault_Utilities_Example_CSharp.htm)

## Remarks

This structure extends [EdmGroupData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData.html) and is used in [IEdmUserMgr7::AddGroups2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7~AddGroups2.html) to add user groups to the vault.

## See Also

[EdmGroupData2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2010
