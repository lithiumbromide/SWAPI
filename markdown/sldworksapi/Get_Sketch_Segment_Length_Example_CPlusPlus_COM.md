---
title: "Get Sketch SegmentLength Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Segment_Length_Example_CPlusPlus_COM.htm"
---

# Get Sketch SegmentLength Example (C++ COM)

## Get Sketch Segment Length Example (C++ COM)

This example shows how to get the length of a sketch segment.

```vb
double GetLength(LPMODELDOC Part,LPSELECTIONMGR SelectionManager,LPTSTR objectName)
{
LPTSTR segType = _T("EXTSKETCHSEGMENT");
VARIANT_BOOL success;
double Length(-1.0);  // neg number == failure
Part->SelectByID(objectName, segType, 0.0, 0.0, 0,&success);
if(Part->SelectByID(objectName, segType, 0.0, 0.0, 0,&success) == S_OK && success)
{
LPSKETCHSEGMENT SketchSegment;
LPDISPATCH disp;
if(SelectionManager->GetSelectedObject2(1,&disp) == S_OK &&
disp != NULL &&
disp->QueryInterface(IID_ISketchSegment,(void **)&SketchSegment) == S_OK &&
SketchSegment != NULL)
SketchSegment->GetLength(&Length);
}
return Length;
}
```
