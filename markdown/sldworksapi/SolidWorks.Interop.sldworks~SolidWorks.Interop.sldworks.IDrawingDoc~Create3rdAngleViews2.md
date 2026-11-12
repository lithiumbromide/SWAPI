---
title: "Create3rdAngleViews2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "Create3rdAngleViews2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create3rdAngleViews2.html"
---

# Create3rdAngleViews2 Method (IDrawingDoc)

Creates standard three orthographic views (third angle projection) for the specified model.

## Syntax

### Visual Basic (Declaration)

```vb
Function Create3rdAngleViews2( _
   ByVal ModelName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim ModelName As System.String
Dim value As System.Boolean

value = instance.Create3rdAngleViews2(ModelName)
```

### C#

```csharp
System.bool Create3rdAngleViews2(
   System.string ModelName
)
```

### C++/CLI

```cpp
System.bool Create3rdAngleViews2(
   System.String^ ModelName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModelName`: Name of the document from which to create views

### Return Value

True if successful, false if not

## VBA Syntax

See [DrawingDoc::Create3rdAngleViews2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~Create3rdAngleViews2.html).

## Examples

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)
[Dimension Edge in Drawing (VBA)](Dimension_Edge_in_Drawing_Example_VB.htm)
[Select Entity in Drawing View (VBA)](Select_Entity_in_Drawing_View_Example_VB.htm)
[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)
[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)

## Remarks

The views honor the automatic scaling behavior as specified in the document setting.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::CreateDrawViewFromModelView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView2.html)
[IDrawingDoc::CreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt4.html)
[IDrawingDoc::CreateViewport3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport3.html)
[IDrawingDoc::ICreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAuxiliaryViewAt2.html)
[IDrawingDoc::ICreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDetailViewAt3.html)
[IDrawingDoc::ICreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateSectionViewAt4.html)
[IDrawingDoc::Create1stAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create1stAngleViews2.html)
[IDrawingDoc::Create3rdAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create3rdAngleViews2.html)
[IDrawingDoc::CreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDetailViewAt3.html)
[IDrawingDoc::CreateDrawViewFromModelView3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView3.html)
[IDrawingDoc::CreateFlatPatternViewFromModelView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateFlatPatternViewFromModelView2.html)
[IDrawingDoc::CreateSectionView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionView.html)
[IDrawingDoc::CreateRelativeView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateRelativeView.html)
[IDrawingDoc::CreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt4.html)
[IDrawingDoc::CreateUnfoldedViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateUnfoldedViewAt3.html)
[IDrawingDoc::CreateViewport3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport3.html)
[IDrawingDoc::ICreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDetailViewAt3.html)
[IDrawingDoc::ICreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateSectionViewAt4.html)
[IDrawingDoc::CreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAuxiliaryViewAt2.html)

## Availability

SOLIDWORKS 99 SP01, datecode 1999229
