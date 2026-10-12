---
title: "GetHyperLinksCount Method (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "GetHyperLinksCount"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetHyperLinksCount.html"
---

# GetHyperLinksCount Method (ISwDMDocument)

Gets the number of embedded hyperlinks for this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetHyperLinksCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
Dim value As System.Integer

value = instance.GetHyperLinksCount()
```

### C#

```csharp
System.int GetHyperLinksCount()
```

### C++/CLI

```cpp
System.int GetHyperLinksCount();
```

### Return Value

Number of embedded hyperlinks

## VBA Syntax

See [SwDMDocument::GetHyperLinksCount](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~GetHyperLinksCount.html).

## Examples

[Get Hyperlinks (C#)](Get_Hyperlinks_Example_CSharp.htm)
[Get Hyperlinks (VB.NET)](Get_Hyperlinks_Example_VBNET.htm)

## Remarks

Call this method before calling [ISwDMDocument::GetHyperLinkAt](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetHyperLinkAt.html) and [ISwDMDocument::ModifyHyperLinkAt](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~ModifyHyperLinkAt.html).

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
