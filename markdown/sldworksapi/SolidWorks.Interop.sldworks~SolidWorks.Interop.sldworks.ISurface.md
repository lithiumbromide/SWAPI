---
title: "ISurface Interface"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html"
---

# ISurface Interface

Used as the underlying definition of a face.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISurface
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
```

### C#

```csharp
public interface ISurface
```

### C++/CLI

```cpp
public interface class ISurface
```

## VBA Syntax

See [Surface](ms-its:sldworksapivb6.chm::/sldworks~Surface.html).

## Examples

[Get B-Spline Surface Parameterization Data (C#)](Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm)
[Get B-Spline Surface Parameterization Data (VB.NET)](Get_B-Spline_Surface_Parameterization_Data_Example_VBNET.htm)
[Get B-Spline Surface Parameterization Data (VBA)](Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm)
[Get Surface Type (VBA)](Get_Surface_Type_Example_VB.htm)
[Evaluate Points on Surface (VBA)](Evaluate_Points_on_Surface_Example_VB.htm)

## Remarks

This interface allows you to get the surface type and various surface definition data as well as evaluate and reverse evaluate locations on the surface.

## Accessors

[IAdvancedHoleElementData::SelectionEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~SelectionEntity.html)

[IBody2::CreateBlendSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateBlendSurface.html) and [IBody2::ICreateBlendSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateBlendSurface.html)

[IBody2::CreateBsplineSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateBsplineSurface.html) and [IBody2::ICreateBsplineSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateBsplineSurface.html)

[IBody2::CreateExtrusionSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateExtrusionSurface.html) and [IBody2::ICreateExtrusionSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateExtrusionSurface.html)

[IBody2::CreateNewSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateNewSurface.html) and [IBody2::ICreateNewSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateNewSurface.html)

[IBody2::CreateOffsetSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateOffsetSurface.html) and [IBody2::ICreateOffsetSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateOffsetSurface.html)

[IBody2::CreatePlanarSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreatePlanarSurface.html) and [IBody2::ICreatePlanarSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreatePlanarSurface.html)

[IBody2::CreateRevolutionSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateRevolutionSurface.html) and [IBody2::ICreateRevolutionSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateRevolutionSurface.html)

[IBody2::CreateRuledSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateRuledSurface.html) and [IBody2::ICreateRuledSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateRuledSurface.html)

[IBody2::ICreateExtrusionSurfaceDLL](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateExtrusionSurfaceDLL.html)

[IBody2::ICreatePlanarSurfaceDLL](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreatePlanarSurfaceDLL.html)

[IBody2::ICreatePsplineSurfaceDLL](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreatePsplineSurfaceDLL.html)

[IBody2::ICreateRevolutionSurfaceDLL](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateRevolutionSurfaceDLL.html)

[ICoincidentMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData~EntitiesToMate.html)

[IConcentricMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData~EntitiesToMate.html)

[IFace2::GetSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetSurface.html) and [IFace2::IGetSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetSurface.html)

[IHingeMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~EntitiesToMate.html)

[IIntersectFeatureData::GetIntersectionsTools](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IIntersectFeatureData~GetIntersectionsTools.html)

[ILinearPatternFeatureData::D1Axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1Axis.html)

[ILinearPatternFeatureData::D2Axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2Axis.html)

[ILocalLinearPatternFeatureData::D1Axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1Axis.html)

[ILocalLinearPatternFeatureData::D2Axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2Axis.html)

[IModeler::CreateBsplineSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateBsplineSurface.html) and [IModeler::ICreateBsplineSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateBsplineSurface.html)

[IModeler::CreateConicalSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateConicalSurface2.html) and [IModeler::ICreateConicalSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateConicalSurface2.html)

[IModeler::CreateCoonsBSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateCoonsBSurface.html)

[IModeler::CreateCylindricalSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateCylindricalSurface2.html) and [IModeler::ICreateCylindricalSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateCylindricalSurface2.html)

[IModeler::CreateExtrusionSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateExtrusionSurface.html) and [IModeler::ICreateExtrusionSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateExtrusionSurface.html)

[IModeler::CreateLoftSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateLoftSurface.html) and [IModeler::ICreateLoftSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateLoftSurface.html)

[IModeler::CreateOffsetSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateOffsetSurface.html) and [IModeler::ICreateOffsetSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateOffsetSurface.html)

[IModeler::CreatePlanarSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreatePlanarSurface2.html) and [IModeler::ICreatePlanarSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreatePlanarSurface2.html)

[IModeler::CreateRuledSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateRuledSurface.html) and [IModeler::ICreateRuledSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateRuledSurface.html)

[IModeler::CreateSphericalSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateSphericalSurface2.html) and [IModeler::ICreateSphericalSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateSphericalSurface2.html)

[IModeler::CreateSweptSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateSweptSurface.html)

[IModeler::CreateToroidalSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateToroidalSurface.html)

[IMoveFaceFeatureData::GetEndConditionEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~GetEndConditionEntity.html)

[IMoveFaceFeatureData::GetFromEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~GetFromEntity.html)

[IPrimaryMemberFacePlaneIntersectionFeatureData::GetIntersectingPlanesAndFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData~GetIntersectingPlanesAndFaces.html)

[IRackPinionMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData~EntitiesToMate.html)

[IStructureSystemMemberProfile::ProfileAlignmentObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileAlignmentObject.html)

[ISurface::Copy](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~Copy.html) and [ISurface::ICopy](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~ICopy.html)

[ISurface::GetOffsetSurfParams2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~GetOffsetSurfParams2.html) and [ISurface::IGetOffsetSurfParams2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IGetOffsetSurfParams2.html)

[ISurfaceFlattenFeatureData::Faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~Faces.html)

[ISweepFeatureData::EndDirectionVector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~EndDirectionVector.html)

[ISweepFeatureData::StartDirectionVector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~StartDirectionVector.html)

[IThreadFeatureData::GetEndConditionReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~GetEndConditionReference.html)

[IThreadFeatureData::StartEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~StartEntity.html)

## Access Diagram

[Surface](SWObjectModel.pdf#Surface)

## See Also

[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
