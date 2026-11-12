---
title: "LastSavedDate Property (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "LastSavedDate"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~LastSavedDate.html"
---

# LastSavedDate Property (ISwDMDocument)

Gets the date in string format that this document was last saved.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property LastSavedDate As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
Dim value As System.String

value = instance.LastSavedDate
```

### C#

```csharp
System.string LastSavedDate {get;}
```

### C++/CLI

```cpp
property System.String^ LastSavedDate {
   System.String^ get();
}
```

### Property Value

Date in string format that this document was last saved

## VBA Syntax

See [SwDMDocument::LastSavedDate](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~LastSavedDate.html).

## Examples

[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)

## Remarks

To get the date in numeric format that this document was last saved, use [ISwDMDocument19::LastSaveDate2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~LastSavedDate2.html).

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)
[ISwDMDocument::Author Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Author.html)
[ISwDMDocument::Comments Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Comments.html)
[ISwDMDocument::CreationDate Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~CreationDate.html)
[ISwDMDocument19::CreationDate2 Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~CreationDate2.html)
[ISwDMDocument::FullName Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~FullName.html)
[ISwDMDocument::Keywords Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Keywords.html)
[ISwDMDocument::LastSavedBy Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~LastSavedBy.html)
[ISwDMDocument::Subject Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Subject.html)
[ISwDMDocument::Title Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Title.html)
[ISwDMDocument::Save Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Save.html)
[ISwDMDocument::SaveAs Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~SaveAs.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
