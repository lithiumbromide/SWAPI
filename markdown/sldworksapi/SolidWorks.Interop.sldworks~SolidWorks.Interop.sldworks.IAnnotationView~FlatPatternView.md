---
title: "FlatPatternView Property (IAnnotationView)"
project: "SOLIDWORKS API Help"
interface: "IAnnotationView"
member: "FlatPatternView"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~FlatPatternView.html"
---

# FlatPatternView Property (IAnnotationView)

Gets whether this annotation view is a flat-pattern view.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FlatPatternView As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotationView
Dim value As System.Boolean

value = instance.FlatPatternView
```

### C#

```csharp
System.bool FlatPatternView {get;}
```

### C++/CLI

```cpp
property System.bool FlatPatternView {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if this annotation view is a flat-pattern view, false if not

## VBA Syntax

See [AnnotationView::FlatPatternView](ms-its:sldworksapivb6.chm::/sldworks~AnnotationView~FlatPatternView.html).

## Examples

[Move Annotations to Notes Area Annotation View (C#)](Move_Annotations_to_First_Annotation_View_Example_CSharp.htm)
[Move Annotations to Notes Area Annotation View (VB.NET)](Move_Annotations_to_First_Annotation_View_Example_VBNET.htm)
[Move Annotations to Notes Area Annotation View (VBA)](Move_Annotations_to_First_Annotation_View_Example_VB.htm)

## See Also

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.html)
[IAnnotationView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.html)
[IAnnotationView::UnassignedView Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~UnassignedView.html)

## Availability

SOLIDWORKS 2015 SP1, Revision Number 23.1
