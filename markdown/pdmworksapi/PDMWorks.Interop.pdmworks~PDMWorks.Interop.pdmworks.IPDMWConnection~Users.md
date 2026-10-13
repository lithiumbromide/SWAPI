---
title: "Users Property (IPDMWConnection)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConnection"
member: "Users"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~Users.html"
---

# Users Property (IPDMWConnection)

Gets a collection of users.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Users As PDMWUsers
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConnection
Dim value As PDMWUsers

value = instance.Users
```

### C#

```csharp
PDMWUsers Users {get;}
```

### C++/CLI

```cpp
property PDMWUsers^ Users {
   PDMWUsers^ get();
}
```

### Property Value

[IPDMWUsers](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUsers.html) collection

## VBA Syntax

See [PDMWConnection::Users](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConnection~Users.html).

## See Also

[IPDMWConnection Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection.html)
[IPDMWConnection Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2004 FCS
