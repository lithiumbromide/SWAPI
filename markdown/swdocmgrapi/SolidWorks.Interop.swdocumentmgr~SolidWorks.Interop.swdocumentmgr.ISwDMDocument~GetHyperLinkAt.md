---
title: "GetHyperLinkAt Method (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "GetHyperLinkAt"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetHyperLinkAt.html"
---

# GetHyperLinkAt Method (ISwDMDocument)

Gets the embedded hyperlinks at the specified index for this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetHyperLinkAt( _
   ByVal at As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
Dim at As System.Integer
Dim value As System.String

value = instance.GetHyperLinkAt(at)
```

### C#

```csharp
System.string GetHyperLinkAt(
   System.int at
)
```

### C++/CLI

```cpp
System.String^ GetHyperLinkAt(
   System.int at
)
```

### Parameters

- `at`: 0-based index at which to get the embedded hyperlinks

### Return Value

Hyperlinks

## VBA Syntax

See [SwDMDocument::GetHyperLinkAt](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~GetHyperLinkAt.html).

## Examples

[Get Hyperlinks (C#)](Get_Hyperlinks_Example_CSharp.htm)
[Get Hyperlinks (VB.NET)](Get_Hyperlinks_Example_VBNET.htm)

## Remarks

Before calling this method, call [ISwDMDocument::GetHyperLinksCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetHyperLinksCount.html) to get the number of embedded hyperlinks associated with this document.

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)
[ISwDMDocument::ModifyHyperLinkAt Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~ModifyHyperLinkAt.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
