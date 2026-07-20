---
title: "GetAnnotations Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotations.html"
---

# GetAnnotations Method (IView)

Gets the annotations in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAnnotations() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
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

[View::GetAnnotations](ms-its:sldworksapivb6.chm::/sldworks~View~GetAnnotations.html)

.

## Examples

[Get Names of Annotations (VBA)](Get_Names_of_Annotations_Example_VB.htm)

[Get Names of Annotations (C#)](Get_Names_of_Annotations_Example_CSharp.htm)

[Get Names of Annotations (VB.NET)](Get_Names_of_Annotations_Example_VBNET.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)

[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

[IView::GetAnnotationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotationCount.html)

[IView::IGetAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetAnnotations.html)

[IView::GetFirstAnnotation3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstAnnotation3.html)

[IView::GetAnnotationsByType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotationsByType.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
