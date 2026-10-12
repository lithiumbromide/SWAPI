---
title: "Orient Method (IAnnotationView)"
project: "SOLIDWORKS API Help"
interface: "IAnnotationView"
member: "Orient"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Orient.html"
---

# Orient Method (IAnnotationView)

Orients this annotation view.

## Syntax

### Visual Basic (Declaration)

```vb
Function Orient() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotationView
Dim value As System.Boolean

value = instance.Orient()
```

### C#

```csharp
System.bool Orient()
```

### C++/CLI

```cpp
System.bool Orient();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the annotation view is oriented, false if not

## VBA Syntax

See [AnnotationView::Orient](ms-its:sldworksapivb6.chm::/sldworks~AnnotationView~Orient.html).

## Remarks

The annotation view is oriented normal to its plane.

## See Also

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.html)
[IAnnotationView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.html)
[IAnnotationView::ActivateAndReorient Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~ActivateAndReorient.html)
[IAnnotationView::Activate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Activate.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
