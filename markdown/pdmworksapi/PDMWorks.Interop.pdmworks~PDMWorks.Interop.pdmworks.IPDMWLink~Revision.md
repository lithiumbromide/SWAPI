---
title: "Revision Property (IPDMWLink)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWLink"
member: "Revision"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink~Revision.html"
---

# Revision Property (IPDMWLink)

Gets the revision of the document associated with this link.

## Syntax

### Visual Basic (Declaration)

```vb
Property Revision As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWLink
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

Revision of the document associated with this link

## VBA Syntax

See [PDMWLink::Revision](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWLink~Revision.html).

## See Also

[IPDMWLink Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink.html)
[IPDMWLink Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink_members.html)
[IPDMWConnection::BumpRevision Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~BumpRevision.html)
[IPDMWConnection::Revision Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~Revision.html)
[IPDMWConnection::RevisionLabels Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~RevisionLabels.html)
[IPDMWConnection::Revisions Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~Revisions.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
