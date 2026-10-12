---
title: "InsertModelAnnotations4 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertModelAnnotations4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelAnnotations4.html"
---

# InsertModelAnnotations4 Method (IDrawingDoc)

Inserts model annotations into this drawing document's currently selected drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertModelAnnotations4( _
   ByVal Option As System.Integer, _
   ByVal Types As System.Integer, _
   ByVal AllViews As System.Boolean, _
   ByVal DuplicateDims As System.Boolean, _
   ByVal HiddenFeatureDims As System.Boolean, _
   ByVal UsePlacementInSketch As System.Boolean, _
   ByVal InsertAllAnnotations As System.Boolean, _
   ByVal InsertAllReferenceGeometry As System.Boolean _
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
Dim InsertAllAnnotations As System.Boolean
Dim InsertAllReferenceGeometry As System.Boolean
Dim value As System.Object

value = instance.InsertModelAnnotations4(Option, Types, AllViews, DuplicateDims, HiddenFeatureDims, UsePlacementInSketch, InsertAllAnnotations, InsertAllReferenceGeometry)
```

### C#

```csharp
System.object InsertModelAnnotations4(
   System.int Option,
   System.int Types,
   System.bool AllViews,
   System.bool DuplicateDims,
   System.bool HiddenFeatureDims,
   System.bool UsePlacementInSketch,
   System.bool InsertAllAnnotations,
   System.bool InsertAllReferenceGeometry
)
```

### C++/CLI

```cpp
System.Object^ InsertModelAnnotations4(
   System.int Option,
   System.int Types,
   System.bool AllViews,
   System.bool DuplicateDims,
   System.bool HiddenFeatureDims,
   System.bool UsePlacementInSketch,
   System.bool InsertAllAnnotations,
   System.bool InsertAllReferenceGeometry
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Option`: Source of dimensions as defined by [swImportModelItemsSource_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swImportModelItemsSource_e.html)
- `Types`: Annotation types to insert as defined in [swInsertAnnotation_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInsertAnnotation_e.html); only valid if InsertAllAnnotations and InsertAllReferenceGeometry are False
- `AllViews`: True to insert the annotations in all views in the drawing, false to insert annotations only in the selected view
- `DuplicateDims`: True to eliminate duplicate dimensions, false to allow duplicate dimensions
- `HiddenFeatureDims`: True to insert dimensions from features that are hidden, false to not insert dimensions from features that are hidden
- `UsePlacementInSketch`: True to insert dimensions as they were placed in sketch, false to not
- `InsertAllAnnotations`: True to insert all annotations, false to insert only those specified in Types
- `InsertAllReferenceGeometry`: True to insert all reference geometry, false to insert only those specified in Types

### Return Value

Array of inserted [IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) objects

## VBA Syntax

See [DrawingDoc::InsertModelAnnotations4](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertModelAnnotations4.html).

## Examples

[Insert Model Annotations (VBA)](Insert_Model_Annotations_Example_VB.htm)
[Insert Model Annotations (VB.NET)](Insert_Model_Annotations_Example_VBNET.htm)
[Insert Model Annotations (C#)](Insert_Model_Annotations_Example_CSharp.htm)

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::InsertModelDimensions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelDimensions.html)
[IDrawingDoc::InsertModelInPredefinedView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelInPredefinedView.html)

## Availability

SOLIDWORKS 2024 FCS, Revision Number 32
