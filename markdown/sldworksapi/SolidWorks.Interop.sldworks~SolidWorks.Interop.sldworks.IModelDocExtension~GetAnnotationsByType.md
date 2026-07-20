---
title: "GetAnnotationsByType Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetAnnotationsByType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAnnotationsByType.html"
---

# GetAnnotationsByType Method (IModelDocExtension)

Gets the annotations of the specified type in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAnnotationsByType( _
   ByVal Type As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Type As System.Integer
Dim value As System.Object

value = instance.GetAnnotationsByType(Type)
```

### C#

```csharp
System.object GetAnnotationsByType(
   System.int Type
)
```

### C++/CLI

```cpp
System.Object^ GetAnnotationsByType(
   System.int Type
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Type`: Annotation type as defined by

[swAnnotationType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAnnotationType_e.html)

(see

Remarks

)

### Return Value

Array of

[annotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html)

## VBA Syntax

See

[ModelDocExtension::GetAnnotationsByType](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetAnnotationsByType.html)

.

## Remarks

This method does not support swAnnotationType_e.swCThread for parts and assemblies, because in those models cosmetic threads are added as sub-features of holes, not annotations.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)

[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

[IModelDocExtension::GetAnnotations Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAnnotations.html)

[IModelDocExtension::GetAnnotationCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAnnotationCount.html)

[IView::GetAnnotationsByType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotationsByType.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
