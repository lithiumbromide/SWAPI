---
title: "ExtWhereUsed Property (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "ExtWhereUsed"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~ExtWhereUsed.html"
---

# ExtWhereUsed Property (IPDMWDocument)

Gets the links to external document that reference this document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ExtWhereUsed As PDMWLinks
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As PDMWLinks

value = instance.ExtWhereUsed
```

### C#

```csharp
PDMWLinks ExtWhereUsed {get;}
```

### C++/CLI

```cpp
property PDMWLinks^ ExtWhereUsed {
   PDMWLinks^ get();
}
```

### Property Value

Collection of [links](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLinks.html) of external documents that reference this document

## VBA Syntax

See [PDMWDocument::ExtWhereUsed](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~ExtWhereUsed.html).

## Remarks

An external document is any type of derived part, parent or child, including base, mirrored, and component parts.

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)
[IPDMWDocument::ExtReferences Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~ExtReferences.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
