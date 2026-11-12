---
title: "MoveDocument Method (ISwDMApplication)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMApplication"
member: "MoveDocument"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~MoveDocument.html"
---

# MoveDocument Method (ISwDMApplication)

Moves a single document and optionally updates references to it.

## Syntax

### Visual Basic (Declaration)

```vb
Function MoveDocument( _
   ByVal fromName As System.String, _
   ByVal toName As System.String, _
   ByVal fromChildren As System.Object, _
   ByVal toChildren As System.Object, _
   ByVal option As System.Integer, _
   ByVal pSrcOption As SwDMSearchOption _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMApplication
Dim fromName As System.String
Dim toName As System.String
Dim fromChildren As System.Object
Dim toChildren As System.Object
Dim option As System.Integer
Dim pSrcOption As SwDMSearchOption
Dim value As System.Integer

value = instance.MoveDocument(fromName, toName, fromChildren, toChildren, option, pSrcOption)
```

### C#

```csharp
System.int MoveDocument(
   System.string fromName,
   System.string toName,
   System.object fromChildren,
   System.object toChildren,
   System.int option,
   SwDMSearchOption pSrcOption
)
```

### C++/CLI

```cpp
System.int MoveDocument(
   System.String^ fromName,
   System.String^ toName,
   System.Object^ fromChildren,
   System.Object^ toChildren,
   System.int option,
   SwDMSearchOption^ pSrcOption
)
```

### Parameters

- `fromName`: Full path and filename of the document to move
- `toName`: Full path and filename of the new document to which to move the document specified for fromName
- `fromChildren`: Array containing the full path and filenames of the child documents dependent on the document specified for fromName
- `toChildren`: Array containing the new full path and filenames for the child documents to which to move the documents specified for fromChildren
- `option`: Move options as defined by [SwDmCopyOptions](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmCopyOptions.html)
- `pSrcOption`: Pointer to an [ISwDMSearchOption](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMSearchOption.html) object

### Return Value

Success or error code as defined by [SwDmMoveCopyError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmMoveCopyError.html)

## VBA Syntax

See [SwDMApplication::MoveDocument](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMApplication~MoveDocument.html).

## Remarks

If a document is opened, you must call [ISwDMDocument::CloseDoc](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~CloseDoc.html) to close it before calling this method.

## See Also

[ISwDMApplication Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication.html)
[ISwDMApplication Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication_members.html)
[ISwDMApplication::CopyDocument Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~CopyDocument.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
