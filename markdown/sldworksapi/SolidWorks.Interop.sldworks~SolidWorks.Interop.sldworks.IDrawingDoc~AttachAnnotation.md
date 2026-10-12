---
title: "AttachAnnotation Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "AttachAnnotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AttachAnnotation.html"
---

# AttachAnnotation Method (IDrawingDoc)

Attaches an existing annotation to a drawing sheet or view.

## Syntax

### Visual Basic (Declaration)

```vb
Function AttachAnnotation( _
   ByVal Option As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Option As System.Integer
Dim value As System.Boolean

value = instance.AttachAnnotation(Option)
```

### C#

```csharp
System.bool AttachAnnotation(
   System.int Option
)
```

### C++/CLI

```cpp
System.bool AttachAnnotation(
   System.int Option
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Option`: Annotation attachment option as defined in [swAttachAnnotationOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAttachAnnotationOption_e.html)

### Return Value

True if attachment is successful, false if not

## VBA Syntax

See [DrawingDoc::AttachAnnotation](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~AttachAnnotation.html).

## Examples

[Attach Annotation (VBA)](Attach_Annotation_Example_VB.htm)
[Attach Annotation (VB.NET)](Attach_Annotation_Example_VBNET.htm)
[Attach Annotation (C#)](Attach_Annotation_Example_CSharp.htm)

## Remarks

To attach an annotation to a drawing view:

1. Multi-select the annotation and drawing view.
2. Call this method with Option set to swAttachAnnotationOption_e.swAttachAnnotationOption_View.

To attach an annotation to a drawing sheet:

1. Select the annotation.
2. Call this method with Option set to swAttachAnnotationOption_e.swAttachAnnotationOption_Sheet.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::InsertModelAnnotations3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelAnnotations3.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
