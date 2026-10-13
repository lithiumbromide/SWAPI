---
title: "AnnotationViews Property (IView3D)"
project: "SOLIDWORKS API Help"
interface: "IView3D"
member: "AnnotationViews"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~AnnotationViews.html"
---

# AnnotationViews Property (IView3D)

Gets or sets the annotation views assigned to this 3D View.

## Syntax

### Visual Basic (Declaration)

```vb
Property AnnotationViews As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView3D
Dim value As System.Object

instance.AnnotationViews = value

value = instance.AnnotationViews
```

### C#

```csharp
System.object AnnotationViews {get; set;}
```

### C++/CLI

```cpp
property System.Object^ AnnotationViews {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [IAnnotationView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotationView.html)s

## VBA Syntax

See [View3D::AnnotationViews](ms-its:sldworksapivb6.chm::/sldworks~View3D~AnnotationViews.html).

## See Also

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.html)
[IView3D Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
