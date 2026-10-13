---
title: "IsDimXpert Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "IsDimXpert"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsDimXpert.html"
---

# IsDimXpert Method (IDisplayDimension)

Obsolete. Superseded by [IAnnotation::IsDimXpert](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~IsDimXpert.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IsDimXpert() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
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

True if the display dimension is a DimXpert dimension, false if not

## VBA Syntax

See [DisplayDimension::IsDimXpert](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~IsDimXpert.html).

## Examples

[Get DimXpert Display Dimensions and Feature (C#)](Get_DimXpert_Display_Dimensions_and_Feature_Example_CSharp.htm)
[Get DimXpert Display Dimensions and Feature (VB.NET)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VBNET.htm)
[Get DimXpert Display Dimensions and Feature (VBA)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VB.htm)

## Remarks

Use this method to determine if the display dimension is a DimXpert display dimension. If it is, then use [IAnnotation::GetDimXpertFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetDimXpertFeature.html) to access the DimXpert feature, which provides access to the display dimension information.

DimXpert dimensions can be hidden shown or hidden as a group, which can be important when exporting to a DXF/DWG file.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IAnnotation::IsDimXpert Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IsDimXpert.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
