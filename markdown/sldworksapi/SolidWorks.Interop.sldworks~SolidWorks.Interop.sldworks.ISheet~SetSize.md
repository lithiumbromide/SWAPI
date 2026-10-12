---
title: "SetSize Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "SetSize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetSize.html"
---

# SetSize Method (ISheet)

Sets the standard sheet size and the size of the sheet so that the drawing looks correct.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSize( _
   ByVal Size As System.Integer, _
   ByVal Width As System.Double, _
   ByVal Height As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim Size As System.Integer
Dim Width As System.Double
Dim Height As System.Double
Dim value As System.Boolean

value = instance.SetSize(Size, Width, Height)
```

### C#

```csharp
System.bool SetSize(
   System.int Size,
   System.double Width,
   System.double Height
)
```

### C++/CLI

```cpp
System.bool SetSize(
   System.int Size,
   System.double Width,
   System.double Height
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Size`: Paper size as defined in [swDwgPaperSizes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html)
- `Width`: Width of sheet
- `Height`: Height of sheet

### Return Value

True if the size of the sheet is set, false if not

## VBA Syntax

See [Sheet::SetSize](ms-its:sldworksapivb6.chm::/sldworks~Sheet~SetSize.html).

## Examples

[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)
[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[ISheet::GetSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetSize.html)
[ISheet::GetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetProperties.html)
[ISheet::PageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~PageSetup.html)
[ISheet::IPageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IPageSetup.html)
[ISheet::SetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetProperties.html)
[ISheet::IGetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IGetProperties.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
