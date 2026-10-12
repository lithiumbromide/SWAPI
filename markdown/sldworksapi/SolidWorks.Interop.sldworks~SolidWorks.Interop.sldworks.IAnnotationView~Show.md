---
title: "Show Method (IAnnotationView)"
project: "SOLIDWORKS API Help"
interface: "IAnnotationView"
member: "Show"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Show.html"
---

# Show Method (IAnnotationView)

Shows the annotations in an annotation view that is not activated.

## Syntax

### Visual Basic (Declaration)

```vb
Function Show() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotationView
Dim value As System.Boolean

value = instance.Show()
```

### C#

```csharp
System.bool Show()
```

### C++/CLI

```cpp
System.bool Show();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the annotations in an annotation view that is not activated are shown (see **Remarks**)

## VBA Syntax

See [AnnotationView::Show](ms-its:sldworksapivb6.chm::/sldworks~AnnotationView~Show.html).

## Examples

[Move Annotations to Notes Area Annotation View (C#)](Move_Annotations_to_First_Annotation_View_Example_CSharp.htm)
[Move Annotations to Notes Area Annotation View (VB.NET)](Move_Annotations_to_First_Annotation_View_Example_VBNET.htm)
[Move Annotations to Notes Area Annotation View (VBA)](Move_Annotations_to_First_Annotation_View_Example_VB.htm)

## Remarks

This method returns false if the annotation view is activated.

## See Also

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.html)
[IAnnotationView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.html)
[IAnnotationView::Hide Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Hide.html)
[IAnnotationView::IsShown Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~IsShown.html)
[IAnnotationView::Activate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Activate.html)
[IAnnotationView::ActivateAndReorient Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~ActivateAndReorient.html)
[IAnnotation::CanShowInAnnotationView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~CanShowInAnnotationView.html)
[IAnnotation::CanShowInMultipleAnnotationViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~CanShowInMultipleAnnotationViews.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
