---
title: "GetRelatedTangentEdges Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetRelatedTangentEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRelatedTangentEdges.html"
---

# GetRelatedTangentEdges Method (IView)

Gets the visible tangent edges for the specified bendline in a [flat-pattern drawing view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IsFlatPatternView.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRelatedTangentEdges( _
   ByVal BendLine As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim BendLine As System.Object
Dim value As System.Object

value = instance.GetRelatedTangentEdges(BendLine)
```

### C#

```csharp
System.object GetRelatedTangentEdges(
   System.object BendLine
)
```

### C++/CLI

```cpp
System.Object^ GetRelatedTangentEdges(
   System.Object^ BendLine
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BendLine`: Bendline whose visible tangent edges you want (see **Remarks**)

### Return Value

Array of visible tangent edges for the specified bendline

## VBA Syntax

See [View::GetRelatedTangentEdges](ms-its:sldworksapivb6.chm::/sldworks~View~GetRelatedTangentEdges.html).

## Examples

[Get Tangent Edges of Bendlines (VB.NET)](Get_Tangent_Edges_of_Bendlines_Example_VBNET.htm)
[Get Tangent Edges of Bendlines (VBA)](Get_Tangent_Edges_of_Bendlines_Example_VB.htm)
[Get Tangent Edges of Bendlines (C#)](Get_Tangent_Edges_of_Bendlines_Example_CSharp.htm)

## Remarks

Hidden tangent edges are not returned by this method. Use [IDrawingDoc::ViewTangentEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~ViewTangentEdges.html) to change the visibility of tangent edges in a drawing.

Call [IView::GetBendLineCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetBendLineCount.html) to get the number of bendlines in a flat-pattern drawing view. Call [IView::GetBendLines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetBendLines.html) or [IView::IGetBendLines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetBendLines.html) to get an array of bendlines for a flat-pattern drawing view. Use the value returned by IView::GetBendLineCount to determine the index of the bendline in the array of bendlines you want.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetRelatedTangentEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRelatedTangentEdgeCount.html)
[IView::IGetRelatedTangentEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetRelatedTangentEdges.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
