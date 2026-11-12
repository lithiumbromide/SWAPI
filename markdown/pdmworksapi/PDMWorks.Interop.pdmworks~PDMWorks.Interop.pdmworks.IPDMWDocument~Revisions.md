---
title: "Revisions Property (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "Revisions"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~Revisions.html"
---

# Revisions Property (IPDMWDocument)

Gets all of the revisions of this document, in order from the oldest to newest.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Revisions As PDMWDocuments
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As PDMWDocuments

value = instance.Revisions
```

### C#

```csharp
PDMWDocuments Revisions {get;}
```

### C++/CLI

```cpp
property PDMWDocuments^ Revisions {
   PDMWDocuments^ get();
}
```

### Property Value

Collection of the revisions of this [document](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocuments.html)

## VBA Syntax

See [PDMWDocument::Revisions](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~Revisions.html).

## Remarks

The collection returned is indexed by number as well as revision, but not by the name of the document. Therefore, the following is possible:

```vb
' VBA
' Given a PDMWDocuments collection called doc
dim doc2 as PDMWDocument
Dim revs As PDMWDocuments
Set revs = doc.Revisions
Set doc2 = revs ('01')  ' Pass a revision name string as an argument
```

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)
[IPDMWDocument::BumpRevision Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~BumpRevision.html)
[IPDMWDocument::Revision Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~Revision.html)
[IPDMWDocument::RevisionLabels Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~RevisionLabels.html)
[IPDMWLink::Revision Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink~Revision.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
