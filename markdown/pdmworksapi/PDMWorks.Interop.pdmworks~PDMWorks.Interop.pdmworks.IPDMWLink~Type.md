---
title: "Type Property (IPDMWLink)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWLink"
member: "Type"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink~Type.html"
---

# Type Property (IPDMWLink)

Gets the type of link.

## Syntax

### Visual Basic (Declaration)

```vb
Property Type As PDMWLinkType
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWLink
Dim value As PDMWLinkType

instance.Type = value

value = instance.Type
```

### C#

```csharp
PDMWLinkType Type {get; set;}
```

### C++/CLI

```cpp
property PDMWLinkType Type {
   PDMWLinkType get();
   void set (    PDMWLinkType value);
}
```

### Property Value

Type of link as defined by [PDMWLinkType](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.PDMWLinkType.html)

## VBA Syntax

See [PDMWLink::Type](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWLink~Type.html).

## See Also

[IPDMWLink Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink.html)
[IPDMWLink Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
