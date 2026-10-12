---
title: "Get Wires, Sketch Segments, and Sketches Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Get_Wires_Sketch_Segments_and_Sketches_Example_VB.htm"
---

# Get Wires, Sketch Segments, and Sketches Example (VBA)

This example shows how to get the wires, route sketch segment IDs, sketch segments, and sketches.

```vb
...
vWires = rtElectricalRoute.GetWires
...
Set rtWire = vWire
...
For Each vWire In vWires
        Set rtWire = vWire
            vRouteSegmentIDs = rtWire.GetRouteSegmentIDs
            If Not IsEmpty(vRouteSegmentIDs) Then
               For lIdx = LBound(vRouteSegmentIDs) To UBound(vRouteSegmentIDs)
                    lSegmentId = vRouteSegmentIDs(lIdx)
                    Debug.Print "Segment ID = " & lSegmentId
                    vSketchSegments = rtElectricalRoute.GetSketchSegments(lSegmentId)
                    If Not IsEmpty(vSketchSegments) Then
                        For Each vSketchSegment In vSketchSegments
                            Set swSketchSegment = vSketchSegment
                            Debug.Assert (Not swSketchSegment Is Nothing)
                            bRetVal = swSketchSegment.Select4(True, Nothing)
                            Debug.Assert (bRetVal)
                            Set swSketch = swSketchSegment.GetSketch
...
```
