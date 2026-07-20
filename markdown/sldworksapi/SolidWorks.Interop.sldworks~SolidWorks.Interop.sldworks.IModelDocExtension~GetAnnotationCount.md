---
title: "GetAnnotationCount Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetAnnotationCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAnnotationCount.html"
---

# GetAnnotationCount Method (IModelDocExtension)

Gets the number of annotations on this part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAnnotationCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Integer

value = instance.GetAnnotationCount()
```

### C#

```csharp
System.int GetAnnotationCount()
```

### C++/CLI

```cpp
System.int GetAnnotationCount();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Number of annotations

## VBA Syntax

See

[ModelDocExtension::GetAnnotationCount](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetAnnotationCount.html)

.

## Remarks

Call this method before calling[IModelDocExtension::IGetAnnotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetAnnotations.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)

[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

[IModelDocExtension::GetAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAnnotations.html)

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)

[IView::GetAnnotationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotationCount.html)

[IModelDocExtension::GetAnnotationsByType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAnnotationsByType.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
