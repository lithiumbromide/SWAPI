---
title: "DeleteUser Method (IPDMWConnection)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConnection"
member: "DeleteUser"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~DeleteUser.html"
---

# DeleteUser Method (IPDMWConnection)

Deletes the specified user.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DeleteUser( _
   ByVal Name As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConnection
Dim Name As System.String

instance.DeleteUser(Name)
```

### C#

```csharp
void DeleteUser(
   System.string Name
)
```

### C++/CLI

```cpp
void DeleteUser(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of user to delete

## VBA Syntax

See [PDMWConnection::DeleteUser](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConnection~DeleteUser.html).

## Remarks

Only a vault administrator can use this method.

## See Also

[IPDMWConnection Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection.html)
[IPDMWConnection Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection_members.html)
[IPDMWConnection::CreateUser Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~CreateUser.html)
[IPDMWProject::SetUserPermissions Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~SetUserPermissions.html)
[IPDMWGroup::AddUser Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup~AddUser.html)
[IPDMWGroup::RemoveUser Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup~RemoveUser.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
