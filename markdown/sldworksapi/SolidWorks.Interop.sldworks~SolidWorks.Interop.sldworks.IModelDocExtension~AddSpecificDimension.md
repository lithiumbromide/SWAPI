---
title: "AddSpecificDimension Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "AddSpecificDimension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddSpecificDimension.html"
---

# AddSpecificDimension Method (IModelDocExtension)

Creates the specified display dimension at the specified location for selected entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddSpecificDimension( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal DimensionType As System.Integer, _
   ByRef Error As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim DimensionType As System.Integer
Dim Error As System.Integer
Dim value As System.Object

value = instance.AddSpecificDimension(X, Y, Z, DimensionType, Error)
```

### C#

```csharp
System.object AddSpecificDimension(
   System.double X,
   System.double Y,
   System.double Z,
   System.int DimensionType,
   out System.int Error
)
```

### C++/CLI

```cpp
System.Object^ AddSpecificDimension(
   System.double X,
   System.double Y,
   System.double Z,
   System.int DimensionType,
   [Out] System.int Error
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X coordinate of display dimension text
- `Y`: Y coordinate of display dimension text
- `Z`: Z coordinate of display dimension text
- `DimensionType`: Type of dimension to add as defined in [swDimensionType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDimensionType_e.html) (see **Remarks**)
- `Error`: Result status as defined in [swAddSpecificDimension_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAddSpecificDimension_e.html)

### Return Value

[IDisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html) (see **Remarks**)

## VBA Syntax

See [ModelDocExtension::AddSpecificDimension](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~AddSpecificDimension.html).

## Examples

[Create Specific Dimension in a Sketch (VBA)](Create_Specific_Dimension_Example_VB.htm)
[Create Specific Dimension in a Sketch (VB.NET)](Create_Specific_Dimension_Example_VBNET.htm)
[Create Specific Dimension in a Sketch (C#)](Create_Specific_Dimension_Example_CSharp.htm)

## Remarks

This method adds specific display dimensions to sketches and drawings. It supports the following from swDimensionType_e:

- swAngularDimension
- swChamferDimension
- swDiameterDimension
- swDiametricLinearDimension
- swHorLinearDimension
- swOrdinateDimension
- swRadialDimension
- swRadialLinearDimension
- swVertLinearDimension

If you specify DimensionType with swDimensionType_e.:

- swDiametricLinearDimension, then this method creates a double-distance linear dimension for a selected construction/center line, circle/arc edge/center. After creation, use [IDisplayDimension::Diametric](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Diametric.html) to display the single-distance linear dimension.
- swRadialLinearDimension, then this method creates a single-distance linear dimension for a selected construction/center line, circle/arc edge/center. After creation, use IDisplayDimension::Diametric to display the double-distance linear dimension.

Before calling this method, you must select the entities to dimension.

For example, to create an angular dimension between two intersecting lines in a drawing:

1. Call [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.html), specifying the X, Y, and Z coordinates of a ray of the angle you want to dimension.
2. Call IModelDocExtension::SelectByRay, specifying the X, Y, and Z coordinates of the other ray of the angle you want to dimension.
3. Call this method, specifying X, Y, and Z with the location coordinates of the display dimension text and specifying DimensionType with swDimensionType_e.swAngularDimension.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::AddDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDimension.html)
[IModelDocExtension::AddSymmetricDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddSymmetricDimension.html)
[IModelDoc2::AddDiameterDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddDiameterDimension2.html)
[IModelDoc2::AddHorizontalDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddHorizontalDimension2.html)
[IModelDoc2::AddRadialDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddRadialDimension2.html)
[IModelDoc2::AddVerticalDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddVerticalDimension2.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
