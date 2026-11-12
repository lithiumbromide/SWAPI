---
title: "Groups Property (IPDMWConnection)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConnection"
member: "Groups"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~Groups.html"
---

# Groups Property (IPDMWConnection)

Gets a collection of groups.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Groups As PDMWGroups
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConnection
Dim value As PDMWGroups

value = instance.Groups
```

### C#

```csharp
PDMWGroups Groups {get;}
```

### C++/CLI

```cpp
property PDMWGroups^ Groups {
   PDMWGroups^ get();
}
```

### Property Value

[IPDMWGroups](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroups.html) collection

## VBA Syntax

See [PDMWConnection::Groups](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConnection~Groups.html).

## See Also

[IPDMWConnection Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection.html)
[IPDMWConnection Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2004 FCS
