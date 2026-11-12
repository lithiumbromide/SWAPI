---
title: "LastSavedBy Property (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "LastSavedBy"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~LastSavedBy.html"
---

# LastSavedBy Property (ISwDMDocument)

Gets the name of the person who last saved this document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property LastSavedBy As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
Dim value As System.String

value = instance.LastSavedBy
```

### C#

```csharp
System.string LastSavedBy {get;}
```

### C++/CLI

```cpp
property System.String^ LastSavedBy {
   System.String^ get();
}
```

### Property Value

Name of the person who last saved this document

## VBA Syntax

See [SwDMDocument::LastSavedBy](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~LastSavedBy.html).

## Examples

[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)
[ISwDocument::Author Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Author.html)
[ISwDocument::Comments Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Comments.html)
[ISwDocument::CreationDate Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~CreationDate.html)
[ISwDMDocument19::CreationDate2 Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~CreationDate2.html)
[ISwDocument::FullName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~FullName.html)
[ISwDocument::Keywords Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Keywords.html)
[ISwDocument::LastSavedDate Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~LastSavedDate.html)
[ISwDMDocument19::LastSavedDate2 Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~LastSavedDate2.html)
[ISwDocument::Subject Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Subject.html)
[ISwDocument::Title Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Title.html)
[ISwDocument::Save Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Save.html)
[ISwDocument::SaveAs Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~SaveAs.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
