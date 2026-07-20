---
title: "InsertAnnotationView Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "InsertAnnotationView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertAnnotationView.html"
---

# InsertAnnotationView Method (IModelDocExtension)

Inserts an annotation view in this part or assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertAnnotationView( _
   ByVal AnnotationViewingDirection As System.Integer, _
   ByVal DirectionReference As System.Object, _
   ByVal FlipDirection As System.Boolean, _
   ByVal HorizontalDirectionReference As System.Object, _
   ByVal AngleMadeWithHorizontal As System.Integer _
) As AnnotationView
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim AnnotationViewingDirection As System.Integer
Dim DirectionReference As System.Object
Dim FlipDirection As System.Boolean
Dim HorizontalDirectionReference As System.Object
Dim AngleMadeWithHorizontal As System.Integer
Dim value As AnnotationView

value = instance.InsertAnnotationView(AnnotationViewingDirection, DirectionReference, FlipDirection, HorizontalDirectionReference, AngleMadeWithHorizontal)
```

### C#

```csharp
AnnotationView InsertAnnotationView(
   System.int AnnotationViewingDirection,
   System.object DirectionReference,
   System.bool FlipDirection,
   System.object HorizontalDirectionReference,
   System.int AngleMadeWithHorizontal
)
```

### C++/CLI

```cpp
AnnotationView^ InsertAnnotationView(
   System.int AnnotationViewingDirection,
   System.Object^ DirectionReference,
   System.bool FlipDirection,
   System.Object^ HorizontalDirectionReference,
   System.int AngleMadeWithHorizontal
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `AnnotationViewingDirection`: Defined by either any

[swStandardViews_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swStandardViews_e.html)

enumerator or 0 for selection
- `DirectionReference`: If 0 specified for AnnotationViewingDirection, then specifiy a

[face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

or

[plane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html)

to define the direction of the annotation view
- `FlipDirection`: True to flip the annotation view in the opposite direction, false to notParamDesc
- `HorizontalDirectionReference`: An

[edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

,

[sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html)

, or

[face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)
- `AngleMadeWithHorizontal`: Angle (in degrees) with the specified HorizontalDirectionReference

### Return Value

Newly inserted

[annotation view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotationView.html)

## VBA Syntax

See

[ModelDocExtension::InsertAnnotationView](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~InsertAnnotationView.html)

.

## Examples

'VBA

'----------------------------------------------------------------------------

' Preconditions:

' 1. Open a SOLIDWORKS model file.

' 2. Select a face to define the direction of the annotation view.

' 3. Select an edge as a horizontal direction reference.

'

' Postconditions:Observe that a new annotation view is inserted at a 45 degree angle in reference to the face and edge.

'----------------------------------------------------------------------------

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim swModExt As SldWorks.ModelDocExtension

Dim swSelMgr As SldWorks.SelectionMgr

Dim swFace As SldWorks.Face2

Dim swEdge As SldWorks.edge

Dim swAnnoView As SldWorks.AnnotationView

Dim i As Integer

Sub main()

Set swApp = Application.SldWorks

Set swModel = swApp.ActiveDoc

Set swModExt = swModel.Extension

Set swSelMgr = swModel.SelectionManager

For i = 0 To swSelMgr.GetSelectedObjectCount2(-1) - 1

If swSelMgr.GetSelectedObjectType3(i + 1, -1) = swSelFACES Then

Set swFace = swSelMgr.GetSelectedObject6(i + 1, -1)

End If

If swSelMgr.GetSelectedObjectType3(i + 1, -1) = swSelEDGES Then

Set swEdge = swSelMgr.GetSelectedObject6(i + 1, -1)

End If

Next i

Set annoView = swModExt. InsertAnnotationView (0, Nothing, False, swEdge, 45)

swModel.EditRebuild3

End Sub

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)

[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
