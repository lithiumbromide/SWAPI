---
title: "IsHeightSpecifiedInPts Method (ITextFormat)"
project: "SOLIDWORKS API Help"
interface: "ITextFormat"
member: "IsHeightSpecifiedInPts"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~IsHeightSpecifiedInPts.html"
---

# IsHeightSpecifiedInPts Method (ITextFormat)

Gets whether the character height is in points or system units.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsHeightSpecifiedInPts() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITextFormat
Dim value As System.Boolean

value = instance.IsHeightSpecifiedInPts()
```

### C#

```csharp
System.bool IsHeightSpecifiedInPts()
```

### C++/CLI

```cpp
System.bool IsHeightSpecifiedInPts();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the character height is in points, false if it is in system units

## VBA Syntax

See [TextFormat::IsHeightSpecifiedInPts](ms-its:sldworksapivb6.chm::/sldworks~TextFormat~IsHeightSpecifiedInPts.html).

## Examples

[Get All Elements in Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)
[Get Note Text Formatting Properties (VBA)](Get_Note_Text_Formatting_Properties_Example_VB.htm)
[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)

## Remarks

| If the font height was set using... | Then this method returns... |
| --- | --- |
| ITextFormat::CharHeight | False |
| ITextFormat::CharHeightInPts | True |

## See Also

[ITextFormat Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.html)
[ITextFormat Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat_members.html)
