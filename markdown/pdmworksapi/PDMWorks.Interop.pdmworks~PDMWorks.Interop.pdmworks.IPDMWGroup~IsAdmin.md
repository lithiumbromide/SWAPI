---
title: "IsAdmin Property (IPDMWGroup)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWGroup"
member: "IsAdmin"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup~IsAdmin.html"
---

# IsAdmin Property (IPDMWGroup)

Gets whether this group is a vault administrator.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsAdmin As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWGroup
Dim value As System.Boolean

value = instance.IsAdmin
```

### C#

```csharp
System.bool IsAdmin {get;}
```

### C++/CLI

```cpp
property System.bool IsAdmin {
   System.bool get();
}
```

### Property Value

True if this group is a vault administrator, false if not

## VBA Syntax

See [PDMWGroup::IsAdmin](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWGroup~IsAdmin.html).

## See Also

[IPDMWGroup Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup.html)
[IPDMWGroup Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2007 SP2
