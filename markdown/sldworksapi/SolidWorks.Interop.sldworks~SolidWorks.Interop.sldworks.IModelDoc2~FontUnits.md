---
title: "FontUnits Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "FontUnits"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontUnits.html"
---

# FontUnits Method (IModelDoc2)

Changes font height (specified in current system units) in the selected notes, dimensions, and GTols.

## Syntax

### Visual Basic (Declaration)

```vb
Sub FontUnits( _
   ByVal Units As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Units As System.Double

instance.FontUnits(Units)
```

### C#

```csharp
void FontUnits(
   System.double Units
)
```

### C++/CLI

```cpp
void FontUnits(
   System.double Units
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Units`: Specifies the font height in current system units (for example, inches, millimeters, and so on)

## VBA Syntax

See [ModelDoc2::FontUnits](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~FontUnits.html).

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
[IModelDoc2::FontPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontPoints.html)
[IModelDoc2::FontUnderline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontUnderline.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
