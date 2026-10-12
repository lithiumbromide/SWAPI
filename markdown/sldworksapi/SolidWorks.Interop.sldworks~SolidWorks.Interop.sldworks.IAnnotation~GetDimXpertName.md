---
title: "GetDimXpertName Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "GetDimXpertName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetDimXpertName.html"
---

# GetDimXpertName Method (IAnnotation)

Gets the DimXpert name for this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDimXpertName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.String

value = instance.GetDimXpertName()
```

### C#

```csharp
System.string GetDimXpertName()
```

### C++/CLI

```cpp
System.String^ GetDimXpertName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

DimXpert name

## VBA Syntax

See [Annotation::GetDimXpertName](ms-its:sldworksapivb6.chm::/sldworks~Annotation~GetDimXpertName.html).

## Examples

[Get DimXpert Display Dimensions and Features (C#)](Get_DimXpert_Display_Dimensions_and_Feature_Example_CSharp.htm)
[Get DimXpert Display Dimensions and Features (VB.NET)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VBNET.htm)
[Get DimXpert Display Dimensions and Features (VBA)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VB.htm)

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::GetName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetName.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
