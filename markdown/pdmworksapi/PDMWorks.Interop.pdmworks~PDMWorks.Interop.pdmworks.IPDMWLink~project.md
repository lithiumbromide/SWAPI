---
title: "project Property (IPDMWLink)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWLink"
member: "project"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink~project.html"
---

# project Property (IPDMWLink)

Gets the name of the project for the document for this link.

## Syntax

### Visual Basic (Declaration)

```vb
Property project As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWLink
Dim value As System.String

instance.project = value

value = instance.project
```

### C#

```csharp
System.string project {get; set;}
```

### C++/CLI

```cpp
property System.String^ project {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of project for this link

## VBA Syntax

See [PDMWLink::project](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWLink~project.html).

## See Also

[IPDMWLink Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink.html)
[IPDMWLink Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 SP3
