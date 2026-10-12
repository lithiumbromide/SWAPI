---
title: "AnnotationView Property (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "AnnotationView"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~AnnotationView.html"
---

# AnnotationView Property (IAnnotation)

Gets the annotation view for this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property AnnotationView As AnnotationView
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As AnnotationView

value = instance.AnnotationView
```

### C#

```csharp
AnnotationView AnnotationView {get;}
```

### C++/CLI

```cpp
property AnnotationView^ AnnotationView {
   AnnotationView^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Annotation view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotationView.html)

## VBA Syntax

See [Annotation::AnnotationView](ms-its:sldworksapivb6.chm::/sldworks~Annotation~AnnotationView.html).

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
