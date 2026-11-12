---
title: "AnnotationViews2 Property (IView3D)"
project: "SOLIDWORKS API Help"
interface: "IView3D"
member: "AnnotationViews2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~AnnotationViews2.html"
---

# AnnotationViews2 Property (IView3D)

Gets the annotation views assigned to this 3D View.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property AnnotationViews2 As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView3D
Dim value As System.Object

value = instance.AnnotationViews2
```

### C#

```csharp
System.object AnnotationViews2 {get;}
```

### C++/CLI

```cpp
property System.Object^ AnnotationViews2 {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [IAnnotationView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.html)

## VBA Syntax

See [View3D::AnnotationViews2](ms-its:sldworksapivb6.chm::/sldworks~View3D~AnnotationViews2.html).

## See Also

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.html)
[IView3D Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
