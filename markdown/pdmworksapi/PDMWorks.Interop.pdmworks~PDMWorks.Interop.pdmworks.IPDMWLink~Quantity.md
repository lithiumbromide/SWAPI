---
title: "Quantity Property (IPDMWLink)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWLink"
member: "Quantity"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink~Quantity.html"
---

# Quantity Property (IPDMWLink)

Gets the number of documents associated with this link.

## Syntax

### Visual Basic (Declaration)

```vb
Property Quantity As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWLink
Dim value As System.Integer

instance.Quantity = value

value = instance.Quantity
```

### C#

```csharp
System.int Quantity {get; set;}
```

### C++/CLI

```cpp
property System.int Quantity {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Number of documents associated with this link

## VBA Syntax

See [PDMWLink::Quantity](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWLink~Quantity.html).

## See Also

[IPDMWLink Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink.html)
[IPDMWLink Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
