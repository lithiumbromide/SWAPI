---
title: "ChangeOwner Method (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "ChangeOwner"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~ChangeOwner.html"
---

# ChangeOwner Method (IPDMWDocument)

Changes the document's owner.

## Syntax

### Visual Basic (Declaration)

```vb
Function ChangeOwner( _
   ByVal Owner As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim Owner As System.String
Dim value As System.Integer

value = instance.ChangeOwner(Owner)
```

### C#

```csharp
System.int ChangeOwner(
   System.string Owner
)
```

### C++/CLI

```cpp
System.int ChangeOwner(
   System.String^ Owner
)
```

### Parameters

- `Owner`: Name of new document owner

### Return Value

0 on success, non-0 on failure

## VBA Syntax

See [PDMWDocument::ChangeOwner](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~ChangeOwner.html).

## Remarks

This functionality is only available via the SOLIDWORKS Workgroup PDM API; it is not available in the user interface. Only vault administrators can use this method.

This method does not release ownership of any child documents. Use [IPDMWDocument::ReleaseOwnership](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~ReleaseOwnership.html) to do this.

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)
[IPDMWDocument::ReleaseOwnership Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~ReleaseOwnership.html)
[IPDMWDocument::TakeOwnership Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~TakeOwnership.html)

## Availability

SOLIDWORKS Workgroup PDM 2005 FCS
