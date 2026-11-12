---
title: "SaveAs Method (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "SaveAs"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~SaveAs.html"
---

# SaveAs Method (ISwDMDocument)

Saves the document as the specified filename.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveAs( _
   ByVal saveName As System.String _
) As SwDmDocumentSaveError
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
Dim saveName As System.String
Dim value As SwDmDocumentSaveError

value = instance.SaveAs(saveName)
```

### C#

```csharp
SwDmDocumentSaveError SaveAs(
   System.string saveName
)
```

### C++/CLI

```cpp
SwDmDocumentSaveError SaveAs(
   System.String^ saveName
)
```

### Parameters

- `saveName`: Filename to which to save the document

### Return Value

Success or error code as defined by [SwDMDocumentSaveError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmDocumentSaveError.html)

## VBA Syntax

See [SwDMDocument::SaveAs](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~SaveAs.html).

## Remarks

A read-only document saved as a different file results in the new file being read-write.

This method lets you save a file to a different filename; this method does not let you save a file to a different file type.

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)
[ISwDMDocument::Save Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Save.html)
[ISwDMDocument::LastSavedBy Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~LastSavedBy.html)
[ISwDMDocument::LastSavedDate Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~LastSavedDate.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
