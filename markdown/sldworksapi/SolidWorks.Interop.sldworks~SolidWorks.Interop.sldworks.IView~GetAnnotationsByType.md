---
title: "GetAnnotationsByType Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetAnnotationsByType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotationsByType.html"
---

# GetAnnotationsByType Method (IView)

Gets the annotations of the specified type in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAnnotationsByType( _
   ByVal Type As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Type As System.Integer
Dim value As System.Object

value = instance.GetAnnotationsByType(Type)
```

### C#

```csharp
System.object GetAnnotationsByType(
   System.int Type
)
```

### C++/CLI

```cpp
System.Object^ GetAnnotationsByType(
   System.int Type
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Type`: Annotation type as defined by

[swAnnotationType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAnnotationType_e.html)

### Return Value

Array of

[annotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html)

## VBA Syntax

See

[View::GetAnnotationsByType](ms-its:sldworksapivb6.chm::/sldworks~View~GetAnnotationsByType.html)

.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)

[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

[IView::GetAnnotations Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotations.html)

[IView::GetFirstAnnotation3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstAnnotation3.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
