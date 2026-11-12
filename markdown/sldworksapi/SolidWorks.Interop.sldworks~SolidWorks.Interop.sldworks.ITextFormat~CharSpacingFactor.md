---
title: "CharSpacingFactor Property (ITextFormat)"
project: "SOLIDWORKS API Help"
interface: "ITextFormat"
member: "CharSpacingFactor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~CharSpacingFactor.html"
---

# CharSpacingFactor Property (ITextFormat)

Gets or sets the factor that controls the spacing between characters.

## Syntax

### Visual Basic (Declaration)

```vb
Property CharSpacingFactor As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITextFormat
Dim value As System.Double

instance.CharSpacingFactor = value

value = instance.CharSpacingFactor
```

### C#

```csharp
System.double CharSpacingFactor {get; set;}
```

### C++/CLI

```cpp
property System.double CharSpacingFactor {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Factor that controls the spacing between characters

## VBA Syntax

See [TextFormat::CharSpacingFactor](ms-its:sldworksapivb6.chm::/sldworks~TextFormat~CharSpacingFactor.html).

## Examples

[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)
[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)

## Remarks

The character spacing factor for a piece of text is normally 1. To make the spacing between characters larger, increase this value; to make the spacing between characters smaller, decrease this value.

## See Also

[ITextFormat Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.html)
[ITextFormat Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision NUmber 10.0
