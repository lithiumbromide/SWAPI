---
title: "SplitOpenSegment Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "SplitOpenSegment"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SplitOpenSegment.html"
---

# SplitOpenSegment Method (ISketchManager)

Splits the selected open sketch segment into two sketch segments.

## Syntax

### Visual Basic (Declaration)

```vb
Function SplitOpenSegment( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Object

value = instance.SplitOpenSegment(X, Y, Z)
```

### C#

```csharp
System.object SplitOpenSegment(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.Object^ SplitOpenSegment(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X coordinate of the point that splits the sketch segment in two
- `Y`: Y coordinate of the point that splits the sketch segment in two
- `Z`: Z coordinate of the point that splits the sketch segment in two

### Return Value

Array of [sketch segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) of the now split formerly open sketch skegment

## VBA Syntax

See [SketchManager::SplitOpenSegment](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~SplitOpenSegment.html).

## Examples

[Split Open Sketch Segment (VBA)](Split_Open_Sketch_Segment_Example_VB.htm)
[Split Open Sketch Segment (VB.NET)](Split_Open_Sketch_Segment_Example_VBNET.htm)
[Split Open Sketch Segment (C#)](Split_Open_Sketch_Segment_Example_CSharp.htm)

## Remarks

Before calling this method, be sure to disable snapping by either:

- De-selecting **System Options > Sketch > Relations/Snaps > Enable snapping**

- or -

- Calling [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html)([swUserPreferenceToggle_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.html).swSketchInference, false).

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::SplitClosedSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SplitClosedSegment.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
