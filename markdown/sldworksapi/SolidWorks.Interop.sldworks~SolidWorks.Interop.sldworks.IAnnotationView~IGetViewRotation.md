---
title: "IGetViewRotation Method (IAnnotationView)"
project: "SOLIDWORKS API Help"
interface: "IAnnotationView"
member: "IGetViewRotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~IGetViewRotation.html"
---

# IGetViewRotation Method (IAnnotationView)

Gets the rotation matrix of the annotation view relative to the X-Y plane of the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetViewRotation() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotationView
Dim value As System.Double

value = instance.IGetViewRotation()
```

### C#

```csharp
System.double IGetViewRotation()
```

### C++/CLI

```cpp
System.double IGetViewRotation();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of 9 doubles of the rotation matrix of the annotation view relative to the X-Y plane of the model

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.html)
[IAnnotationView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.html)
[IAnnotation::GetViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~GetViewRotation.html)
[IAnnotation::GetPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPlane.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
