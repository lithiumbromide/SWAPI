---
title: "GetFirstAnnotation3 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetFirstAnnotation3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstAnnotation3.html"
---

# GetFirstAnnotation3 Method (IView)

Gets the first annotation in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstAnnotation3() As Annotation
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As Annotation

value = instance.GetFirstAnnotation3()
```

### C#

```csharp
Annotation GetFirstAnnotation3()
```

### C++/CLI

```cpp
Annotation^ GetFirstAnnotation3();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

First

[annotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html)

in the drawing view

## VBA Syntax

See

[View::GetFirstAnnotation3](ms-its:sldworksapivb6.chm::/sldworks~View~GetFirstAnnotation3.html)

.

## Examples

[Get Display Dimensions, GTols, and Surface-finish Symbols (VBA)](Get_Display_Dimensions,_Gtols,_and_Surface-Finish_Symbols_Example_VB.htm)

[Get Entities Attached to Cosmetic Thread (VBA)](Get_Entities_Attached_To_Cosmetic_Thread_Example_VB.htm)

[Show Dimensions in Drawing Sheet (VBA)](Show_Dimensions_in_Drawing_Sheet_Example_VB.htm)

## Remarks

This method gets any display dimension, including suppressed, hidden, or dangling dimensions on the sheet and on the sheet format if it is visible. The sheet must be visible. See[ISheet::SheetFormatVisible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet~SheetFormatVisible.html).

A dimension becomes suppressed or hidden when you specifically select a dimension and hide it or when you select a feature and say hide all dimensions. If you need to filter out these dimensions, you must use[IAnnotation::Visible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~Visible.html)to check that status.

If the annotation is on a layer that is not shown, the annotation is still returned.

To get the next annotation, call[IAnnotation::GetNext3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetNext3.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)

[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

[IView::GetAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotations.html)

[IView::IGetAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetAnnotations.html)

[IView::GetAnnotationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotationCount.html)

[IAnnotation::GetNext3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetNext3.html)

[IView::GetAnnotationsByType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotationsByType.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
