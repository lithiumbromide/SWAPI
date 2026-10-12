---
title: "Always2D Property (IAnnotationView)"
project: "SOLIDWORKS API Help"
interface: "IAnnotationView"
member: "Always2D"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Always2D.html"
---

# Always2D Property (IAnnotationView)

Gets whether to display annotations in 2D or 3D.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Always2D As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotationView
Dim value As System.Boolean

value = instance.Always2D
```

### C#

```csharp
System.bool Always2D {get;}
```

### C++/CLI

```cpp
property System.bool Always2D {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display annotations in 2D, false to display them in 3D

## VBA Syntax

See [AnnotationView::Always2D](ms-its:sldworksapivb6.chm::/sldworks~AnnotationView~Always2D.html).

## See Also

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.html)
[IAnnotationView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
