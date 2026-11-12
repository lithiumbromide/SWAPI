---
title: "CanShowInAnnotationView Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "CanShowInAnnotationView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~CanShowInAnnotationView.html"
---

# CanShowInAnnotationView Method (IAnnotation)

Gets whether this annotation can be shown in the specified [annotation view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CanShowInAnnotationView( _
   ByVal AnnotationViewName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim AnnotationViewName As System.String
Dim value As System.Boolean

value = instance.CanShowInAnnotationView(AnnotationViewName)
```

### C#

```csharp
System.bool CanShowInAnnotationView(
   System.string AnnotationViewName
)
```

### C++/CLI

```cpp
System.bool CanShowInAnnotationView(
   System.String^ AnnotationViewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AnnotationViewName`: Name of annotation view in which to show this annotation (see **Remarks**)

### Return Value

True if this annotation can be shown in the specified annotation view, false if not

## VBA Syntax

See [Annotation::CanShowInAnnotationView](ms-its:sldworksapivb6.chm::/sldworks~Annotation~CanShowInAnnotationView.html).

## Examples

[Get Where Annotations Can Be Shown (C#)](Get_Where_Annotations_Can_Be_Shown_Example_CSharp.htm)
[Get Where Annotations Can Be Shown (VB.NET)](Get_Where_Annotations_Can_Be_Shown_Example_VBNET.htm)
[Get Where Annotations Can Be Shown (VBA)](Get_Where_Annotations_Can_Be_Shown_Example_VB.htm)

## Remarks

Use [IFeature::Name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Name.html) to get the name of the annotation view. See the examples for details.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::CanShowInMultipleAnnotationViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~CanShowInMultipleAnnotationViews.html)
[IAnnotationView::Hide Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Hide.html)
[IAnnotationView::IsShown Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~IsShown.html)
[IAnnotationView::Show Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Show.html)

## Availability

SOLIDWORKS 2015 SP1, Revision Number 23.1
