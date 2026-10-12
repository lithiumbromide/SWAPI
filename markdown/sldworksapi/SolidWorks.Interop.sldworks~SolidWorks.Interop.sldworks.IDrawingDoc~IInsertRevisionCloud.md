---
title: "IInsertRevisionCloud Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "IInsertRevisionCloud"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IInsertRevisionCloud.html"
---

# IInsertRevisionCloud Method (IDrawingDoc)

Inserts a revision cloud annotation with the specified shape into a view or sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function IInsertRevisionCloud( _
   ByVal CloudShape As System.Integer _
) As RevisionCloud
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim CloudShape As System.Integer
Dim value As RevisionCloud

value = instance.IInsertRevisionCloud(CloudShape)
```

### C#

```csharp
RevisionCloud IInsertRevisionCloud(
   System.int CloudShape
)
```

### C++/CLI

```cpp
RevisionCloud^ IInsertRevisionCloud(
   System.int CloudShape
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CloudShape`: Revision cloud annotation shape as defined in [swRevisionCloudShape_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRevisionCloudShape_e.html)

### Return Value

- in-process, unmanaged C++: Pointer to an [IRevisionCloud](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionCloud.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

After calling this method:

1. Call [IRevisionCloud::IGetAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionCloud~IGetAnnotation.html) to get the annotation object for the revision cloud.
2. Call [IAnnotation::SetPosition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~SetPosition.html) to set the revision cloud position point on the drawing. If you eliminate this step, the revision cloud is rendered starting at the drawing origin of x=0, y=0, z=0. Set the revision cloud position point as follows:

  | For revision cloud shape... | Set the revision cloud position point to... |
  | --- | --- |
  | Ellipse | The center of the revision cloud. |
  | Rectangle | A corner of the revision cloud. |
  | Polygon | One of the points on the revision cloud. |
  | Freehand | One of the points on the revision cloud. |
3. Call [IRevisionCloud::ArcRadius](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionCloud~ArcRadius.html) to set the arc radius of the revision cloud.
4. Call [IRevisionCloud::SetPathPointAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionCloud~SetPathPointAtIndex.html) with Index = -1 to create points on the revision cloud as follows:

  | For revision cloud shape... | Call IRevisionCloud::SetPathPointAtIndex... |
  | --- | --- |
  | Ellipse | Once, specifying the coordinates of a corner of the ellipse-inscribed rectangle. |
  | Rectangle | Once, specifying the coordinates of a corner opposite the revision cloud position point. |
  | Polygon | (Number of polygon sides + 1) times, such that the first and last points coincide with the revision cloud position point. |
  | Freehand | Indefinite number of times, such that the first and last points coincide with the revision cloud position point. |
5. Call [IRevisionCloud::Finalize](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionCloud~Finalize.html) to close the revision cloud path. Once the revision cloud path is closed, you can no longer add points to it.
6. Call IRevisionCloud::SetPathPointAtIndex to modify the position of an existing point on the revision cloud.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IView::InsertRevisionCloud Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertRevisionCloud.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
