---
title: "Visible Property (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "Visible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Visible.html"
---

# Visible Property (IAnnotation)

Gets or sets the visibility state of this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Property Visible As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Integer

instance.Visible = value

value = instance.Visible
```

### C#

```csharp
System.int Visible {get; set;}
```

### C++/CLI

```cpp
property System.int Visible {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Visibility state as defined in [swAnnotationVisibilityState_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAnnotationVisibilityState_e.html)

## VBA Syntax

See [Annotation::Visible](ms-its:sldworksapivb6.chm::/sldworks~Annotation~Visible.html).

## Examples

[Get Patterned Cosmetic Thread Annotations Data (C#)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_CSharp.htm)
[Get Patterned Cosmetic Thread Annotations Data (VB.NET)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VBNET.htm)
[Get Patterned Cosmetic Thread Annotations Data (VBA)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VB.htm)

## Remarks

There are several reasons why an annotation might or might not be visible on the screen.

This property determines whether an annotation has been individually displayed or hidden if you selected and specifically hid the annotation or if you selected and specifically hid the dimensions of a feature. This property cannot determine whether an annotation is hidden if it is on a layer that is hidden (all annotations of this type are hidden) or if the feature that owns it is suppressed. Therefore, even though this method indicates that an annotation is visible, it might not necessarily be visible on the screen.

If an annotation's visibility is set to swAnnotationHalfHidden, then that annotation is in a half-hidden state, which is not a permanent state. For example, during a **Hide/Show Annotations** operation in a drawing, a half-hidden annotation is displayed in gray if the interactive user selects to show all annotations. Any annotation set to swAnnotationHalfHidden is hidden when the interactive user finishes using **Hide/Show Annotations**.

When you use this property to change the visibility of an annotation, you also cause changes to the visible model. To see those changes, redraw the graphics window using [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html).

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)

## Availability

SOLIDWORKS 99 SP05 datecode 1999313
