---
title: "Position Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "Position"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Position.html"
---

# Position Property (IView)

Gets or sets the X and Y location of the model view's geometric center, relative to the drawing sheet origin.

## Syntax

### Visual Basic (Declaration)

```vb
Property Position As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

instance.Position = value

value = instance.Position
```

### C#

```csharp
System.object Position {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Position {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of 2 doubles (see **Remarks**)

## VBA Syntax

See [View::Position](ms-its:sldworksapivb6.chm::/sldworks~View~Position.html).

## Examples

[Insert and Position DXF File in Drawing (VBA)](Insert_and_Position_DXF_File_in_Drawing_Example_VB.htm)
[Reposition Drawing Views to Avoid Overlap (VBA)](Reposition_Drawing_Views_to_Avoid_Overlap_Example_VB.htm)
[Get View Bounding Box and Position (C#)](Get_View_Bounding_Box_and_Position_Example_CSharp.htm)
[Get View Bounding Box and Position (VB.NET)](Get_View_Bounding_Box_and_Position_Example_VBNET.htm)
[Get View Bounding Box and Position (VBA)](Get_View_Bounding_Box_and_Position_Example_VB.htm)

## Remarks

Any view alignments that might affect this view are handled the same way as if you were using the SOLIDWORKS Design user interface to draw the view to move it. If it is aligned with another view, it will only be allowed to move along the alignment vector. If it has child views that are aligned with it, those views will also be moved along with this view.

Changing this property can cause changes to the graphics of the drawing. After making all the view-related changes, call [IModelDoc2::EditRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRebuild3.html) to regenerate the drawing to see these changes.

To move a drawing view independently of its child views, use [IView::SetViewPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetViewPosition.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IPosition.html)
[IView::ModelToViewTransform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ModelToViewTransform.html)
[IView::SetXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetXform.html)
[IView::ISetXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ISetXform.html)
[IView::IGetXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetXform.html)
[IView::IGetViewXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetViewXform.html)
[IView::GetXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetXform.html)
[IView::GetViewXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetViewXform.html)
[IView::PositionLocked Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~PositionLocked.html)
