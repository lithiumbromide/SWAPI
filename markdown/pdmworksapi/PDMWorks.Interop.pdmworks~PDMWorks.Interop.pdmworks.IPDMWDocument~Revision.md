---
title: "Revision Property (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "Revision"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~Revision.html"
---

# Revision Property (IPDMWDocument)

Gets the revision for this document.

## Syntax

### Visual Basic (Declaration)

```vb
Property Revision As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As System.String

instance.Revision = value

value = instance.Revision
```

### C#

```csharp
System.string Revision {get; set;}
```

### C++/CLI

```cpp
property System.String^ Revision {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Revision for this document

## VBA Syntax

See [PDMWDocument::Revision](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~Revision.html).

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)
[IPDMWDocument::BumpRevision Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~BumpRevision.html)
[IPDMWDocument::RevisionLabels Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~RevisionLabels.html)
[IPDMWDocument::Revisions Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~Revisions.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
