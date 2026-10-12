---
title: "IDisplayDimension Interface"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html"
---

# IDisplayDimension Interface

Represents instances of dimensions displayed in [parts](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html), [assemblies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc.html), [drawings](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc.html) and [sensors](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISensor.html).

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IDisplayDimension
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
```

### C#

```csharp
public interface IDisplayDimension
```

### C++/CLI

```cpp
public interface class IDisplayDimension
```

## VBA Syntax

See [DisplayDimension](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension.html).

## Examples

[Get Chamfer Display Dimension (C#)](Get_Chamfer_Display_Dimension_Example_CSharp.htm)
[Get Chamfer Display Dimension (VB.NET)](Get_Chamfer_Display_Dimension_Example_VBNET.htm)
[Get Chamfer Display Dimension (VBA)](Get_Chamfer_Display_Dimension_Example_VB.htm)
[Get and Set Sensor (C#)](Get_and_Set_Sensor_Example_CSharp.htm)
[Get and Set Sensor (VB.NET)](Get_and_Set_Sensor_Example_VBNET.htm)
[Get and Set Sensor (VBA)](Get_and_Set_Sensor_Example_VB.htm)
[Get DimXpert Display Dimensions and Feature (C#)](Get_DimXpert_Display_Dimensions_and_Feature_Example_CSharp.htm)
[Get DimXpert Display Dimensions and Feature (VB.NET)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VBNET.htm)
[Get DimXpert Display Dimensions and Feature (VBA)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VB.htm)
[Set Properties of Angular Running Dimension (VBA)](Set_Properties_of_Angular_Running_Dimension_Example_VB.htm)
[Set Properties of Angular Running Dimension (VB.NET)](Set_Properties_of_Angular_Running_Dimension_Example_VBNET.htm)
[Set Properties of Angular Running Dimension (C#)](Set_Properties_of_Angular_Running_Dimension_Example_CSharp.htm)

## Remarks

You can display a SOLIDWORKS dimension more than once. For example, you can bring the base-extrude dimension into three different views on a drawing. These three dimensions are referred to as display dimensions and are represented by the DisplayDimension object in the SOLIDWORKS API. The original base-extrude dimension is represented by the [Dimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension.html) object in the SOLIDWORKS API.

SOLIDWORKS stores many of the properties associated with a dimension with the underlying Dimension object. For example, you must get the Dimension object using [IDisplayDimension::GetDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetDimension.html) to access or modify the underlying dimension value.

## Accessors

[IAnnotation::GetSpecificAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetSpecificAnnotation.html) and [IAnnotation::IGetSpecificAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~IGetSpecificAnnotation.html)

[IDisplayDimension::GetNext5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetNext5.html)

[IDrawingDoc::AddChamferDim](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~AddChamferDim.html) and [IDrawingDoc::IAddChamferDim](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~IAddChamferDim.html)

[IDrawingDoc::AddHoleCallout2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~AddHoleCallout2.html) and [IDrawingDoc::IAddHoleCallout2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~IAddHoleCallout2.html)

[IDrawingDoc::CreateAngDim4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateAngDim4.html) and [IDrawingDoc::ICreateAngDim4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~ICreateAngDim4.html)

[IDrawingDoc::CreateDiamDim4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateDiamDim4.html) and [IDrawingDoc::ICreateDiamDim4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~ICreateDiamDim4.html)

[IDrawingDoc::CreateLinearDim4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~ICreateLinearDim4.html)

[IDrawingDoc::CreateOrdinateDim4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateOrdinateDim4.html) and [IDrawingDoc::ICreateOrdinateDim4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~ICreateOrdinateDim4.html)

[IEnumDisplayDimensions::Next](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumDisplayDimensions~Next.html)

[IFeature::EnumDisplayDimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~EnumDisplayDimensions.html)

[IFeature::GetDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDisplayDimension.html)

[IFeature::GetFirstDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetFirstDisplayDimension.html)

[IFeature::GetNextDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetNextDisplayDimension.html)

SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndReference.html

[ILinearPatternFeatureData::D1Axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1Axis.html)

[ILinearPatternFeatureData::D2Axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2Axis.html)

[ILocalLinearPatternFeatureData::D1Axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1Axis.html)

[ILocalLinearPatternFeatureData::D2Axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2Axis.html)

[IMacroFeatureData::GetDisplayDimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~GetDisplayDimensions.html) and [IMacroFeatureData::IGetDisplayDimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~IGetDisplayDimensions.html)

[IMate2::DisplayDimension2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMate2~DisplayDimension2.html)

[IModelDoc2::AddDiameterDimension2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddDiameterDimension2.html) and [IModelDoc2::IAddDiameterDimension2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IAddDiameterDimension2.html)

[IModelDoc2::AddHorizontalDimension2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddHorizontalDimension2.html) and [IModelDoc2::IAddHorizontalDimension2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IAddHorizontalDimension2.html)

[IModelDoc2::AddRadialDimension2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddRadialDimension2.html) and [IModelDoc2::IAddRadialDimension2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IAddRadialDimension2.html)

[IModelDoc2::AddVerticalDimension2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddVerticalDimension2.html) and [IModelDoc2::IAddVerticalDimension2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IAddVerticalDimension2.html)

[IModelDocExtension::AddDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDimension.html)

[IModelDocExtension::AddPathLengthDim](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~AddPathLengthDim.html)

[IModelDocExtension::AddSpecificDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddSpecificDimension.html)

[IModelDocExtension::AddSymmetricDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddSymmetricDimension.html)

[IModelDocExtension::InsertChainDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertChainDimensions.html)

[ISketchBlockDefinition::GetDisplayDimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~GetDisplayDimensions.html) and [ISketchBlockDefinition::IGetDisplayDimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~IGetDisplayDimensions.html)

[ISketchManager::AddAlongXDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~AddAlongXDimension.html), [ISketchManager::AddAlongYDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~AddAlongYDimension.html), and [ISketchManager::AddAlongZDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~AddAlongZDimension.html)

[ISketchRelation::GetDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation~GetDisplayDimension.html)

[IView::GetFirstDisplayDimension5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstDisplayDimension5.html)

[IView::GetDisplayDimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetDisplayDimensions.html) and [IView::IGetDisplayDimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetDisplayDimensions.html)

## Access Diagram

[DisplayDimension](SWObjectModel.pdf#DisplayDimension)

## See Also

[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.html)
[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.html)
