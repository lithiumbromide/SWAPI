---
title: "CreationDate2 Property (ISwDMDocument19)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument19"
member: "CreationDate2"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~CreationDate2.html"
---

# CreationDate2 Property (ISwDMDocument19)

Gets the date in numeric format that this document was created.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CreationDate2 As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument19
Dim value As System.Integer

value = instance.CreationDate2
```

### C#

```csharp
System.int CreationDate2 {get;}
```

### C++/CLI

```cpp
property System.int CreationDate2 {
   System.int get();
}
```

### Property Value

Date in numeric format that this document was created

## VBA Syntax

See [SwDMDocument19::CreationDate2](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument19~CreationDate2.html).

## Examples

[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)

## Remarks

To get the creation date in string format that this document was created, use [ISwDMDocument::CreationDate](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~CreationDate.html).

## See Also

[ISwDMDocument19 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19.html)
[ISwDMDocument19 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19_members.html)
[ISwDMDocument::Author Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Author.html)
[ISwDMDocument::Comments Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Comments.html)
[ISwDMDocument::Keywords Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Keywords.html)
[ISwDMDocument::LastSavedBy Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~LastSavedBy.html)
[ISwDMDocument::LastSavedDate Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~LastSavedDate.html)
[ISwDMDocument19::LastSavedDate2 Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~LastSavedDate2.html)
[ISwDMDocument::Subject Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Subject.html)
[ISwDMDocument::Title Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Title.html)

## Availability

SOLIDWORKS Document Manager API 2015 FCS
