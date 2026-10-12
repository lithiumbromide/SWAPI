---
title: "Italic Property (ITextFormat)"
project: "SOLIDWORKS API Help"
interface: "ITextFormat"
member: "Italic"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~Italic.html"
---

# Italic Property (ITextFormat)

Gets or sets the whether the text format is italic.

## Syntax

### Visual Basic (Declaration)

```vb
Property Italic As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITextFormat
Dim value As System.Boolean

instance.Italic = value

value = instance.Italic
```

### C#

```csharp
System.bool Italic {get; set;}
```

### C++/CLI

```cpp
property System.bool Italic {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the text is italic, false otherwise

## VBA Syntax

See [TextFormat::Italic](ms-its:sldworksapivb6.chm::/sldworks~TextFormat~Italic.html).

## Examples

[Change Text Format (VBA)](Change_Text_Format_Example_VB.htm)
[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)
[Get Format of Note Text (VBA)](Get_Format_of_Note_Text_Example_VB.htm)
[Get Note Text Formatting Properties (VBA)](Get_Note_Text_Formatting_Properties_Example_VB.htm)
[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)

## See Also

[ITextFormat Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.html)
[ITextFormat Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat_members.html)
