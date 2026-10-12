---
title: "ExtReferences Property (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "ExtReferences"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~ExtReferences.html"
---

# ExtReferences Property (IPDMWDocument)

Gets the links to external documents that this document references.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ExtReferences As PDMWLinks
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As PDMWLinks

value = instance.ExtReferences
```

### C#

```csharp
PDMWLinks ExtReferences {get;}
```

### C++/CLI

```cpp
property PDMWLinks^ ExtReferences {
   PDMWLinks^ get();
}
```

### Property Value

Collection of [links](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLinks.html) of external documents that this document references

## VBA Syntax

See [PDMWDocument::ExtReferences](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~ExtReferences.html).

## Remarks

An external document is any type of derived part, parent or child, including base, mirrored, and component parts.

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)
[IPDMWDocument::ExtWhereUsed Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~ExtWhereUsed.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
