---
title: "IGetAnnotations Method (IAnnotationView)"
project: "SOLIDWORKS API Help"
interface: "IAnnotationView"
member: "IGetAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~IGetAnnotations.html"
---

# IGetAnnotations Method (IAnnotationView)

Obsolete. Superseded by [IAnnotationView::GetAnnotations2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~GetAnnotations2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAnnotations( _
   ByVal AnnotationCount As System.Integer _
) As Annotation
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotationView
Dim AnnotationCount As System.Integer
Dim value As Annotation

value = instance.IGetAnnotations(AnnotationCount)
```

### C#

```csharp
Annotation IGetAnnotations(
   System.int AnnotationCount
)
```

### C++/CLI

```cpp
Annotation^ IGetAnnotations(
   System.int AnnotationCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AnnotationCount`: Number of annotations

### Return Value

- in-process, unmanaged C++: Pointer to an array of [annotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IAnnotationView::AnnotationCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotationView~AnnotationCount.html) to get the value for AnnotationCount.

## See Also

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.html)
[IAnnotationView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.html)
[IAnnotationView::Annotations Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Annotations.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
