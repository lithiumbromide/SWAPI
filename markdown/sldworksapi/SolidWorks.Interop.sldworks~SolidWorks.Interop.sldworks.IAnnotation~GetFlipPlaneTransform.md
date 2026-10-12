---
title: "GetFlipPlaneTransform Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "GetFlipPlaneTransform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetFlipPlaneTransform.html"
---

# GetFlipPlaneTransform Method (IAnnotation)

Gets the transformation matrix of the annotation plane in the opposite direction.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFlipPlaneTransform() As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As MathTransform

value = instance.GetFlipPlaneTransform()
```

### C#

```csharp
MathTransform GetFlipPlaneTransform()
```

### C++/CLI

```cpp
MathTransform^ GetFlipPlaneTransform();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Transformation matrix](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.html) of the annotation plane in the opposite direction

## VBA Syntax

See [Annotation::GetFlipPlaneTransform](ms-its:sldworksapivb6.chm::/sldworks~Annotation~GetFlipPlaneTransform.html).

## Examples

[Move Annotations to Notes Area Annotation View (C#)](Move_Annotations_to_First_Annotation_View_Example_CSharp.htm)
[Move Annotations to Notes Area Annotation View (VB.NET)](Move_Annotations_to_First_Annotation_View_Example_VBNET.htm)
[Move Annotations to Notes Area Annotation View (VBA)](Move_Annotations_to_First_Annotation_View_Example_VB.htm)

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)

## Availability

SOLIDWORKS 2015 SP1, Revision Number 23.1
