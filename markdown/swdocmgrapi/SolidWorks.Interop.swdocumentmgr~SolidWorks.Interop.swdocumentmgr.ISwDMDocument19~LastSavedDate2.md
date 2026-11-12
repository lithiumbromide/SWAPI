---
title: "LastSavedDate2 Property (ISwDMDocument19)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument19"
member: "LastSavedDate2"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~LastSavedDate2.html"
---

# LastSavedDate2 Property (ISwDMDocument19)

Gets the date in numeric format that this document was last saved.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property LastSavedDate2 As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument19
Dim value As System.Integer

value = instance.LastSavedDate2
```

### C#

```csharp
System.int LastSavedDate2 {get;}
```

### C++/CLI

```cpp
property System.int LastSavedDate2 {
   System.int get();
}
```

### Property Value

Date in numeric format that this document was last saved

## VBA Syntax

See [SwDMDocument19::LastSavedDate2](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument19~LastSavedDate2.html).

## Examples

[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)

## Remarks

To get the date in string format that this document was last saved, use [ISwDMDocument::LastSavedDate](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~LastSavedDate.html).

## See Also

[ISwDMDocument19 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19.html)
[ISwDMDocument19 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19_members.html)
[ISwDMDocument::Author Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Author.html)
[ISwDMDocument::Comments Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Comments.html)
[ISwDMDocument::CreationDate Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~CreationDate.html)
[ISwDMDocument19::CreationDate2 Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~CreationDate2.html)
[ISwDMDocument::LastSavedBy Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~LastSavedBy.html)
[ISwDMDocument::Subject Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Subject.html)
[ISwDMDocument::Title Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Title.html)
[ISwDMDocument::Keywords Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Keywords.html)

## Availability

SOLIDWORKS Document Manager API 2015 FCS
