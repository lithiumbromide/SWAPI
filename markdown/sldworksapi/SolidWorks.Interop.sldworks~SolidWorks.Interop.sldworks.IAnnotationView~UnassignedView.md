---
title: "UnassignedView Property (IAnnotationView)"
project: "SOLIDWORKS API Help"
interface: "IAnnotationView"
member: "UnassignedView"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~UnassignedView.html"
---

# UnassignedView Property (IAnnotationView)

Gets whether this annotation view is assigned to a 3D View.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property UnassignedView As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotationView
Dim value As System.Boolean

value = instance.UnassignedView
```

### C#

```csharp
System.bool UnassignedView {get;}
```

### C++/CLI

```cpp
property System.bool UnassignedView {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if this annotation view is not assigned to a 3D View, false if it is

## VBA Syntax

See [AnnotationView::UnassignedView](ms-its:sldworksapivb6.chm::/sldworks~AnnotationView~UnassignedView.html).

## Examples

[Move Annotations to Notes Area Annotation View (C#)](Move_Annotations_to_First_Annotation_View_Example_CSharp.htm)
[Move Annotations to Notes Area Annotation View (VB.NET)](Move_Annotations_to_First_Annotation_View_Example_VBNET.htm)
[Move Annotations to Notes Area Annotation View (VBA)](Move_Annotations_to_First_Annotation_View_Example_VB.htm)

## See Also

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.html)
[IAnnotationView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.html)
[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.html)
[IAnnotationView::FlatPatternView Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~FlatPatternView.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
