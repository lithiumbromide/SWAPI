---
title: "Annotations Property (IAnnotationView)"
project: "SOLIDWORKS API Help"
interface: "IAnnotationView"
member: "Annotations"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Annotations.html"
---

# Annotations Property (IAnnotationView)

Obsolete. Superseded by [IAnnotationView::GetAnnotations2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~GetAnnotations2.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Annotations As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotationView
Dim value As System.Object

value = instance.Annotations
```

### C#

```csharp
System.object Annotations {get;}
```

### C++/CLI

```cpp
property System.Object^ Annotations {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Annotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)

## VBA Syntax

See [AnnotationView::Annotations](ms-its:sldworksapivb6.chm::/sldworks~AnnotationView~Annotations.html).

## See Also

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.html)
[IAnnotationView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.html)
[IAnnotationView::IGetAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~IGetAnnotations.html)
[IAnnotationView::AnnotationCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~AnnotationCount.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
