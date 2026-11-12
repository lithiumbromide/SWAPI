---
title: "SetBulletsAndNumbering Method (IParagraphs)"
project: "SOLIDWORKS API Help"
interface: "IParagraphs"
member: "SetBulletsAndNumbering"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~SetBulletsAndNumbering.html"
---

# SetBulletsAndNumbering Method (IParagraphs)

Sets the list properties of the current paragraph.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetBulletsAndNumbering( _
   ByVal ParagraphType As System.Integer, _
   ByVal NumberingType As System.Integer, _
   ByVal StartAt As System.Integer, _
   ByVal Type As System.Integer, _
   ByVal Format As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IParagraphs
Dim ParagraphType As System.Integer
Dim NumberingType As System.Integer
Dim StartAt As System.Integer
Dim Type As System.Integer
Dim Format As System.Integer
Dim value As System.Boolean

value = instance.SetBulletsAndNumbering(ParagraphType, NumberingType, StartAt, Type, Format)
```

### C#

```csharp
System.bool SetBulletsAndNumbering(
   System.int ParagraphType,
   System.int NumberingType,
   System.int StartAt,
   System.int Type,
   System.int Format
)
```

### C++/CLI

```cpp
System.bool SetBulletsAndNumbering(
   System.int ParagraphType,
   System.int NumberingType,
   System.int StartAt,
   System.int Type,
   System.int Format
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ParagraphType`: List type as defined in [swParagraphType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swParagraphType_e.html)
- `NumberingType`: Numbering direction as defined in [swNumberedListStartType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swNumberedListStartType_e.html); valid only if ParagraphType is swParagraphType_e.swParagraphNumbered
- `StartAt`: Letter or number starting this numbered list, depending on Type; valid only if ParagraphType is swParagraphType_e.swParagraphNumbered
- `Type`: Numbered list type as defined in [swNumberedListType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swNumberedListType_e.html); valid only if ParagraphType is swParagraphType_e.swParagraphNumbered
- `Format`: Numbered list format as defined in [swNumberingFormat_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNumberingFormat_e.html); valid only if ParagraphType is swParagraphType_e.swParagraphNumbered

### Return Value

True if successful, false if not

## VBA Syntax

See [Paragraphs::SetBulletsAndNumbering](ms-its:sldworksapivb6.chm::/sldworks~Paragraphs~SetBulletsAndNumbering.html).

## Remarks

Before calling this method, set the current paragraph using [IParagraphs::CurrentParagraph](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~CurrentParagraph.html).

After calling this method, call [IParagraphs::UpdateParagraph](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~UpdateParagraph.html) to update the model.

## See Also

[IParagraphs Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.html)
[IParagraphs Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs_members.html)
[IParagraphs::GetBulletsAndNumbering Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetBulletsAndNumbering.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
