---
title: "GetDocument Method (ISwDMComponent3)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMComponent3"
member: "GetDocument"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent3~GetDocument.html"
---

# GetDocument Method (ISwDMComponent3)

Obsolete. Superseded by [ISwDMComponent4::GetDocument2](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMComponent4~GetDocument2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDocument( _
   ByVal allowReadOnly As System.Boolean, _
   ByRef result As SwDmDocumentOpenError _
) As SwDMDocument
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMComponent3
Dim allowReadOnly As System.Boolean
Dim result As SwDmDocumentOpenError
Dim value As SwDMDocument

value = instance.GetDocument(allowReadOnly, result)
```

### C#

```csharp
SwDMDocument GetDocument(
   System.bool allowReadOnly,
   out SwDmDocumentOpenError result
)
```

### C++/CLI

```cpp
SwDMDocument^ GetDocument(
   System.bool allowReadOnly,
   [Out] SwDmDocumentOpenError result
)
```

### Parameters

- `allowReadOnly`: True to open the document as read-only, false as read-write
- `result`: Error as defined by [SwDmDocumentOpenError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmDocumentOpenError.html)

### Return Value

Pointer to the [ISwDMDocument](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument.html) object

## VBA Syntax

See [SwDMComponent3::GetDocument](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMComponent3~GetDocument.html).

## See Also

[ISwDMComponent3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent3.html)
[ISwDMComponent3 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent3_members.html)

## Availability

SOLIDWORKS Document Manager API 2008 FCS
