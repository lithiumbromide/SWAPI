---
title: "Activate Method (IAnnotationView)"
project: "SOLIDWORKS API Help"
interface: "IAnnotationView"
member: "Activate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Activate.html"
---

# Activate Method (IAnnotationView)

Activates this annotation view.

## Syntax

### Visual Basic (Declaration)

```vb
Function Activate() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotationView
Dim value As System.Boolean

value = instance.Activate()
```

### C#

```csharp
System.bool Activate()
```

### C++/CLI

```cpp
System.bool Activate();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the annotation view is activated, false if not

## VBA Syntax

See [AnnotationView::Activate](ms-its:sldworksapivb6.chm::/sldworks~AnnotationView~Activate.html).

## Examples

[Move Annotations to Notes Area Annotation View (C#)](Move_Annotations_to_First_Annotation_View_Example_CSharp.htm)
[Move Annotations to Notes Area Annotation View (VB.NET)](Move_Annotations_to_First_Annotation_View_Example_VBNET.htm)
[Move Annotations to Notes Area Annotation View (VBA)](Move_Annotations_to_First_Annotation_View_Example_VB.htm)

## See Also

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.html)
[IAnnotationView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.html)
[IAnnotationView::ActivateAndReorient Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~ActivateAndReorient.html)
[IAnnotationView::Hide Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Hide.html)
[IAnnotationView::Show Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Show.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
