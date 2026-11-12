---
title: "GetDisplayDimension Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetDisplayDimension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDisplayDimension.html"
---

# GetDisplayDimension Method (IFeature)

Gets the display dimension object for the specified pattern property.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayDimension( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetDisplayDimension(Index)
```

### C#

```csharp
System.object GetDisplayDimension(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetDisplayDimension(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Pattern property as defined by [swFeatureDimensionParameter_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureDimensionParameter_e.html)

### Return Value

[IDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html)

## VBA Syntax

See [Feature::GetDisplayDimension](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetDisplayDimension.html).

## Examples

[Get Pattern Display Dimension (VBA)](Get_Pattern_Display_Dimension_Example_VB.htm)
[Get Pattern Display Dimension (VB.NET)](Get_Pattern_Display_Dimension_Example_VBNET.htm)
[Get Pattern Display Dimension (C#)](Get_Pattern_Display_Dimension_Example_CSharp.htm)

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::EnumDisplayDimensions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~EnumDisplayDimensions.html)
[IFeature::GetFirstDisplayDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFirstDisplayDimension.html)
[IFeature::GetNextDisplayDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextDisplayDimension.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
