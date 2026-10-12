---
title: "ActivateAndReorient Method (IAnnotationView)"
project: "SOLIDWORKS API Help"
interface: "IAnnotationView"
member: "ActivateAndReorient"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~ActivateAndReorient.html"
---

# ActivateAndReorient Method (IAnnotationView)

Activates and reorients this annotation view.

## Syntax

### Visual Basic (Declaration)

```vb
Function ActivateAndReorient() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotationView
Dim value As System.Boolean

value = instance.ActivateAndReorient()
```

### C#

```csharp
System.bool ActivateAndReorient()
```

### C++/CLI

```cpp
System.bool ActivateAndReorient();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the annotation view is activated and reoriented, false if not

## VBA Syntax

See [AnnotationView::ActivateAndReorient](ms-its:sldworksapivb6.chm::/sldworks~AnnotationView~ActivateAndReorient.html).

## Remarks

The annotation view is oriented normal to its plane.

## See Also

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.html)
[IAnnotationView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.html)
[IAnnotationView::Activate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Activate.html)
[IAnnotationView::Orient Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Orient.html)
[IAnnotationView::Hide Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Hide.html)
[IAnnotationView::Show Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Show.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
