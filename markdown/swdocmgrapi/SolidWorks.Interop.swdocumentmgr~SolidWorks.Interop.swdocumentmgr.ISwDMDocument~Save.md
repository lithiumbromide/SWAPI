---
title: "Save Method (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "Save"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Save.html"
---

# Save Method (ISwDMDocument)

Saves the document.

## Syntax

### Visual Basic (Declaration)

```vb
Function Save() As SwDmDocumentSaveError
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
Dim value As SwDmDocumentSaveError

value = instance.Save()
```

### C#

```csharp
SwDmDocumentSaveError Save()
```

### C++/CLI

```cpp
SwDmDocumentSaveError Save();
```

### Return Value

Success or error code as defined by [SwDMDocumentSaveError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmDocumentSaveError.html)

## VBA Syntax

See [SwDMDocument::Save](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~Save.html).

## Remarks

This method returns an error if you try to save a read-only document.

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)
[ISwDMDocument::SaveAs Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~SaveAs.html)
[ISwDMDocument::LastSavedBy Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~LastSavedBy.html)
[ISwDMDocument::LastSavedDate Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~LastSavedDate.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
