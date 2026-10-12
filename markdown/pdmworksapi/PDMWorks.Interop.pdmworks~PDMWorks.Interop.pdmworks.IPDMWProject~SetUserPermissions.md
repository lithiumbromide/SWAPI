---
title: "SetUserPermissions Method (IPDMWProject)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWProject"
member: "SetUserPermissions"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~SetUserPermissions.html"
---

# SetUserPermissions Method (IPDMWProject)

Sets the permission for the specified user or group's project.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetUserPermissions( _
   ByVal Name As System.String, _
   ByVal permissions As PDMWPermission _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWProject
Dim Name As System.String
Dim permissions As PDMWPermission
Dim value As System.Boolean

value = instance.SetUserPermissions(Name, permissions)
```

### C#

```csharp
System.bool SetUserPermissions(
   System.string Name,
   PDMWPermission permissions
)
```

### C++/CLI

```cpp
System.bool SetUserPermissions(
   System.String^ Name,
   PDMWPermission permissions
)
```

### Parameters

- `Name`: Name of user or group's project for which to set permissions
- `permissions`: Permissions to set as defined in [PDMWPermission](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.PDMWPermission.html)

### Return Value

True if the permissions are set, false if not

## VBA Syntax

See [PDMWProject::SetUserPermissions](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWProject~SetUserPermissions.html).

## Remarks

Only a vault administrator can use this method.

## See Also

[IPDMWProject Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject.html)
[IPDMWProject Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject_members.html)
[IPDMWConnection::CreateProject Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~CreateProject.html)
[IPDMWConnection::CreateUser Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~CreateUser.html)
[IPDMWConnection::DeleteProject Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~DeleteProject.html)
[IPDMWConnection::DeleteUser Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~DeleteUser.html)
[IPDMWGroup::AddUser Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup~AddUser.html)
[IPDMWGroup::RemoveUser Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup~RemoveUser.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
