---
title: "CloseDoc Method (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "CloseDoc"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~CloseDoc.html"
---

# CloseDoc Method (ISwDMDocument)

Closes the document.

## Syntax

### Visual Basic (Declaration)

```vb
Sub CloseDoc()
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument

instance.CloseDoc()
```

### C#

```csharp
void CloseDoc()
```

### C++/CLI

```cpp
void CloseDoc();
```

## VBA Syntax

See [SwDMDocument::CloseDoc](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~CloseDoc.html).

## Examples

[Open and Close Document (C++)](Open_and_Close_Document_Example_CPlusCPlus_COM.htm)
[Get Drawing Sheets' Properties (C#)](Get_Drawing_Sheets_Properties_Example_CSharp.htm)
[Get Drawing Sheets' Properties (VB.NET)](Get_Drawing_Sheets_Properties_Example_vbnet.htm)

## Remarks

You must call this method to close a document before calling:

- [ISwDMApplication::CopyDocument](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~CopyDocument.html)
- [ISwDMApplication::MoveDocument](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~MoveDocument.html)

If you update a document, call this method to close it before attempting to create a new assembly with it.

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
