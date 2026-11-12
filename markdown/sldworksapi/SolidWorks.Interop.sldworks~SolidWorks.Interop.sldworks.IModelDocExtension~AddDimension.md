---
title: "AddDimension Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "AddDimension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDimension.html"
---

# AddDimension Method (IModelDocExtension)

Creates a display dimension at the specified location for selected entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddDimension( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal Direction As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Direction As System.Integer
Dim value As System.Object

value = instance.AddDimension(X, Y, Z, Direction)
```

### C#

```csharp
System.object AddDimension(
   System.double X,
   System.double Y,
   System.double Z,
   System.int Direction
)
```

### C++/CLI

```cpp
System.Object^ AddDimension(
   System.double X,
   System.double Y,
   System.double Z,
   System.int Direction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X coordinate of display dimension text
- `Y`: Y coordinate of display dimension text
- `Z`: Z coordinate of display dimension text
- `Direction`: Direction of dimensioning extension line or rapid dimensioning quadrant as defined in [swSmartDimensionDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSmartDimensionDirection_e.html) (see **Remarks**)

### Return Value

[IDisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)

## VBA Syntax

See [ModelDocExtension::AddDimension](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~AddDimension.html).

## Examples

[Create Angular Dimension (VBA)](Create_Angular_Dimension_Example_VB.htm)
[Create Angular Dimension (VB.NET)](Create_Angular_Dimension_Example_VBNET.htm)
[Create Angular Dimension (C#)](Create_Angular_Dimension_Example_CSharp.htm)

## Remarks

The X, Y, and Z coordinates of the display dimension text must be appropriate for the specified Direction, or this method fails to add the display dimension.

For parts, Direction specifies the dimensioning manipulator direction that appears in the user interface when an extension line is needed to unambiguously define what to dimension.

For drawings, Direction specifies the rapid dimensioning selector quadrant to which to add the display dimension.

Before calling this method, you must select the entities for which to add a display dimension. Entities must be selected by location and not name. If you specify line names instead of coordinates, the dimensioning routines randomly pick locations on the lines, which can yield unpredictable results during angular dimension creation.

For example, to create an angular dimension between two lines:

1. Call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select a sketch segment of the angle you want to dimension, specifying the line's X, Y, and Z coordinates.
2. Call IModelDocExtension::SelectByID2 to select the vertex of the angle you want to dimension, specifying the vertex's X, Y, and Z coordinates.
3. Call this method, specifying the X, Y, Z coordinates of the display dimension text and the Direction of the extension line that is needed to unambiguously define the angle to dimension.

If the pre-selected entities unambiguously define what you wish to dimension, then no extension lines are needed. In that case, call [IModelDoc2::AddDimension2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddDimension2.html) instead of this method.

**NOTE:** To change the angle in an angular dimension to its supplementary angle, use [IDisplayDimension::SupplementaryAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SupplementaryAngle.html).

You should only use this method on visible documents. Before using this method, use [ISldWorks::Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~Visible.html) to check whether a document is visible.

Before calling this method, you might want to call [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html) with [swUserPreferenceToggle_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.html).swInputDimValOnCreate to suppress the dialog box that allows the user to type the dimension value.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDoc2::AddDiameterDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddDiameterDimension2.html)
[IModelDoc2::IAddDiameterDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddDiameterDimension2.html)
[IModelDoc2::AddHorizontalDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddHorizontalDimension2.html)
[IModelDoc2::IAddHorizontalDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddHorizontalDimension2.html)
[IModelDoc2::AddRadialDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddRadialDimension2.html)
[IModelDoc2::IAddRadialDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddRadialDimension2.html)
[IModelDoc2::AddVerticalDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddVerticalDimension2.html)
[IModelDoc2::IAddVerticalDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddVerticalDimension2.html)
[IModelDocExtension::AddSymmetricDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddSymmetricDimension.html)
[IModelDocExtension::AddSpecificDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddSpecificDimension.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
