---
title: "IGetAnnotations Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IGetAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetAnnotations.html"
---

# IGetAnnotations Method (IModelDocExtension)

Gets the annotations on this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAnnotations( _
   ByVal NumAnnotations As System.Integer _
) As Annotation
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim NumAnnotations As System.Integer
Dim value As Annotation

value = instance.IGetAnnotations(NumAnnotations)
```

### C#

```csharp
Annotation IGetAnnotations(
   System.int NumAnnotations
)
```

### C++/CLI

```cpp
Annotation^ IGetAnnotations(
   System.int NumAnnotations
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumAnnotations`: Number of annotations

### Return Value

- in-process, unmanaged C++: Pointer to an array of [annotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IModelDocExtension::GetAnnotationCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetAnnotations.html) before calling this method.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAnnotations.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
