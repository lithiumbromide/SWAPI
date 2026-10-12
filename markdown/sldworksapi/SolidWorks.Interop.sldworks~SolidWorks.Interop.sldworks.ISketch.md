---
title: "ISketch Interface"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html"
---

# ISketch Interface

Allows access to sketch entities and to extract information about sketch elements, the sketch orientation, and so on.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISketch
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
```

### C#

```csharp
public interface ISketch
```

### C++/CLI

```cpp
public interface class ISketch
```

## VBA Syntax

See [Sketch](ms-its:sldworksapivb6.chm::/sldworks~Sketch.html).

## Examples

[Get Spline Points (C++)](Get_Spline_Points_Example_CPlusPlus_COM.htm)
[Get Spline's Parameters (C#)](Get_Spline's_Parameters_Example_CSharp.htm)
[Get Spline's Parameters (VB.NET)](Get_Spline's_Parameters_Example_VBNET.htm)
[Get Spline's Parameters (VBA)](Get_Spline's_Parameters_Example_VB.htm)
[Create Imported Surface Body from Sketch (C#)](Create_Imported_Surface_Body_from_Sketch_Example_CSharp.htm)
[Delete All Constraints in Selected Sketch (VBA)](Delete_All_Constraints_in_Selected_Sketch_Example_VB.htm)
[Transform Sketch to Model (VBA)](Transform_Sketch_to_Model_Example_VB.htm)
[Open and Exit Sketch (VBA)](Open_and_Exit_Sketch_Example_VB.htm)

## Remarks

A sketch is typically used in [part](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html) or [assembly](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc.html) documents to generate a solid body or such subsequent [features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) as a cut or boss. A sketch is also used in [drawing](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc.html) documents whenever the user constructs individual lines, arcs, and so on, on a drawing [sheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet.html) or in a drawing [view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html).

## Accessors

[IBoundaryBossFeatureData::D1Curves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D1Curves.html)

[IBoundaryBossFeatureData::D2Curves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D2Curves.html)

[IChainPatternFeatureData::Path](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Path.html)

[ICosmeticWeldBeadFeatureData::GetEntitiesWeldPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntitiesWeldPath.html)

[ICurveDrivenPatternFeatureData::D1Direction](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D1Direction.html)

[ICurveDrivenPatternFeatureData::D2Direction](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D2Direction.html)

[IDomeFeatureData2::ConstraintPointOrSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDomeFeatureData2~ConstraintPointOrSketch.html)

[IFeature::GetSpecificFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetSpecificFeature2.html)

[ILocalCurvePatternFeatureData::D1Direction](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalCurvePatternFeatureData~D1Direction.html)

[ILocalCurvePatternFeatureData::D2Direction](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalCurvePatternFeatureData~D2Direction.html)

[ILocalSketchPatternFeatureData::Sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalSketchPatternFeatureData~Sketch.html)

[IModelDoc2::GetActiveSketch2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetActiveSketch2.html) and [IModelDoc2::IGetActiveSketch2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetActiveSketch2.html)

[INote::GetSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetSketch.html) or [INote::IGetSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~IGetSketch.html)

[IProfileGroupFolder::GetSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder~GetSketch.html)

[ISheet::GetTemplateSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet~GetTemplateSketch.html)

[ISketchBlockDefinition::GetSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~GetSketch.html)

[ISketchBlockInstance::GetSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~GetSketch.html)

[ISketchContour::Sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchContour~Sketch.html)

[ISketchHatch::GetSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchHatch~GetSketch.html)

[ISketchPath::GetSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPath~GetSketch.html)

[ISketchPatternFeatureData::Sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPatternFeatureData~Sketch.html)

[ISketchPoint::GetSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint~GetSketch.html)

[ISketchRegion::Sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRegion~Sketch.html)

[ISketchSegment::GetSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~GetSketch.html)

[ISplitLineFeatureData::GetSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitLineFeatureData~Sketch.html)

[IStructureSystemMemberProfile::GetSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~GetSketch.html)

[ISweptFlangeFeatureData::Path](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~Path.html)

[ISweptFlangeFeatureData::Profile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~Profile.html)

[IView::GetCenterLineSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetCenterLineSketch.html)

[IView::GetSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetSketch.html) and [IView::IGetSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetSketch.html)

[IWrapSketchFeatureData::GetSourceSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWrapSketchFeatureData~SourceSketch.html)

## Access Diagram

[Sketch](SWObjectModel.pdf#Sketch)

## See Also

[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ISketchArc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.html)
[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchContour Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.html)
[ISketchedBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.html)
[ISketchEllipse Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse.html)
[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html)
[ISketchLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html)
[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchParabola Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola.html)
[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html)
[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)
[ISketchRegion Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion.html)
[ISketchRelation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.html)
[ISketchRelationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager.html)
[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchText Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText.html)
