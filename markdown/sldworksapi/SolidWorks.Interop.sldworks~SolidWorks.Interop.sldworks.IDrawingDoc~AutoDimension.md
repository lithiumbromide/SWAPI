---
title: "AutoDimension Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "AutoDimension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutoDimension.html"
---

# AutoDimension Method (IDrawingDoc)

Automatically dimensions the selected drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function AutoDimension( _
   ByVal EntitiesToDimension As System.Integer, _
   ByVal HorizontalScheme As System.Integer, _
   ByVal HorizontalPlacement As System.Integer, _
   ByVal VerticalScheme As System.Integer, _
   ByVal VerticalPlacement As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim EntitiesToDimension As System.Integer
Dim HorizontalScheme As System.Integer
Dim HorizontalPlacement As System.Integer
Dim VerticalScheme As System.Integer
Dim VerticalPlacement As System.Integer
Dim value As System.Integer

value = instance.AutoDimension(EntitiesToDimension, HorizontalScheme, HorizontalPlacement, VerticalScheme, VerticalPlacement)
```

### C#

```csharp
System.int AutoDimension(
   System.int EntitiesToDimension,
   System.int HorizontalScheme,
   System.int HorizontalPlacement,
   System.int VerticalScheme,
   System.int VerticalPlacement
)
```

### C++/CLI

```cpp
System.int AutoDimension(
   System.int EntitiesToDimension,
   System.int HorizontalScheme,
   System.int HorizontalPlacement,
   System.int VerticalScheme,
   System.int VerticalPlacement
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntitiesToDimension`: Entities to dimension as defined in [swAutodimEntities_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAutodimEntities_e.html)
- `HorizontalScheme`: Horizontal dimensioning scheme as defined in [swAutodimScheme_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAutodimScheme_e.html)
- `HorizontalPlacement`: Placement relative to the drawing view as defined in [swAutodimHorizontalPlacement_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAutodimHorizontalPlacement_e.html)
- `VerticalScheme`: Vertical dimensioning scheme as defined in [swAutodimScheme_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAutodimScheme_e.html)
- `VerticalPlacement`: Placement relative to the drawing view as defined in [swAutodimVerticalPlacement_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAutodimVerticalPlacement_e.html)

### Return Value

swAutodimStatusSuccess if the view is automatically dimensioned; see [swAutodimStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAutodimStatus_e.html) for reasons for possible failures

## VBA Syntax

See [DrawingDoc::AutoDimension](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~AutoDimension.html).

## Examples

[Autodimension Selected Drawing View (C#)](Autodimension_Selected_Drawing_View_Example_CSharp.htm)
[Autodimension Selected Drawing View (VB.NET)](Autodimension_Selected_Drawing_View_Example_VBNET.htm)
[Autodimension Selected Drawing View (VBA)](Autodimension_Selected_Drawing_View_Example_VB.htm)

## Remarks

This method requires information about the:

- drawing view to autodimension. This information can be supplied by selecting the drawing view to use. No mark is necessary.

  If a drawing view is not selected, then this method attempts to determine the drawing view information from the other entities that are selected. If no other selections exist, then this method defaults to using the first drawing view, which is consistent with how the SOLIDWORKS Design user interface works.
- datums to use for the dimensioning baseline. These can be supplied by selecting a vertical edge, vertical sketch line, vertex, or sketch point as the datum for the horizontal dimensioning scheme. Mark the selection with swAutodimMarkHorizontalDatum from [swAutodimMark_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAutodimMark_e.html). Similarly a horizontal edge, horizontal sketch line, vertex, or sketch point should be selected and marked with swAutodimMark_e.swAutodimMarkVerticalDatum for defining the datum for the vertical dimensioning scheme. If only one of these datums is supplied, only the appropriate dimensions are created for that datum.

  Instead of selecting the horizontal and vertical datum separately, you can select a vertex or sketch point to use to define both datums. Mark the selected vertex or sketch point selection with swAutodimMark_e.swAutodimMarkOriginDatum. If no datums are selected, then this method automatically uses the left- and bottom-most entities in the view to determine default datums, which is consistent with how the SOLIDWORKS Design user interface works.
- entities to autodimension. This information is supplied by the entitiesToDimension argument and the selected entities marked with swAutodimMark_e.swAutodimMarkEntities. The entitiesToDimension argument takes a value from the swAutodimEntities_e enumeration:

  - swAutodimEntitiesSelected indicates that only selected entities marked with a value of swAutodimMarkEntities are considered for autodimensioning.
  - swAutodimEntitiesAll indicates that all entities in the drawing view are autodimensioned.
  - swAutodimEntitiesBasedOnPreselect indicates that SOLIDWORKS figures out what to do based on the selected entities marked with swAutodimMarkEntities. If any exist, then autodimension them, just like swAutodimEntitiesSelected. If none exist, then autodimension all entities, just like swAutodimEntitiesAll.

    Supported entities for dimensioning are lines, points, vertices, faces, and sketch entities.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc:AddChamferDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddChamferDim.html)
[IDrawingDoc:CreateAngDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAngDim4.html)
[IDrawingDoc:CreateDiamDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDiamDim4.html)
[IDrawingDoc:CreateLinearDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateLinearDim4.html)
[IDrawingDoc:CreateOrdinateDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateOrdinateDim4.html)
[IDrawingDoc:Dimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Dimensions.html)
[IDrawingDoc:DragModelDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DragModelDimension.html)
[IDrawingDoc:HideShowDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~HideShowDimensions.html)
[IDrawingDoc:IAddChamferDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IAddChamferDim.html)
[IDrawingDoc:ICreateAngDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAngDim4.html)
[IDrawingDoc:ICreateDiamDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDiamDim4.html)
[IDrawingDoc:ICreateLinearDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateLinearDim4.html)
[IDrawingDoc:ICreateOrdinateDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateOrdinateDim4.html)
[IDrawingDoc:InsertBaseDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertBaseDim.html)
[IDrawingDoc:InsertHorizontalOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertHorizontalOrdinate.html)
[IDrawingDoc:InsertModelAnnotations3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelAnnotations3.html)
[IDrawingDoc:InsertModelDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelDimensions.html)
[IDrawingDoc:InsertOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertOrdinate.html)
[IDrawingDoc:InsertRefDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertRefDim.html)
[IDrawingDoc:InsertVerticalOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertVerticalOrdinate.html)
[IDrawingDoc::SketchDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SketchDim.html)
[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
