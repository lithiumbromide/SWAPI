---
title: "BumpRevision Method (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "BumpRevision"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~BumpRevision.html"
---

# BumpRevision Method (IPDMWDocument)

Changes the revision number of the document.

## Syntax

### Visual Basic (Declaration)

```vb
Function BumpRevision( _
   ByVal i_cstrNewRev As System.String, _
   ByVal i_cstrNote As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim i_cstrNewRev As System.String
Dim i_cstrNote As System.String
Dim value As System.Integer

value = instance.BumpRevision(i_cstrNewRev, i_cstrNote)
```

### C#

```csharp
System.int BumpRevision(
   System.string i_cstrNewRev,
   System.string i_cstrNote
)
```

### C++/CLI

```cpp
System.int BumpRevision(
   System.String^ i_cstrNewRev,
   System.String^ i_cstrNote
)
```

### Parameters

- `i_cstrNewRev`: New revision number

  NOTE: If you specify an empty string for i_cstrNewRev, then the next logical revision is used.
- `i_cstrNote`: Note

### Return Value

0 on success, non-0 on failure

## VBA Syntax

See [PDMWDocument::BumpRevision](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~BumpRevision.html).

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)
[IPDMWDocument::Revision Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~Revision.html)
[IPDMWDocument::RevisionLabels Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~RevisionLabels.html)
[IPDMWLink::Revision Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink~Revision.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 SP4
