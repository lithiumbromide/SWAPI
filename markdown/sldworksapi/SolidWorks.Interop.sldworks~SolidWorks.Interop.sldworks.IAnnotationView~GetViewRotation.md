---
title: "GetViewRotation Method (IAnnotationView)"
project: "SOLIDWORKS API Help"
interface: "IAnnotationView"
member: "GetViewRotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~GetViewRotation.html"
---

# GetViewRotation Method (IAnnotationView)

Gets the rotation matrix of the annotation view relative to the X-Y plane of the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetViewRotation() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotationView
Dim value As System.Object

value = instance.GetViewRotation()
```

### C#

```csharp
System.object GetViewRotation()
```

### C++/CLI

```cpp
System.Object^ GetViewRotation();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of 9 doubles of the rotation matrix of the annotation view relative to the X-Y plane of the model

## VBA Syntax

See [AnnotationView::GetViewRotation](ms-its:sldworksapivb6.chm::/sldworks~AnnotationView~GetViewRotation.html).

## See Also

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.html)
[IAnnotationView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.html)
[IAnnotation::IGetViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~IGetViewRotation.html)
[IAnnotation::GetPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPlane.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
