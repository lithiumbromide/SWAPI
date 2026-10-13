---
title: "Attachments Property (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "Attachments"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~Attachments.html"
---

# Attachments Property (IPDMWDocument)

Gets the non-SOLIDWORKS attachments for this SOLIDWORKS document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Attachments As PDMWLinks
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As PDMWLinks

value = instance.Attachments
```

### C#

```csharp
PDMWLinks Attachments {get;}
```

### C++/CLI

```cpp
property PDMWLinks^ Attachments {
   PDMWLinks^ get();
}
```

### Property Value

Collection of [links](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLinks.html) of non-SOLIDWORKS attachments for this SOLIDWORKS document

## VBA Syntax

See [PDMWDocument::Attachments](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~Attachments.html).

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
