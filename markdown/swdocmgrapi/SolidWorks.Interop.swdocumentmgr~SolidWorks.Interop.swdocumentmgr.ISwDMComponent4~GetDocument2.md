---
title: "GetDocument2 Method (ISwDMComponent4)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMComponent4"
member: "GetDocument2"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent4~GetDocument2.html"
---

# GetDocument2 Method (ISwDMComponent4)

Gets this component's document using the specified search options.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDocument2( _
   ByVal allowReadOnly As System.Boolean, _
   ByVal pSrcOption As SwDMSearchOption, _
   ByRef result As SwDmDocumentOpenError _
) As SwDMDocument
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMComponent4
Dim allowReadOnly As System.Boolean
Dim pSrcOption As SwDMSearchOption
Dim result As SwDmDocumentOpenError
Dim value As SwDMDocument

value = instance.GetDocument2(allowReadOnly, pSrcOption, result)
```

### C#

```csharp
SwDMDocument GetDocument2(
   System.bool allowReadOnly,
   SwDMSearchOption pSrcOption,
   out SwDmDocumentOpenError result
)
```

### C++/CLI

```cpp
SwDMDocument^ GetDocument2(
   System.bool allowReadOnly,
   SwDMSearchOption^ pSrcOption,
   [Out] SwDmDocumentOpenError result
)
```

### Parameters

- `allowReadOnly`: True to open the document as read-only, false as read-write
- `pSrcOption`: [Search options](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMSearchOption.html)
- `result`: Error as defined by [ISwDMDocumentOpenError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmDocumentOpenError.html)

### Return Value

[ISwDMDocument](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument.html)

## VBA Syntax

See [SwDMComponent4::GetDocument2](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMComponent4~GetDocument2.html).

## See Also

[ISwDMComponent4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent4.html)
[ISwDMComponent4 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent4_members.html)

## Availability

SOLIDWORKS Document Manager API 2008 SP1
