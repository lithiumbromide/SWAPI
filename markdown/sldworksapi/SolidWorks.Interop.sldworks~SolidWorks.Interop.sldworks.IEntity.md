---
title: "IEntity Interface"
project: "SOLIDWORKS API Help"
interface: "IEntity"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.html"
---

# IEntity Interface

Allows access to an attribute instance that is stored on an entity.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IEntity
```

### Visual Basic (Usage)

```vb
Dim instance As IEntity
```

### C#

```csharp
public interface IEntity
```

### C++/CLI

```cpp
public interface class IEntity
```

## VBA Syntax

See [Entity](ms-its:sldworksapivb6.chm::/sldworks~Entity.html).

## Examples

[Get Offset Surface Data (C#)](Get_Offset_Surface_Data_Example_CSharp.htm)
[Get Offset Surface Data (VB.NET)](Get_Offset_Surface_Data_Example_VBNET.htm)
[Get Offset Surface Data (VBA)](Get_Offset_Surface_Data_Example_VB.htm)
[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)
[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)
[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

## Remarks

In Microsoft Visual Studio 2008/MFC 9.0 or later, Microsoft added a new interface called IEntity. Your add-in might not compile if it uses both this interface and the SOLIDWORKS IEntity interface.

Possible errors are:

- error C3121: cannot change GUID for class 'IEntity'
- error C2011: 'IEntity' : 'struct' type redefinition
- undefined symbol errors when linking add-ins that do a QueryInterface on IEntity

To avoid errors, you can:

- Include the namespace when declaring an IEntity variable:

SldWorks::IEntity ent

- Rename IEntity by adding the rename function to the import of **sldworks.tlb**:
  #import "sldworks.tlb" rename("IEntity", "SWEntity")

and do any of the following:

- use SWEntity instead of IEntity in your code
- do a QueryInterface using the GUID constant of the renamed interface:

pFace->QueryInterface(**IID_SWEntity**, (LPVOID*)&entity);

- do a QueryInterface using a GUID lookup of the renamed interface:

pFace->QueryInterface**(__uuidof(SWEntity),** (LPVOID*)&entity);

## Accessors

[IAttribute::GetEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute~GetEntity.html)

[IAttribute::IGetEntity2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute~IGetEntity2.html)

[IBrokenOutSectionFeatureData::DepthReference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBrokenOutSectionFeatureData~DepthReference.html)

[ICoincidentMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData~EntitiesToMate.html)

[IComponent2::GetCorrespondingEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetCorrespondingEntity.html) and [IComponent2::IGetCorrespondingEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IGetCorrespondingEntity.html)

[IDraftFeatureData2::GetDraftEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDraftFeatureData2~GetDraftedEntities.html) and [IDraftFeatureData2::IGetDraftEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDraftFeatureData2~IGetDraftedEntities.html)

[IEntity::GetSafeEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity~GetSafeEntity.html)

[IFaultEntity::Entity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFaultEntity~Entity.html)

[IHoleSeriesFeatureData2::GetHoleBottomMateEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~GetHoleBottomMateEntity.html) and [IHoleSeriesFeatureData2::IGetHoleBottomMateEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~IGetHoleBottomMateEntity.html)

[IHoleSeriesFeatureData2::GetHoleTopMateEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~GetHoleTopMateEntity.html) and [IHoleSeriesFeatureData2::IGetHoleTopMateEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~IGetHoleTopMateEntity.html)

[IMateReference::ReferenceEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateReference~ReferenceEntity.html)

[IModelDocExtension::GetCorrespondingEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity.html)

[IMotionPlotAxisFeatureData::Entities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMotionPlotAxisFeatureData~Entities.html)

[IPartDoc::GetEntityByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~GetEntityByName.html) and [IPartDoc::IGetEntityByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~IGetEntityName.html)

[IPartDoc::GetNamedEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~GetNamedEntities.html) and [IPartDoc::IGetNamedEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~IGetNamedEntities.html)

[ISurfaceOffsetFeatureData::Entities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceOffsetFeatureData~Entities.html)

[ISurfaceOffsetFeatureData::IGetEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceOffsetFeatureData~IGetEntities.html)

[IView::GetCorrespondingEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCorrespondingEntity.html)

[IView::GetVisibleEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetVisibleEntities.html) and [IView::IGetVisibleEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetVisibleEntities.html)

## Access Diagram

[Entity](SWObjectModel.pdf#Entity)

## See Also

[IEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
