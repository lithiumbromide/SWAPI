---
title: "FontPoints Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "FontPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontPoints.html"
---

# FontPoints Method (IModelDoc2)

Changes the font height (specified in points) in the selected notes, dimensions, and GTols.

## Syntax

### Visual Basic (Declaration)

```vb
Sub FontPoints( _
   ByVal Points As System.Short _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Points As System.Short

instance.FontPoints(Points)
```

### C#

```csharp
void FontPoints(
   System.short Points
)
```

### C++/CLI

```cpp
void FontPoints(
   System.short Points
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Points`: Height, in points, of the font

## VBA Syntax

See [ModelDoc2::FontPoints](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~FontPoints.html).

## Examples

[Add Watermark to Part (C#)](Add_Watermark_to_Part_Example_CSharp.htm)
[Add Watermark to Part (VB.NET)](Add_Watermark_to_Part_Example_VBNET.htm)
[Add Watermark to Part (VBA)](Add_Watermark_to_Part_Example_VB.htm)

## Remarks

You can also use [ITextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat.html) for full control of text formatting. Obtain ITextFormat using the appropriate GetTextFormat method (see index entry GetTextFormat for a list of available GetTextFormat methods).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::FontBold Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontBold.html)
[IModelDoc2::FontFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontFace.html)
[IModelDoc2::FontItalic Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontItalic.html)
[IModelDoc2::FontUnderline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontUnderline.html)
[IModelDoc2::FontUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontUnits.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
