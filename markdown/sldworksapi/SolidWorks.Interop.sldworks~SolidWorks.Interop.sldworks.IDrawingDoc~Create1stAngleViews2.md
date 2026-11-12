---
title: "Create1stAngleViews2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "Create1stAngleViews2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create1stAngleViews2.html"
---

# Create1stAngleViews2 Method (IDrawingDoc)

Creates standard three orthographic views (first angle projection) for the specified model.

## Syntax

### Visual Basic (Declaration)

```vb
Function Create1stAngleViews2( _
   ByVal ModelName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim ModelName As System.String
Dim value As System.Boolean

value = instance.Create1stAngleViews2(ModelName)
```

### C#

```csharp
System.bool Create1stAngleViews2(
   System.string ModelName
)
```

### C++/CLI

```cpp
System.bool Create1stAngleViews2(
   System.String^ ModelName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModelName`: Name of the document from which to create views

### Return Value

True if successful, false if not

## VBA Syntax

See [DrawingDoc::Create1stAngleViews2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~Create1stAngleViews2.html).

## Remarks

The views honor the automatic scaling behavior as specified in the document setting.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::Create3rdAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create3rdAngleViews2.html)
[IDrawingDoc::CreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAuxiliaryViewAt2.html)
[IDrawingDoc::CreateDetailViewAt4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDetailViewAt4.html)
[IDrawingDoc::CreateDrawViewFromModelView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView2.html)
[IDrawingDoc::CreateSectionView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionView.html)
[IDrawingDoc::CreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt4.html)
[IDrawingDoc::CreateViewport3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport3.html)
[IDrawingDoc::ICreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAuxiliaryViewAt2.html)
[IDrawingDoc::ICreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateSectionViewAt4.html)

## Availability

SOLIDWORKS 99 SP01, datecode 1999229
