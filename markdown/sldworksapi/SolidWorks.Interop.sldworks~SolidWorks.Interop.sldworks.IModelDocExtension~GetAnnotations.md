---
title: "GetAnnotations Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAnnotations.html"
---

# GetAnnotations Method (IModelDocExtension)

Gets the annotations on this part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAnnotations() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Object

value = instance.GetAnnotations()
```

### C#

```csharp
System.object GetAnnotations()
```

### C++/CLI

```cpp
System.Object^ GetAnnotations();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Array of

[annotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html)

## VBA Syntax

See

[ModelDocExtension::GetAnnotations](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetAnnotations.html)

.

## Examples

[Get Annotations (VBA)](Get_Annotations_Example_VB.htm)

[Get Annotations (VB.NET)](Get_Annotations_Example_VBNET.htm)

[Get Annotations (C#)](Get_Annotations_Example_CSharp.htm)

## Remarks

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)

[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

[IModelDocExtension::GetAnnotationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAnnotationCount.html)

[IModelDocExtension::IGetAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetAnnotations.html)

[IView::GetAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotations.html)

[IModelDocExtension::GetAnnotationsByType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAnnotationsByType.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
