---
title: "TakeOwnership Method (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "TakeOwnership"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~TakeOwnership.html"
---

# TakeOwnership Method (IPDMWDocument)

Allows you to take ownership of a document.

## Syntax

### Visual Basic (Declaration)

```vb
Function TakeOwnership() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As System.Integer

value = instance.TakeOwnership()
```

### C#

```csharp
System.int TakeOwnership()
```

### C++/CLI

```cpp
System.int TakeOwnership();
```

### Return Value

0 if successful, an exception is thrown if not (see Remarks)

## VBA Syntax

See [PDMWDocument::TakeOwnership](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~TakeOwnership.html).

## Remarks

Before you can check a document in, you must own it. See [IPDMWConnection::Checkin](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~CheckIn.html) for details about checking in documents.

If a call to this method fails, the Document ownership was denied exception is thrown. You can trap this exception using a try/catch block in C# or C++, or On Error in VB.

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)
[IPDMWDocument::ChangeOwner Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~ChangeOwner.html)
[IPDMWDocument::ReleaseOwnership Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~ReleaseOwnership.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
