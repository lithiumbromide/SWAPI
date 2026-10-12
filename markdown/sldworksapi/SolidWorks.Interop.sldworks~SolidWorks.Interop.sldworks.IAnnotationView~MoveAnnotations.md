---
title: "MoveAnnotations Method (IAnnotationView)"
project: "SOLIDWORKS API Help"
interface: "IAnnotationView"
member: "MoveAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~MoveAnnotations.html"
---

# MoveAnnotations Method (IAnnotationView)

Moves the specified annotations to this annotation view.

## Syntax

### Visual Basic (Declaration)

```vb
Function MoveAnnotations( _
   ByVal AnnotationsToMove As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotationView
Dim AnnotationsToMove As System.Object
Dim value As System.Boolean

value = instance.MoveAnnotations(AnnotationsToMove)
```

### C#

```csharp
System.bool MoveAnnotations(
   System.object AnnotationsToMove
)
```

### C++/CLI

```cpp
System.bool MoveAnnotations(
   System.Object^ AnnotationsToMove
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AnnotationsToMove`: Annotations to move

### Return Value

True if the specified annotations are moved, false if not

## VBA Syntax

See [AnnotationView::MoveAnnotations](ms-its:sldworksapivb6.chm::/sldworks~AnnotationView~MoveAnnotations.html).

## Examples

[Move Annotations to Notes Area Annotation View (C#)](Move_Annotations_to_First_Annotation_View_Example_CSharp.htm)
[Move Annotations to Notes Area Annotation View (VB.NET)](Move_Annotations_to_First_Annotation_View_Example_VBNET.htm)
[Move Annotations to Notes Area Annotation View (VBA)](Move_Annotations_to_First_Annotation_View_Example_VB.htm)

## See Also

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.html)
[IAnnotationView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
