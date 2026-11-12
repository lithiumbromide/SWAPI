---
title: "FontBold Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "FontBold"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontBold.html"
---

# FontBold Method (IModelDoc2)

Enables or disables bold font style in the selected notes, dimensions, and GTols.

## Syntax

### Visual Basic (Declaration)

```vb
Sub FontBold( _
   ByVal Bold As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Bold As System.Boolean

instance.FontBold(Bold)
```

### C#

```csharp
void FontBold(
   System.bool Bold
)
```

### C++/CLI

```cpp
void FontBold(
   System.bool Bold
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Bold`: True to enable bold font style, false to disable it

## VBA Syntax

See [ModelDoc2::FontBold](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~FontBold.html).

## Remarks

You can also use [ITextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat.html) for full control of text formatting. Obtain ITextFormat using the appropriate GetTextFormat method (see index entry GetTextFormat for a list of available GetTextFormat methods).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::FontFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontFace.html)
[IModelDoc2::FontItalic Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontItalic.html)
[IModelDoc2::FontPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontPoints.html)
[IModelDoc2::FontUnderline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontUnderline.html)
[IModelDoc2::FontUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontUnits.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
