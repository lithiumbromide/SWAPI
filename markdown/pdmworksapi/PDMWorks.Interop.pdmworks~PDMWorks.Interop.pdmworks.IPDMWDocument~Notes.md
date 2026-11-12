---
title: "Notes Property (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "Notes"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~Notes.html"
---

# Notes Property (IPDMWDocument)

Gets the notes associated with this document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Notes As PDMWDocumentNotes
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As PDMWDocumentNotes

value = instance.Notes
```

### C#

```csharp
PDMWDocumentNotes Notes {get;}
```

### C++/CLI

```cpp
property PDMWDocumentNotes^ Notes {
   PDMWDocumentNotes^ get();
}
```

### Property Value

Collection of [notes](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocumentNotes.html) associated with this document

## VBA Syntax

See [PDMWDocument::Notes](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~Notes.html).

## Remarks

Notes are ordered from oldest to newest.

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)
[IPDMWDocument::AddNote Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~AddNote.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
