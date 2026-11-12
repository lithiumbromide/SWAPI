---
title: "TypeFaceName Property (ITextFormat)"
project: "SOLIDWORKS API Help"
interface: "ITextFormat"
member: "TypeFaceName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~TypeFaceName.html"
---

# TypeFaceName Property (ITextFormat)

Gets or sets the name of the font.

## Syntax

### Visual Basic (Declaration)

```vb
Property TypeFaceName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ITextFormat
Dim value As System.String

instance.TypeFaceName = value

value = instance.TypeFaceName
```

### C#

```csharp
System.string TypeFaceName {get; set;}
```

### C++/CLI

```cpp
property System.String^ TypeFaceName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the font

## VBA Syntax

See [TextFormat::TypeFaceName](ms-its:sldworksapivb6.chm::/sldworks~TextFormat~TypeFaceName.html).

## Examples

[Change Text Format (VBA)](Change_Text_Format_Example_VB.htm)
[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)
[Get Note Text Formatting Properties (VBA)](Get_Note_Text_Formatting_Properties_Example_VB.htm)
[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)

## See Also

[ITextFormat Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.html)
[ITextFormat Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat_members.html)
