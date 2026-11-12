---
title: "FontItalic Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "FontItalic"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontItalic.html"
---

# FontItalic Method (IModelDoc2)

Enables or disables italic font style in the selected notes, dimensions, and GTols.

## Syntax

### Visual Basic (Declaration)

```vb
Sub FontItalic( _
   ByVal Italic As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Italic As System.Boolean

instance.FontItalic(Italic)
```

### C#

```csharp
void FontItalic(
   System.bool Italic
)
```

### C++/CLI

```cpp
void FontItalic(
   System.bool Italic
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Italic`: True to enable italic font style, false to disable

## VBA Syntax

See [ModelDoc2::FontItalic](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~FontItalic.html).

## Remarks

You can also use [ITextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat.html) for full control of text formatting. Obtain ITextFormat using the appropriate GetTextFormat method (see index entry GetTextFormat for a list of available GetTextFormat methods).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::FontBold Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontBold.html)
[IModelDoc2::FontFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontFace.html)
[IModelDoc2::FontPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontPoints.html)
[IModelDoc2::FontUnderline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontUnderline.html)
[IModelDoc2::FontUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontUnits.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
