---
title: "AnnotationCount Property (IAnnotationView)"
project: "SOLIDWORKS API Help"
interface: "IAnnotationView"
member: "AnnotationCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~AnnotationCount.html"
---

# AnnotationCount Property (IAnnotationView)

Gets the number of [annotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html) in this annotation view.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property AnnotationCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotationView
Dim value As System.Integer

value = instance.AnnotationCount
```

### C#

```csharp
System.int AnnotationCount {get;}
```

### C++/CLI

```cpp
property System.int AnnotationCount {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of annotations

## VBA Syntax

See [AnnotationView::AnnotationCount](ms-its:sldworksapivb6.chm::/sldworks~AnnotationView~AnnotationCount.html).

## Examples

[Move Annotations to Notes Area Annotation View (C#)](Move_Annotations_to_First_Annotation_View_Example_CSharp.htm)
[Move Annotations to Notes Area Annotation View (VB.NET)](Move_Annotations_to_First_Annotation_View_Example_VBNET.htm)
[Move Annotations to Notes Area Annotation View (VBA)](Move_Annotations_to_First_Annotation_View_Example_VB.htm)

## Remarks

Call this method before calling [IAnnotationView::IGetAnnotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotationView~IGetAnnotations.html) to get the size of the array for that method.

## See Also

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.html)
[IAnnotationView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.html)
[IAnnotationView::Annotations Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Annotations.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
