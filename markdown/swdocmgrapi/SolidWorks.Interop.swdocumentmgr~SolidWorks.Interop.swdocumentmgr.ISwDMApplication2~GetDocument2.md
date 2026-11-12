---
title: "GetDocument2 Method (ISwDMApplication2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMApplication2"
member: "GetDocument2"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication2~GetDocument2.html"
---

# GetDocument2 Method (ISwDMApplication2)

Gets the specified document from an IStream or IStorage storage.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDocument2( _
   ByVal documentStream As System.Object, _
   ByRef result As SwDmDocumentOpenError _
) As SwDMDocument
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMApplication2
Dim documentStream As System.Object
Dim result As SwDmDocumentOpenError
Dim value As SwDMDocument

value = instance.GetDocument2(documentStream, result)
```

### C#

```csharp
SwDMDocument GetDocument2(
   System.object documentStream,
   out SwDmDocumentOpenError result
)
```

### C++/CLI

```cpp
SwDMDocument^ GetDocument2(
   System.Object^ documentStream,
   [Out] SwDmDocumentOpenError result
)
```

### Parameters

- `documentStream`: Pointer to an unknown type, the IStream or IStorage storage
- `result`: Error as defined by [SwDmDocumentOpenError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmDocumentOpenError.html)

### Return Value

Pointer to the [ISwDMDocument](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument.html) object

## VBA Syntax

See [SwDMApplication2::GetDocument2](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMApplication2~GetDocument2.html).

## Remarks

Use [ISwDMApplication::GetDocument](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMApplication~GetDocument.html) to get a document using its name.

## See Also

[ISwDMApplication2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication2.html)
[ISwDMApplication2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication2_members.html)

## Availability

SOLIDWORKS Document Manager API 2007 SP3
