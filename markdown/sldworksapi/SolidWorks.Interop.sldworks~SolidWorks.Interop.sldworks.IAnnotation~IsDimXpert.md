---
title: "IsDimXpert Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "IsDimXpert"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IsDimXpert.html"
---

# IsDimXpert Method (IAnnotation)

Gets whether the annotation is a DimXpert annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsDimXpert() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Boolean

value = instance.IsDimXpert()
```

### C#

```csharp
System.bool IsDimXpert()
```

### C++/CLI

```cpp
System.bool IsDimXpert();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the annotation is a DimXpert annotation, false if not

## VBA Syntax

See [Annotation::IsDimXpert](ms-its:sldworksapivb6.chm::/sldworks~Annotation~IsDimXpert.html).

## Examples

[Get DimXpert Display Dimensions and Feature (C#)](Get_DimXpert_Display_Dimensions_and_Feature_Example_CSharp.htm)
[Get DimXpert Display Dimensions and Feature (VB.NET)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VBNET.htm)
[Get DimXpert Display Dimensions and Feature (VBA)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VB.htm)

## Remarks

Use this method to determine if the annotation is a DimXpert display dimension. If it is, then use [IAnnotation::GetDimXpertFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetDimXpertFeature.html) to access the DimXpert feature, which provides access to the display dimension information.

DimXpert annotations such as datums and GTols can be hidden, shown, or hidden as a group, which can be important when exporting to a DXF/DWG file.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::GetDimXpertFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetDimXpertFeature.html)

## Availability

SOLIDWORKS 2009 SP2, Revision Number 17.2
