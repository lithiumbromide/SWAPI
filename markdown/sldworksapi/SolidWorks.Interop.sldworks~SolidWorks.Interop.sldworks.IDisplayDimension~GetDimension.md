---
title: "GetDimension Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetDimension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetDimension.html"
---

# GetDimension Method (IDisplayDimension)

Obsolete. Superseded by [IDisplayDimension::GetDimension2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetDimension2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDimension() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Object

value = instance.GetDimension()
```

### C#

```csharp
System.object GetDimension()
```

### C++/CLI

```cpp
System.Object^ GetDimension();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Dimension

## VBA Syntax

See [DisplayDimension::GetDimension](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetDimension.html).

## Examples

[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)
[Get Component Via Display Dimension (VBA)](Get_Component_Via_Display_Dimension_Example_VB.htm)
[Get Display Dimension Properties (VBA)](Get_Display_Dimension_Properties_Example_VB.htm)
[Iterate Through Dimensions in Model (VBA)](Iterate_Through_Dimensions_in_Model_Example_VB.htm)
[Set Dimensions to Mid-tolerance (VBA)](Set_Dimensions_to_Mid-Tolerance_Example_VB.htm)
[Traverse Feature Dimensions (VBA)](Traverse_Feature_Dimensions_Example_VB.htm)
[Unlink Dimensions (VBA)](Unlink_Dimensions_Example_VB.htm)

## Remarks

SOLIDWORKS can display a dimension more than once. For example, a base-extrude dimension can be brought into three different views on a drawing. These three dimensions are referred to as display dimensions and are represented by the [IDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html) object in the SOLIDWORKS API. The original base-extrude dimension is represented by the [IDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension.html) object in the SOLIDWORKS API.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IFeature::Parameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Parameter.html)
[IFeature::IParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IParameter.html)
[IModelDoc2::Parameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Parameter.html)
[IModelDoc2::IParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IParameter.html)
[IDisplayDimension::IGetDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IGetDimension.html)
