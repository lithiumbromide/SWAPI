---
title: "CanShowInMultipleAnnotationViews Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "CanShowInMultipleAnnotationViews"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~CanShowInMultipleAnnotationViews.html"
---

# CanShowInMultipleAnnotationViews Method (IAnnotation)

Gets whether this annotation can be shown in multiple [annotation views.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function CanShowInMultipleAnnotationViews() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Boolean

value = instance.CanShowInMultipleAnnotationViews()
```

### C#

```csharp
System.bool CanShowInMultipleAnnotationViews()
```

### C++/CLI

```cpp
System.bool CanShowInMultipleAnnotationViews();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this annotation can be shown in multiple annotation views, false if not

## VBA Syntax

See [Annotation::CanShowInMultipleAnnotationViews](ms-its:sldworksapivb6.chm::/sldworks~Annotation~CanShowInMultipleAnnotationViews.html).

## Examples

[Get Where Annotations Can Be Shown (C#)](Get_Where_Annotations_Can_Be_Shown_Example_CSharp.htm)
[Get Where Annotations Can Be Shown (VB.NET)](Get_Where_Annotations_Can_Be_Shown_Example_VBNET.htm)
[Get Where Annotations Can Be Shown (VBA)](Get_Where_Annotations_Can_Be_Shown_Example_VB.htm)

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::CanShowInAnnotationView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~CanShowInAnnotationView.html)
[IAnnotationView::Hide Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Hide.html)
[IAnnotationView::IsShown Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~IsShown.html)
[IAnnotationView::Show Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Show.html)

## Availability

SOLIDWORKS 2015 SP1, Revision Number 23.1
