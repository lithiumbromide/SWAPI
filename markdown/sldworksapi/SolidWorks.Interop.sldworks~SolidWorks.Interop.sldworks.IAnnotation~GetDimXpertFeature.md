---
title: "GetDimXpertFeature Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "GetDimXpertFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetDimXpertFeature.html"
---

# GetDimXpertFeature Method (IAnnotation)

Gets the DimXpert feature associated with this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDimXpertFeature() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Object

value = instance.GetDimXpertFeature()
```

### C#

```csharp
System.object GetDimXpertFeature()
```

### C++/CLI

```cpp
System.Object^ GetDimXpertFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[DimXpert feature](ms-its:swdimxpertapi.chm::/SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)

## VBA Syntax

See [Annotation::GetDimXpertFeature](ms-its:sldworksapivb6.chm::/sldworks~Annotation~GetDimXpertFeature.html).

## Examples

[Get DimXpert Display Dimensions and Feature (C#)](Get_DimXpert_Display_Dimensions_and_Feature_Example_CSharp.htm)
[Get DimXpert Display Dimensions and Feature (VB.NET)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VBNET.htm)
[Get DimXpert Display Dimensions and Feature (VBA)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VB.htm)

## Remarks

If an annotation is a display dimension, then use [IAnnotation::IsDimXpert](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~IsDimXpert.html) to determine if it is a DimXpert annotation. If it is, then use IAnnotation::GetDimXpertFeature to access the DimXpert feature, which provides access to the display dimension information.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IDisplayDimension::IsDimXpert Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsDimXpert.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
