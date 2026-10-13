---
title: "GetSize Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "GetSize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetSize.html"
---

# GetSize Method (ISheet)

Gets the size of the sheet and the corresponding standard sheet size.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSize( _
   ByRef Width As System.Double, _
   ByRef Height As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim Width As System.Double
Dim Height As System.Double
Dim value As System.Integer

value = instance.GetSize(Width, Height)
```

### C#

```csharp
System.int GetSize(
   out System.double Width,
   out System.double Height
)
```

### C++/CLI

```cpp
System.int GetSize(
   [Out] System.double Width,
   [Out] System.double Height
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Width`: Width of sheet
- `Height`: Height of sheet

### Return Value

Paper size as defined in [swDwgPaperSizes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html)

## VBA Syntax

See [Sheet::GetSize](ms-its:sldworksapivb6.chm::/sldworks~Sheet~GetSize.html).

## Examples

[Get the Number of Lines Flat-pattern Drawing View's Boundary-box Sketch (C#)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_CSharp.htm)
[Get the Number of Lines Flat-pattern Drawing View's Boundary-box Sketch (VB.NET)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_VBNET.htm)
[Get the Number of Lines Flat-pattern Drawing View's Boundary-box Sketch (VBA)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_VB.htm)

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[ISheet::GetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetProperties.html)
[ISheet::IGetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IGetProperties.html)
[ISheet::SetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetProperties.html)
[ISheet::SetSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetSize.html)
[ISheet::IPageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IPageSetup.html)
[ISheet::PageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~PageSetup.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
