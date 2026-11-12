---
title: "ModifyHyperLinkAt Method (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "ModifyHyperLinkAt"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~ModifyHyperLinkAt.html"
---

# ModifyHyperLinkAt Method (ISwDMDocument)

Sets the embedded hyperlink at the specified index for this document.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ModifyHyperLinkAt( _
   ByVal at As System.Integer, _
   ByVal newlink As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
Dim at As System.Integer
Dim newlink As System.String

instance.ModifyHyperLinkAt(at, newlink)
```

### C#

```csharp
void ModifyHyperLinkAt(
   System.int at,
   System.string newlink
)
```

### C++/CLI

```cpp
void ModifyHyperLinkAt(
   System.int at,
   System.String^ newlink
)
```

### Parameters

- `at`: 0-based index at which to set the embedded hyperlink
- `newlink`: New embedded hyperlink

## VBA Syntax

See [SwDMDocument::ModifyHyperLinkAt](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~ModifyHyperLinkAt.html).

## Remarks

Before calling this method, call [ISwDMDocument::GetHyperLinksCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetHyperLinksCount.html) to get the number of embedded hyperlinks for this document.

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)
[ISwDMDocument::GetHyperLinkAt Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetHyperLinkAt.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
