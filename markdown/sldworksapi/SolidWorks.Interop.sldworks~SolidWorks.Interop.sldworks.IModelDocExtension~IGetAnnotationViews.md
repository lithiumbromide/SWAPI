---
title: "IGetAnnotationViews Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IGetAnnotationViews"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetAnnotationViews.html"
---

# IGetAnnotationViews Method (IModelDocExtension)

Gets the annotation views in this part or assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAnnotationViews( _
   ByVal AnnotationViewCount As System.Integer _
) As AnnotationView
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim AnnotationViewCount As System.Integer
Dim value As AnnotationView

value = instance.IGetAnnotationViews(AnnotationViewCount)
```

### C#

```csharp
AnnotationView IGetAnnotationViews(
   System.int AnnotationViewCount
)
```

### C++/CLI

```cpp
AnnotationView^ IGetAnnotationViews(
   System.int AnnotationViewCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AnnotationViewCount`: Number of annotation views in this part or assembly document

### Return Value

- in-process, unmanaged C++: Pointer to an array of [annotation views](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotationView.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IModelDocExtension::AnnotationViewCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~AnnotationViewCount.html) to get the value of AnnotationViewCount.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::AnnotationViews Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AnnotationViews.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
