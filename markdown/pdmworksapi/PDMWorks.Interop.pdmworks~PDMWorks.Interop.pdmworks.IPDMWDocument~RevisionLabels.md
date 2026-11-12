---
title: "RevisionLabels Property (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "RevisionLabels"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~RevisionLabels.html"
---

# RevisionLabels Property (IPDMWDocument)

Gets the next suggested revisions for the document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property RevisionLabels As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As System.Object

value = instance.RevisionLabels
```

### C#

```csharp
System.object RevisionLabels {get;}
```

### C++/CLI

```cpp
property System.Object^ RevisionLabels {
   System.Object^ get();
}
```

### Property Value

Revisions

## VBA Syntax

See [PDMWDocument::RevisionLabels](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~RevisionLabels.html).

## Requirements

For example, if the current revision labels are PRE-01, DEV-01, and REL-01, the next suggested revision labels would be PRE-02, DEV-02, and REL-02.

Call this property before calling [IPDMWConnection::Checkin](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~CheckIn.html).

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)
[IPDMWDocument::BumpRevision Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~BumpRevision.html)
[IPDMWDocument::Revision Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~Revision.html)
[IPDMWDocument::Revisions Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~Revisions.html)

## Availability

SOLIDWORKS Workgroup PDM 2005 FCS
