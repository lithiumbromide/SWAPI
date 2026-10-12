---
title: "GetGroupMemberships Method (IEdmUser8)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUser8"
member: "GetGroupMemberships"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser8~GetGroupMemberships.html"
---

# GetGroupMemberships Method (IEdmUser8)

Gets all of the groups to which this user belongs.

## Syntax

### Visual Basic

```vb
Sub GetGroupMemberships( _
   ByRef poGroups As System.Object() _
)
```

### C#

```csharp
void GetGroupMemberships(
   out System.object[] poGroups
)
```

### C++/CLI

```cpp
void GetGroupMemberships(
   [Out] System.array<Object^> poGroups
)
```

### Parameters

- `poGroups`: Array of [IEdmUserGroup6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup6.html) interfaces

## Examples

The following sample code displays a message box with the names of all the groups to which a user, John, belongs:

Private Sub GetJohnsGroups(ByVal vault As IEdmVault12)

'Get the user interface of user 'John'
Dim userMgr As IEdmUserMgr7
userMgr = vault.CreateUtility(EdmUtility.EdmUtil_UserMgr)
Dim john As IEdmUser8
john = userMgr.GetUser("John")

'Get the groups to which he belongs
Dim groups() As Object
groups = Nothing
john.GetGroupMemberships(groups)

'Display a message box with the group names
Dim message As String
message = "John's groups:" + vbLf
Dim i As Integer
i = LBound(groups)
While (i <= UBound(groups))
Dim group As IEdmUserGroup7
group = groups(i)
message = message + group.Name + vbLf
i = i + 1
End While

MsgBox(message)

End Sub

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUser8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser8.html)
[IEdmUser8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser8_members.html)
[IEdmUser9::GetGroupMembershipsInFolder Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser9~GetGroupMembershipsInFolder.html)

## Availability

SOLIDWORKS PDM Professional 2011
