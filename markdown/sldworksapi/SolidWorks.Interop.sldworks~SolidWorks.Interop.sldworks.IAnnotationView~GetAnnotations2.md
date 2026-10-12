---
title: "GetAnnotations2 Method (IAnnotationView)"
project: "SOLIDWORKS API Help"
interface: "IAnnotationView"
member: "GetAnnotations2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~GetAnnotations2.html"
---

# GetAnnotations2 Method (IAnnotationView)

Gets the annotations in this annotation view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAnnotations2( _
   ByVal DimXpertOnly As System.Boolean, _
   ByVal UnassignedInPlane As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotationView
Dim DimXpertOnly As System.Boolean
Dim UnassignedInPlane As System.Boolean
Dim value As System.Object

value = instance.GetAnnotations2(DimXpertOnly, UnassignedInPlane)
```

### C#

```csharp
System.object GetAnnotations2(
   System.bool DimXpertOnly,
   System.bool UnassignedInPlane
)
```

### C++/CLI

```cpp
System.Object^ GetAnnotations2(
   System.bool DimXpertOnly,
   System.bool UnassignedInPlane
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DimXpertOnly`: True to get only DimXpert annotations, false to get all annotations
- `UnassignedInPlane`: True to get annotations on all planes, including annotations on unassigned planes; false to get annotations on all planes, except annotations on unassigned planes

### Return Value

[Annotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)

## VBA Syntax

See [AnnotationView::GetAnnotations2](ms-its:sldworksapivb6.chm::/sldworks~AnnotationView~GetAnnotations2.html).

## Examples

[Move Annotations to Notes Area Annotation View (C#)](Move_Annotations_to_First_Annotation_View_Example_CSharp.htm)
[Move Annotations to Notes Area Annotation View (VB.NET)](Move_Annotations_to_First_Annotation_View_Example_VBNET.htm)
[Move Annotations to Notes Area Annotation View (VBA)](Move_Annotations_to_First_Annotation_View_Example_VB.htm)

## See Also

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.html)
[IAnnotationView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.html)
[IAnnotationView::AnnotationCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~AnnotationCount.html)

## Availability

SOLIDWORKS 2015 SP1, Revision number 23.1
