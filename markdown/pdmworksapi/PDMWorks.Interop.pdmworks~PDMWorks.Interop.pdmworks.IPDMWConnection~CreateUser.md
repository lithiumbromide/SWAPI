---
title: "CreateUser Method (IPDMWConnection)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConnection"
member: "CreateUser"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~CreateUser.html"
---

# CreateUser Method (IPDMWConnection)

Creates a new user.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateUser( _
   ByVal Name As System.String, _
   ByVal password As System.String, _
   ByVal DisplayName As System.String, _
   ByVal Email As System.String, _
   ByVal Comment As System.String, _
   ByVal PropertyFilterName As System.String, _
   ByVal PropertyFilterValue As System.String _
) As PDMWUser
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConnection
Dim Name As System.String
Dim password As System.String
Dim DisplayName As System.String
Dim Email As System.String
Dim Comment As System.String
Dim PropertyFilterName As System.String
Dim PropertyFilterValue As System.String
Dim value As PDMWUser

value = instance.CreateUser(Name, password, DisplayName, Email, Comment, PropertyFilterName, PropertyFilterValue)
```

### C#

```csharp
PDMWUser CreateUser(
   System.string Name,
   System.string password,
   System.string DisplayName,
   System.string Email,
   System.string Comment,
   System.string PropertyFilterName,
   System.string PropertyFilterValue
)
```

### C++/CLI

```cpp
PDMWUser^ CreateUser(
   System.String^ Name,
   System.String^ password,
   System.String^ DisplayName,
   System.String^ Email,
   System.String^ Comment,
   System.String^ PropertyFilterName,
   System.String^ PropertyFilterValue
)
```

### Parameters

- `Name`: Name of new user
- `password`: Password for new user required at login
- `DisplayName`: Name of new user for vault administrator's purposes
- `Email`: Email of new user for vault administrator's purposes
- `Comment`: Comments for vault administrator's purposes
- `PropertyFilterName`: Name of property to use to restrict access to files and projects or an empty string to indicate that properties are not in use to restrict access
- `PropertyFilterValue`: Values for properties (use a comma between values) to restrict access to files and projects or an empty string to indicate that properties are not in use to restrict access

### Return Value

[IPDMWUser](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser.html) object

## VBA Syntax

See [PDMWConnection::CreateUser](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConnection~CreateUser.html).

## Remarks

Only a vault administrator can use this method.

## See Also

[IPDMWConnection Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection.html)
[IPDMWConnection Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection_members.html)
[IPDMWConnection::DeleteUser Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~DeleteUser.html)
[IPDMGroup::AddUser Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup~AddUser.html)
[IPDMProject::RemoveUser Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup~RemoveUser.html)
[IPDMGroup::SetUserPermissions Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~SetUserPermissions.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
