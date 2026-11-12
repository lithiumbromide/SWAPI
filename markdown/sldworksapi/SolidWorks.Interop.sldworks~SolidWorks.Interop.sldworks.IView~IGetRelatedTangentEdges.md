---
title: "IGetRelatedTangentEdges Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetRelatedTangentEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetRelatedTangentEdges.html"
---

# IGetRelatedTangentEdges Method (IView)

Gets the visible tangent edges for the specified bendline in a [flat-pattern drawing view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IsFlatPatternView.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetRelatedTangentEdges( _
   ByVal BendLine As SketchSegment, _
   ByVal NumOfTangentEdges As System.Integer _
) As Edge
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim BendLine As SketchSegment
Dim NumOfTangentEdges As System.Integer
Dim value As Edge

value = instance.IGetRelatedTangentEdges(BendLine, NumOfTangentEdges)
```

### C#

```csharp
Edge IGetRelatedTangentEdges(
   SketchSegment BendLine,
   System.int NumOfTangentEdges
)
```

### C++/CLI

```cpp
Edge^ IGetRelatedTangentEdges(
   SketchSegment^ BendLine,
   System.int NumOfTangentEdges
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BendLine`: Bendline whose visible tangent edges you want (see **Remarks**)
- `NumOfTangentEdges`: Number of visible tangent edges for the specified bendline

### Return Value

- in-process, unmanaged C++: Pointer to an array of visible tangent [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) for the specified bendline
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IView::GetRelatedTangentEdgeCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetRelatedTangentEdgeCount.html) to get NumOfTangentEdges.

Hidden tangent edges are not returned by this method. Call [IDrawingDoc::ViewTangentEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~ViewTangentEdges.html) to change the visibility of tangent edges in a drawing.

Call [IView::GetBendLineCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetBendLineCount.html) to get the number of bendlines in a flat-pattern drawing view. Call [IView::GetBendLines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetBendLines.html) or [IView::IGetBendLines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetBendLines.html) to get an array of bendlines for a flat-pattern drawing view. Use the value returned by IView::GetBendLineCount to determine the index of the bendline in the array of bendlines you want.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetRelatedTangentEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRelatedTangentEdges.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
