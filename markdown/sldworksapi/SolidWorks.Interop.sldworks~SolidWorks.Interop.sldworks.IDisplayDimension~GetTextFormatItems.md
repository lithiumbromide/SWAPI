---
title: "GetTextFormatItems Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetTextFormatItems"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetTextFormatItems.html"
---

# GetTextFormatItems Method (IDisplayDimension)

Gets the format tokens of the specified text portion of a multi-value display dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextFormatItems( _
   ByVal WhichText As System.Integer, _
   ByRef TokensDefinition As System.Object, _
   ByRef TokensEvaluated As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim WhichText As System.Integer
Dim TokensDefinition As System.Object
Dim TokensEvaluated As System.Object
Dim value As System.Integer

value = instance.GetTextFormatItems(WhichText, TokensDefinition, TokensEvaluated)
```

### C#

```csharp
System.int GetTextFormatItems(
   System.int WhichText,
   out System.object TokensDefinition,
   out System.object TokensEvaluated
)
```

### C++/CLI

```cpp
System.int GetTextFormatItems(
   System.int WhichText,
   [Out] System.Object^ TokensDefinition,
   [Out] System.Object^ TokensEvaluated
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichText`: Portion of the display dimension text as defined in [swDimensionTextParts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionTextParts_e.html)
- `TokensDefinition`: Array of strings containing format symbols for the text portion specified in WhichText
- `TokensEvaluated`: Array of strings containing evaluations of symbols in TokensDefinition

### Return Value

Size of returned arrays

## VBA Syntax

See [DisplayDimension::GetTextFormatItems](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetTextFormatItems.html).

## Examples

[Get Chamfer Display Dimension (C#)](Get_Chamfer_Display_Dimension_Example_CSharp.htm)
[Get Chamfer Display Dimension (VB.NET)](Get_Chamfer_Display_Dimension_Example_VBNET.htm)
[Get Chamfer Display Dimension (VBA)](Get_Chamfer_Display_Dimension_Example_VB.htm)

## Remarks

Each display dimension's PropertyManager page contains a section called Dimension Text that specifies the format of the displayed dimension. The format consists of function symbols or tokens enclosed within angle brackets (e.g., <DIM>), each of which connotes the function or definition of the value symbols that follow it.

This method retrieves all of the symbols, both function and value, for the portion of the display dimension text specified by WhichText. It also retrieves values for any symbols that can be evaluated in TokensDefinition.

**NOTE:** This method does not support [hole callouts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsHoleCallout.html).

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetText.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
