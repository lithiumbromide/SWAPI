---
title: "Author Property (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "Author"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Author.html"
---

# Author Property (ISwDMDocument)

Gets or sets the name of the person who authored this document.

## Syntax

### Visual Basic (Declaration)

```vb
Property Author As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
Dim value As System.String

instance.Author = value

value = instance.Author
```

### C#

```csharp
System.string Author {get; set;}
```

### C++/CLI

```cpp
property System.String^ Author {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Author of document

## VBA Syntax

See [SwDMDocument::Author](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~Author.html).

## Examples

[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)
[ISwDMDocument::Comments Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Comments.html)
[ISwDMDocument::CreationDate Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~CreationDate.html)
[ISwDMDocument19::CreationDate2 Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~CreationDate2.html)
[ISwDMDocument::Keywords Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Keywords.html)
[ISwDMDocument::LastSavedBy Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~LastSavedBy.html)
[ISwDMDocument::LastSavedDate Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~LastSavedDate.html)
[ISwDMDocument19::LastSavedDate2 Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~LastSavedDate2.html)
[ISwDMDocument::Subject Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Subject.html)
[ISwDMDocument::Title Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Title.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
