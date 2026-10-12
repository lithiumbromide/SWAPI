---
title: "Name Property (IPDMWGroup)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWGroup"
member: "Name"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup~Name.html"
---

# Name Property (IPDMWGroup)

Gets or sets the name of this group.

## Syntax

### Visual Basic (Declaration)

```vb
Property Name As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWGroup
Dim value As System.String

instance.Name = value

value = instance.Name
```

### C#

```csharp
System.string Name {get; set;}
```

### C++/CLI

```cpp
property System.String^ Name {
   System.String^ get();
   void set (    System.String^ value);
}
```

## VBA Syntax

See [PDMWGroup::Name](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWGroup~Name.html).

## Remarks

Only a vault administrator can set the name of this group.

## See Also

[IPDMWGroup Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup.html)
[IPDMWGroup Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
