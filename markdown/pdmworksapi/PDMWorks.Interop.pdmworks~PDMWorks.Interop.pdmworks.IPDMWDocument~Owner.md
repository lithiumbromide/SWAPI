---
title: "Owner Property (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "Owner"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~Owner.html"
---

# Owner Property (IPDMWDocument)

Gets the current owner of this document, which may be different from the author of the document.

## Syntax

### Visual Basic (Declaration)

```vb
Property Owner As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As System.String

instance.Owner = value

value = instance.Owner
```

### C#

```csharp
System.string Owner {get; set;}
```

### C++/CLI

```cpp
property System.String^ Owner {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the current owner of this document

## VBA Syntax

See [PDMWDocument::Owner](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~Owner.html).

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
