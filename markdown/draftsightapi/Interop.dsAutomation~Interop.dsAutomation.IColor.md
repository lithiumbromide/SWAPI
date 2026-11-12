---
title: "IColor Interface"
project: ""
interface: "IColor"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IColor.html"
---

# IColor Interface

Allows access to LineColors, TextColors, and background Colors.

## Syntax

### Visual Basic

```vb
Public Interface IColor
```

### C#

```csharp
public interface IColor
```

### JScript

```
public interface IColor
```

### Managed Extensions for C++

```
public __gc __interface IColor
```

### C++/CLI

```cpp
public interface class IColor
```

## Examples

[Construct Line (C#)](Construct_Line_Example_CSharp.htm)
[Construct Line (VB.NET)](Construct_Line_Example_VBNET.htm)
[Construct Line (VBA)](Construct_Line_Example_VBA.htm)
[Create and Apply DimensionStyle (C#)](Create_and_Apply_DimensionStyle_Example_CSharp.htm)
[Create and Apply DimensionStyle (VB.NET)](Create_and_Apply_DimensionStyle_Example_VBNET.htm)
[Create and Apply DimensionStyle (VBA)](Create_and_Apply_DimensionStyle_Example_VBA.htm)
[Create Circles on Different Layers (JavaScript)](Create_Circles_on_Different_Layers_Example_JS.htm)
[Insert Splines (JavaScript)](Insert_Splines_Example_JS.htm)
[Insert Splines (C#)](Insert_Splines_Example_CSharp.htm)
[Insert Splines (VB.NET)](Insert_Splines_Example_VBNET.htm)
[Insert Splines (VBA)](Insert_Splines_Example_VBA.htm)

## Remarks

To change the color of an entity that allows access to its Color:

1. Get the entity's Color object.
2. Call [IColor::SetByColor](Interop.dsAutomation~Interop.dsAutomation.IColor~SetByColor.html), [IColor::SetColorByIndex](Interop.dsAutomation~Interop.dsAutomation.IColor~SetColorByIndex.html), [IColor::SetNamedColor](Interop.dsAutomation~Interop.dsAutomation.IColor~SetNamedColor.html), or [IColor::SetRGBColor](Interop.dsAutomation~Interop.dsAutomation.IColor~SetRGBColor.html) to change the color of that instance of the Color object.
3. Update the entity's Color object using the updated Color object.

The examples linked to this Help topic demonstrate how to change the color of a Line.

## Accessors

[IApplication::GetColorByIndex](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetColorByIndex.html)

[IApplication::GetNamedColor](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetNamedColor.html)

[IApplication::GetRGBColor](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetRGBColor.html)

[IApplicationOptions::GetElementColor](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~GetElementColor.html)

[IAttributeDefinition::Color](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~Color.html)

[IAttributeInstance::Color](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~Color.html)

[IBlockInstance::Color](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~Color.html)

[ICircle::Color](Interop.dsAutomation~Interop.dsAutomation.ICircle~Color.html)

[ICircleArc::Color](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~Color.html)

[IColorPicker::GetColor](Interop.dsAutomation~Interop.dsAutomation.IColorPicker~GetColor.html)

[ICurvedSettings::Color](Interop.dsAutomation~Interop.dsAutomation.ICurvedSettings~Color.html)

[IDgnReference::Color](Interop.dsAutomation~Interop.dsAutomation.IDgnReference~Color.html)

[IDimensionStyleLineOptions::DimensionLineColor](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLineOptions~DimensionLineColor.html)

[IDimensionStyleTextOptions::Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html)

[IDimensionStyleTextOptions::FillColor](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleTextOptions~FillColor.html)

[IEllipseArc::Color](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~Color.html)

[IEmbeddedObject::Color](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~Color.html)

[IEntityHelper::GetColor](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~GetColor.html)

[IExtrudedSurface::Color](Interop.dsAutomation~Interop.dsAutomation.IExtrudedSurface~Color.html)

[IExtrusion::Color](Interop.dsAutomation~Interop.dsAutomation.IExtrusion~Color.html)

[IFace::Color](Interop.dsAutomation~Interop.dsAutomation.IFace~Color.html)

[IGeneralDimension::Color](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~Color.html)

[IGradientBackground::BottomColor](Interop.dsAutomation~Interop.dsAutomation.IGradientBackground~BottomColor.html)

[IGradientBackground::MiddleColor](Interop.dsAutomation~Interop.dsAutomation.IGradientBackground~MiddleColor.html)

[IGradientBackground::TopColor](Interop.dsAutomation~Interop.dsAutomation.IGradientBackground~TopColor.html)

[IHatch::Color](Interop.dsAutomation~Interop.dsAutomation.IHatch~Color.html)

[IInfiniteLine::Color](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~Color.html)

[ILayer::Color](Interop.dsAutomation~Interop.dsAutomation.ILayer~Color.html)

[ILayer::GetColorInViewport](Interop.dsAutomation~Interop.dsAutomation.ILayer~GetColorInViewport.html)

[ILayerProperties::LineColor](Interop.dsAutomation~Interop.dsAutomation.ILayerProperties~LineColor.html)

[ILeader::Color](Interop.dsAutomation~Interop.dsAutomation.ILeader~Color.html)

[ILine::Color](Interop.dsAutomation~Interop.dsAutomation.ILine~Color.html)

[ILoft::Color](Interop.dsAutomation~Interop.dsAutomation.ILoft~Color.html)

[ILoftedSurface::Color](Interop.dsAutomation~Interop.dsAutomation.ILoftedSurface~Color.html)

[INote::BackgroundFillColor](Interop.dsAutomation~Interop.dsAutomation.INote~BackgroundFillColor.html)

[INote::Color](Interop.dsAutomation~Interop.dsAutomation.INote~Color.html)

[IPdfReference::Color](Interop.dsAutomation~Interop.dsAutomation.IPdfReference~Color.html)

[IPoint::Color](Interop.dsAutomation~Interop.dsAutomation.IPoint~Color.html)

[IPolyFaceMesh::Color](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~Color.html)

[IPolygonMesh::Color](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~Color.html)

[IPolyLine::Color](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Color.html)

[IPolyLine3D::Color](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~Color.html)

[IRay::Color](Interop.dsAutomation~Interop.dsAutomation.IRay~Color.html)

[IReferenceImage::Color](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~Color.html)

[IRegion::Color](Interop.dsAutomation~Interop.dsAutomation.IRegion~Color.html)

[IRevolve::Color](Interop.dsAutomation~Interop.dsAutomation.IRevolve~Color.html)

[IRevolvedSurface::Color](Interop.dsAutomation~Interop.dsAutomation.IRevolvedSurface~Color.html)

[IRichLine::Color](Interop.dsAutomation~Interop.dsAutomation.IRichLine~Color.html)

[IRichLineStyle::GetLineColor](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~GetLineColor.html)

[IShape::Color](Interop.dsAutomation~Interop.dsAutomation.IShape~Color.html)

[ISimpleNote::Color](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~Color.html)

[ISolid::Color](Interop.dsAutomation~Interop.dsAutomation.ISolid~Color.html)

[ISolid3D::Color](Interop.dsAutomation~Interop.dsAutomation.ISolid3D~Color.html)

[ISolidBackground::Color](Interop.dsAutomation~Interop.dsAutomation.ISolidBackground~Color.html)

[ISpline::Color](Interop.dsAutomation~Interop.dsAutomation.ISpline~Color.html)

[ISweep::Color](Interop.dsAutomation~Interop.dsAutomation.ISweep~Color.html)

[ISweptSurface::Color](Interop.dsAutomation~Interop.dsAutomation.ISweptSurface~Color.html)

[ITable::Color](Interop.dsAutomation~Interop.dsAutomation.ITable~Color.html)

[ITable::GetBackgroundColor](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBackgroundColor.html)

[ITable::GetBordersColor](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersColor.html)

[ITable::GetCellBackgroundColor](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBackgroundColor.html)

[ITable::GetCellBordersColor](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersColor.html)

[ITable::GetCellTextColor](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextColor.html)

[ITable::GetTextColor](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextColor.html)

[ITableStyle::GetBackgroundColor](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetBackgroundColor.html)

[ITableStyle::GetBordersColor](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetBordersColor.html)

[ITableStyle::GetTextColor](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetTextColor.html)

[ITolerance::Color](Interop.dsAutomation~Interop.dsAutomation.ITolerance~Color.html)

[ITolerance::DimensionLineColor](Interop.dsAutomation~Interop.dsAutomation.ITolerance~DimensionLineColor.html)

[ITolerance::TextColor](Interop.dsAutomation~Interop.dsAutomation.ITolerance~TextColor.html)

[ITrace::Color](Interop.dsAutomation~Interop.dsAutomation.ITrace~Color.html)

[IUnknownEntity::Color](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity~Color.html)

[IViewport::Color](Interop.dsAutomation~Interop.dsAutomation.IViewport~Color.html)

## Access Diagram

DSObjectModel.pdf#Color

[Color](DSObjectModel.pdf#Color)

## See Also

[IColor Members](Interop.dsAutomation~Interop.dsAutomation.IColor_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IColorPicker Interface](Interop.dsAutomation~Interop.dsAutomation.IColorPicker.html)
