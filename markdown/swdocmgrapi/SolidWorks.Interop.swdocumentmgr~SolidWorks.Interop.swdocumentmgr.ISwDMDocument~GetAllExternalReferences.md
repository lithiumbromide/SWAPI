---
title: "GetAllExternalReferences Method (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "GetAllExternalReferences"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetAllExternalReferences.html"
---

# GetAllExternalReferences Method (ISwDMDocument)

Obsolete. Superseded by [ISwDMDocument5::GetAllExternalReferences2](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument5~GetAllExternalReferences2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAllExternalReferences( _
   ByVal pSrcOption As SwDMSearchOption _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
Dim pSrcOption As SwDMSearchOption
Dim value As System.Object

value = instance.GetAllExternalReferences(pSrcOption)
```

### C#

```csharp
System.object GetAllExternalReferences(
   SwDMSearchOption pSrcOption
)
```

### C++/CLI

```cpp
System.Object^ GetAllExternalReferences(
   SwDMSearchOption^ pSrcOption
)
```

### Parameters

- `pSrcOption`:

## VBA Syntax

See [SwDMDocument::GetAllExternalReferences](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~GetAllExternalReferences.html).

## Examples

[Open and Close Document (C++)](Open_and_Close_Document_Example_CPlusCPlus_COM.htm)

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)
[ISwDMDocument::WhereUsed Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~WhereUsed.html)
[ISwDMDocument::ReplaceReference Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~ReplaceReference.html)
[ISwDMDocument8::GetChangedReferences Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8~GetChangedReferences.html)
