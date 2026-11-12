---
title: "Select All Sketch Segments Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_All_Sketch_Segments_Example_CPlusPlus_COM.htm"
---

# Select All Sketch Segments Example (C++ COM)

This example shows how to use the IEnumSketchSegments interface to select all sketch segments in the active sketch. Nearly identical code could be used to also select all the sketch points in the active sketch by replacing IEnumSketchSegments with IEnumSketchPoints.

```vb
 LPMODELDOC pModelDoc = NULL;
 hres = UserApp->getSWApp()->get_IActiveDoc(&pModelDoc);
 if (pModelDoc == NULL) return;

 LPSKETCH pSketch = NULL;
 hres = pModelDoc->IGetActiveSketch2(&pSketch);

 // No Active Sketch
 if (pSketch == NULL) return;

 LPENUMSKETCHSEGMENTS pSketchSegEnum = NULL;
 hres = pSketch->IEnumSketchSegments(&pSketchSegEnum);

 // No Sketch segments exist
 if (pSketchSegEnum == NULL) return;

 int segNum = 0;
 LPSKETCHSEGMENT pSketchSegment = NULL;
 long skReturned = -1
 hres = pSketchSegEnum->Next(1, &pSketchSegment, &skReturned);
 while (S_OK == hres)
 {
  VARIANT_BOOL ok = FALSE;

  // Select the SketchSegment object
  hres = pSketchSegment->Select(TRUE, &ok);

  if (!ok) AfxMessageBox (_T("Error Selecting Sketch Segment! Continuing..."));

  pSketchSegment->Release();
  pSketchSegment = NULL;
  hres = pSketchSegEnum->Next(1, &pSketchSegment, &skReturned);
 }

 if (pSketchSegEnum != NULL) pSketchSegEnum->Release();
```
