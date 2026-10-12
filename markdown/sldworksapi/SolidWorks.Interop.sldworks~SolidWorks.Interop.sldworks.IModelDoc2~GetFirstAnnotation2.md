---
title: "GetFirstAnnotation2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetFirstAnnotation2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFirstAnnotation2.html"
---

# GetFirstAnnotation2 Method (IModelDoc2)

Gets the first annotation in the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstAnnotation2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Object

value = instance.GetFirstAnnotation2()
```

### C#

```csharp
System.object GetFirstAnnotation2()
```

### C++/CLI

```cpp
System.Object^ GetFirstAnnotation2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [annotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html)

## VBA Syntax

See [ModelDoc2::GetFirstAnnotation2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetFirstAnnotation2.html).

## Examples

[Get Display Dimensions, GTols, and Surface-finish Symbols (VBA)](Get_Display_Dimensions,_Gtols,_and_Surface-Finish_Symbols_Example_VB.htm)
[Get DimXpert Display Dimensions and Feature (C#)](Get_DimXpert_Display_Dimensions_and_Feature_Example_CSharp.htm)
[Get DimXpert Display Dimensions and Feature (VB.NET)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VBNET.htm)
[Get DimXpert Display Dimensions and Feature (VBA)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VB.htm)

## Remarks

For parts and assemblies, this method returns the first [IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) object in the model. For drawings, access the annotations using the [IView::GetFirstAnnotation3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstAnnotation3.html) method.

A dimension becomes suppressed or hidden when you specifically select a dimension and hide it, or when you select a feature and you select to hide all dimensions. If you need to filter out these dimensions, use [IAnnotation::Visible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) to check that status.

NOTE: The difference between the obsoleted IModelDoc2::GetFirstAnnotation and this method, IModelDoc2::GetFirstAnnotation2, is that IModelDoc2::GetFirstAnnotation2 retrieves any display dimension, including suppressed, hidden, or dangling dimensions.

To get the next annotation in the model, call [IAnnotation::GetNext3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetNext3.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::IGetFirstAnnotation2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetFirstAnnotation2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
