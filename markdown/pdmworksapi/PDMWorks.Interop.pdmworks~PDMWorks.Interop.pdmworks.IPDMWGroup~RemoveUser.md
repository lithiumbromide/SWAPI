---
title: "RemoveUser Method (IPDMWGroup)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWGroup"
member: "RemoveUser"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup~RemoveUser.html"
---

# RemoveUser Method (IPDMWGroup)

Removes the specified user from a group.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveUser( _
   ByVal userName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWGroup
Dim userName As System.String

instance.RemoveUser(userName)
```

### C#

```csharp
void RemoveUser(
   System.string userName
)
```

### C++/CLI

```cpp
void RemoveUser(
   System.String^ userName
)
```

### Parameters

- `userName`: Name of user to remove from group

## VBA Syntax

See [PDMWGroup::RemoveUser](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWGroup~RemoveUser.html).

## Remarks

Only a vault administrator can use this method.

## See Also

[IPDMWGroup Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup.html)
[IPDMWGroup Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup_members.html)
[IDPMWGroup::SetUserPermissions Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~SetUserPermissions.html)
[IPDMWGroup::AddUser Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup~AddUser.html)
[IPDMWConnection::CreateUser Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~CreateUser.html)
[IPDMWConnection::DeleteUser Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~DeleteUser.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
