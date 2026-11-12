---
title: "IGetAnnotations Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetAnnotations.html"
---

# IGetAnnotations Method (IView)

Gets the annotations in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAnnotations( _
   ByVal NumAnnotations As System.Integer _
) As Annotation
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim NumAnnotations As System.Integer
Dim value As Annotation

value = instance.IGetAnnotations(NumAnnotations)
```

### C#

```csharp
Annotation IGetAnnotations(
   System.int NumAnnotations
)
```

### C++/CLI

```cpp
Annotation^ IGetAnnotations(
   System.int NumAnnotations
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumAnnotations`: Number of annotations

### Return Value

- in-process, unmanaged C++: Pointer to an array of [annotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IView::GetAnnotationCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetAnnotationCount.html) before calling this method to get the value for NumAnnotations.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotations.html)
[IView::GetFirstAnnotation3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstAnnotation3.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
