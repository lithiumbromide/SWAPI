---
title: "ReleaseOwnership Method (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "ReleaseOwnership"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~ReleaseOwnership.html"
---

# ReleaseOwnership Method (IPDMWDocument)

Allows you to release ownership of a document.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReleaseOwnership() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As System.Integer

value = instance.ReleaseOwnership()
```

### C#

```csharp
System.int ReleaseOwnership()
```

### C++/CLI

```cpp
System.int ReleaseOwnership();
```

### Return Value

0 if successful, non-0 if not

## VBA Syntax

See [PDMWDocument::ReleaseOwnership](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~ReleaseOwnership.html).

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)
[IPDMWDocument::ChangeOwner Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~ChangeOwner.html)
[IPDMWDocument::TakeOwnership Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~TakeOwnership.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 SP3
