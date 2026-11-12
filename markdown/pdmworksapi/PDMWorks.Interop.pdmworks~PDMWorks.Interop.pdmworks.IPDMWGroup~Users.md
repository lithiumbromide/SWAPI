---
title: "Users Property (IPDMWGroup)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWGroup"
member: "Users"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup~Users.html"
---

# Users Property (IPDMWGroup)

Gets the users in this group.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Users As PDMWUsers
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWGroup
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

See [PDMWGroup::Users](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWGroup~Users.html).

## See Also

[IPDMWGroup Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup.html)
[IPDMWGroup Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2004 FCS
