---
title: "SplitClosedSegment Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "SplitClosedSegment"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SplitClosedSegment.html"
---

# SplitClosedSegment Method (ISketchManager)

Splits the selected closed sketch segment into two sketch segments.

## Syntax

### Visual Basic (Declaration)

```vb
Function SplitClosedSegment( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Z1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim Z2 As System.Double
Dim value As System.Object

value = instance.SplitClosedSegment(X1, Y1, Z1, X2, Y2, Z2)
```

### C#

```csharp
System.object SplitClosedSegment(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

### C++/CLI

```cpp
System.Object^ SplitClosedSegment(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X1`: X coordinate of first point
- `Y1`: Y coordinate of first point
- `Z1`: Z coordinate of first point
- `X2`: X coordinate of second point
- `Y2`: Y coordinate of second point
- `Z2`: Z coordinate of second point

### Return Value

Array of [sketch segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) of the now split formerly closed sketch skegment

## VBA Syntax

See [SketchManager::SplitClosedSegment](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~SplitClosedSegment.html).

## Examples

[Split Closed Sketch Segment (VBA)](Split_Closed_Sketch_Segment_Example_VB.htm)
[Split Closed Sketch Segment (VB.NET)](Split_Closed_Sketch_Segment_Example_VBNET.htm)
[Split Closed Sketch Segment (C#)](Split_Closed_Sketch_Segment_Example_CSharp.htm)

## Remarks

Before calling this method, be sure to disable snapping by either:

- De-selecting **System Options > Sketch > Relations/Snaps > Enable snapping**

- or -

- Calling [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html)([swUserPreferenceToggle_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.html).swSketchInference, false).

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::SplitOpenSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SplitOpenSegment.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
