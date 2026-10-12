---
title: "IGetFirstAnnotation2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IGetFirstAnnotation2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetFirstAnnotation2.html"
---

# IGetFirstAnnotation2 Method (IModelDoc2)

Gets the first annotation in the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFirstAnnotation2() As Annotation
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As Annotation

value = instance.IGetFirstAnnotation2()
```

### C#

```csharp
Annotation IGetFirstAnnotation2()
```

### C++/CLI

```cpp
Annotation^ IGetFirstAnnotation2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [annotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) in model

## VBA Syntax

See [ModelDoc2::IGetFirstAnnotation2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IGetFirstAnnotation2.html).

## Remarks

For parts and assemblies, this method returns the first [IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) object in the model. For drawings, access the annotations using the [IView::GetFirstAnnotation3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstAnnotation3.html) method.

A dimension becomes suppressed or hidden when you specifically select a dimension and hide it, or when you select a feature and you select to hide all dimensions. If you need to filter out these dimensions, use [IAnnotation::Visible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) to check that status.

NOTE: The difference between the obsoleted IModelDoc2::GetFirstAnnotation and this method, IModelDoc2::GetFirstAnnotation2, is that IModelDoc2::GetFirstAnnotation2 retrieves any display dimension, including suppressed, hidden, or dangling dimensions.

To get the next annotation in the model, call [IAnnotation::GetNext3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetNext3.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetFirstAnnotation2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFirstAnnotation2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
