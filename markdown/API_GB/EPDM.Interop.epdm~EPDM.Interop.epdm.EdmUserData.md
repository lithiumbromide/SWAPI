---
title: "EdmUserData Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmUserData"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData.html"
---

# EdmUserData Structure

Obsolete. Superseded by [EdmUserData2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData2.html) in SOLIDWORKS PDM Professional 2010 and later.

## Syntax

### Visual Basic

```vb
Public Structure EdmUserData
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmUserData : System.ValueType
```

### C++/CLI

```cpp
public value class EdmUserData : public System.ValueType
```

## Examples

struct EdmUserData{
string [mbsUserName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData~mbsUserName.html);
string [mbsInitials](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData~mbsInitials.html);
string [mbsCompleteName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData~mbsCompleteName.html);
string [mbsUserData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData~mbsUserData.html);
string [mbsPassword](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData~mbsPassword.html);
string [mbsEmail](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData~mbsEmail.html);
integer [mlFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData~mlFlags.html);
integer [mlSysRights](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData~mlSysRights.html);
string [mbsColumnView](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData~mbsColumnView.html);
integer [mlUserID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData~mlUserID.html);
integer [mhStatus](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData~mhStatus.html);
[IEdmUser6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser6.html)* [mpoUser](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData~mpoUser.html);
};

## Remarks

Holds information about a user. This struct is used as argument to [IEdmUserMgr6::AddUsers](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr6~AddUsers.html).

## See Also

[EdmUserData Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2007
