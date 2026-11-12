---
title: "WhereUsed Method (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "WhereUsed"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~WhereUsed.html"
---

# WhereUsed Method (ISwDMDocument)

Gets the names of the files that reference this document using the specified search options.

## Syntax

### Visual Basic (Declaration)

```vb
Function WhereUsed( _
   ByVal pSrcOption As SwDMSearchOption _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
Dim pSrcOption As SwDMSearchOption
Dim value As System.Object

value = instance.WhereUsed(pSrcOption)
```

### C#

```csharp
System.object WhereUsed(
   SwDMSearchOption pSrcOption
)
```

### C++/CLI

```cpp
System.Object^ WhereUsed(
   SwDMSearchOption^ pSrcOption
)
```

### Parameters

- `pSrcOption`: [ISwDMSearchOption](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMSearchOption.html)

### Return Value

Array of the names of the files that reference this document

## VBA Syntax

See [SwDMDocument::WhereUsed](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~WhereUsed.html).

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)
[ISwDMDocument::ReplaceReference Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~ReplaceReference.html)
[ISwDMDocument8::GetChangedReferences Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8~GetChangedReferences.html)
[ISwDMDocument5::GetAllExternalReferences2 Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5~GetAllExternalReferences2.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
