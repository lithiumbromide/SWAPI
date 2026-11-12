---
title: "AddUser Method (IPDMWGroup)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWGroup"
member: "AddUser"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup~AddUser.html"
---

# AddUser Method (IPDMWGroup)

Adds the specified user to this group.

## Syntax

### Visual Basic (Declaration)

```vb
Sub AddUser( _
   ByVal userName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWGroup
Dim userName As System.String

instance.AddUser(userName)
```

### C#

```csharp
void AddUser(
   System.string userName
)
```

### C++/CLI

```cpp
void AddUser(
   System.String^ userName
)
```

### Parameters

- `userName`: Name of user to add to the group

## VBA Syntax

See [PDMWGroup::AddUser](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWGroup~AddUser.html).

## Remarks

Only a vault administrator can use this method.

## See Also

[IPDMWGroup Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup.html)
[IPDMWGroup Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup_members.html)
[IPDMWConnection::CreateUser Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~CreateUser.html)
[IPDMWConnection::DeleteUser Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~DeleteUser.html)
[IPDMWGroup::RemoveUser Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup~RemoveUser.html)
[IPDMWProject::SetUserPermissions Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~SetUserPermissions.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
