---
title: "GetNext3 Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "GetNext3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetNext3.html"
---

# GetNext3 Method (IAnnotation)

Gets the next annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNext3() As Annotation
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As Annotation

value = instance.GetNext3()
```

### C#

```csharp
Annotation GetNext3()
```

### C++/CLI

```cpp
Annotation^ GetNext3();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html)

## VBA Syntax

See [Annotation::GetNext3](ms-its:sldworksapivb6.chm::/sldworks~Annotation~GetNext3.html).

## Examples

[Get Display Dimensions, GTols, and Surface-finish Symbols (VBA)](Get_Display_Dimensions,_Gtols,_and_Surface-Finish_Symbols_Example_VB.htm)
[Get Entities Attached to Cosmetic Thread (VBA)](Get_Entities_Attached_To_Cosmetic_Thread_Example_VB.htm)
[Show Dimensions in Drawing Sheet (VBA)](Show_Dimensions_in_Drawing_Sheet_Example_VB.htm)
[Get DimXpert Display Dimensions and Feature (C#)](Get_DimXpert_Display_Dimensions_and_Feature_Example_CSharp.htm)
[Get DimXpert Display Dimensions and Feature (VB.NET)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VBNET.htm)
[Get DimXpert Display Dimensions and Feature (VBA)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VB.htm)

## Remarks

This method:

- retrieves all display dimensions, including suppressed, hidden, and dangling dimensions, on the sheet and on the sheet format if it is visible. See [ISheet::SheetFormatVisible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet~SheetFormatVisible.html) for details.
- retrieves all instances of a dimension. For example, if a (4X) instance dimension is visible in the user interface, this method gets the 4X dimension and each of its four dimension instances.
- retrieves an annotation, even if it is on a layer that is not displayed.

A dimension is suppressed or hidden when you:

- specifically select a dimension and hide it.

  - or -
- select a feature and hide all dimensions.

If you need to filter out suppressed or hidden dimensions, use [IAnnotation::Visible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~Visible.html) to check the visibility status.

To get the first annotation on the sheet, call [IView::GetFirstAnnotation3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstAnnotation3.html) before calling this method.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IView::GetFirstAnnotation3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstAnnotation3.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.
