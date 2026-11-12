---
title: "Name Property (IPDMWLink)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWLink"
member: "Name"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink~Name.html"
---

# Name Property (IPDMWLink)

Gets the name of the document for this link.

## Syntax

### Visual Basic (Declaration)

```vb
Property Name As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWLink
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

### Property Value

Name of the document for this link

## VBA Syntax

See [PDMWLink::Name](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWLink~Name.html).

## See Also

[IPDMWLink Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink.html)
[IPDMWLink Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
