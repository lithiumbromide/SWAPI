---
title: "InsertModelAnnotations3 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertModelAnnotations3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelAnnotations3.html"
---

# InsertModelAnnotations3 Method (IDrawingDoc)

Inserts model annotations into this drawing document's currently selected drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertModelAnnotations3( _
   ByVal Option As System.Integer, _
   ByVal Types As System.Integer, _
   ByVal AllViews As System.Boolean, _
   ByVal DuplicateDims As System.Boolean, _
   ByVal HiddenFeatureDims As System.Boolean, _
   ByVal UsePlacementInSketch As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Option As System.Integer
Dim Types As System.Integer
Dim AllViews As System.Boolean
Dim DuplicateDims As System.Boolean
Dim HiddenFeatureDims As System.Boolean
Dim UsePlacementInSketch As System.Boolean
Dim value As System.Object

value = instance.InsertModelAnnotations3(Option, Types, AllViews, DuplicateDims, HiddenFeatureDims, UsePlacementInSketch)
```

### C#

```csharp
System.object InsertModelAnnotations3(
   System.int Option,
   System.int Types,
   System.bool AllViews,
   System.bool DuplicateDims,
   System.bool HiddenFeatureDims,
   System.bool UsePlacementInSketch
)
```

### C++/CLI

```cpp
System.Object^ InsertModelAnnotations3(
   System.int Option,
   System.int Types,
   System.bool AllViews,
   System.bool DuplicateDims,
   System.bool HiddenFeatureDims,
   System.bool UsePlacementInSketch
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Option`: Source of dimensions as defined by [swImportModelItemsSource_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swImportModelItemsSource_e.html) (see Remarks)
- `Types`: Bitwise OR of annotation types as defined in [swInsertAnnotation_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInsertAnnotation_e.html)
- `AllViews`: True to insert the annotations in all views in the drawing, false to insert annotations only in the selected view
- `DuplicateDims`: True to eliminate duplicate dimensions, false to allow duplicate dimensions
- `HiddenFeatureDims`: True to insert dimensions from features that are hidden, false to not insert dimensions from features that are hidden
- `UsePlacementInSketch`: True to insert dimensions as they were placed in sketch, false to not

### Return Value

Array of inserted [IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) objects

## VBA Syntax

See [DrawingDoc::InsertModelAnnotations3](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertModelAnnotations3.html).

## Remarks

The Option argument was incorrectly documented in versions of the SOLIDWORKS API Help published before SOLIDWORKS 2008 SP3.

| Incorrect | Correct |
| --- | --- |
| 0 - All dimensions in the view | swImportModelItemsFromEntireModel = 0 |
| 1 - All dimensions of the currently selected component (for assembly drawings) | swImportModelItemsFromSelectedFeature = 1 |
| 2 - All dimensions of the currently selected feature | swImportModelItemsFromSelectedComponent = 2 |
| All dimensions of the assembly | swImportModelItemsFromAssemblyOnly = 3 |

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::AddCenterMark Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddCenterMark.html)
[IDrawingDoc::AddChamferDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddChamferDim.html)
[IDrawingDoc::AddHoleCallout2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddHoleCallout2.html)
[IDrawingDoc::Dimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Dimensions.html)
[IDrawingDoc::INewGtol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~INewGtol.html)
[IDrawingDoc::InsertBaseDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertBaseDim.html)
[IDrawingDoc::ICreateText2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateText2.html)
[IDrawingDoc::CreateText2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateText2.html)
[IDrawingDoc::CreateCompoundNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateCompoundNote.html)
[IDrawingDoc::IAddHoleCallout2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IAddHoleCallout2.html)
[IDrawingDoc::ICreateCompoundNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateCompoundNote.html)
[IDrawingDoc::InsertDatumTag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertDatumTag.html)
[IDrawingDoc::InsertNewNote2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertNewNote2.html)
[IDrawingDoc::InsertRefDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertRefDim.html)
[IDrawingDoc::InsertRevisionSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertRevisionSymbol.html)
[IDrawingDoc::InsertSurfaceFinishSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertSurfaceFinishSymbol.html)
[IDrawingDoc::InsertThreadCallout Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertThreadCallout.html)
[IDrawingDoc::InsertWeldSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertWeldSymbol.html)
[IDrawingDoc::NewGtol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewGtol.html)
[IDrawingDoc::NewNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewNote.html)
[IDrawingDoc::AttachAnnotation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AttachAnnotation.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
