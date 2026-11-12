---
title: "EditSketchOrSingleSketchFeature Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "EditSketchOrSingleSketchFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditSketchOrSingleSketchFeature.html"
---

# EditSketchOrSingleSketchFeature Method (IModelDoc2)

Edits a selected sketch or feature sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Sub EditSketchOrSingleSketchFeature()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.EditSketchOrSingleSketchFeature()
```

### C#

```csharp
void EditSketchOrSingleSketchFeature()
```

### C++/CLI

```cpp
void EditSketchOrSingleSketchFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::EditSketchOrSingleSketchFeature](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~EditSketchOrSingleSketchFeature.html).

## Remarks

This method is valid when one of the following is pre-selected:

- Sketch
- Body feature that is created from one sketch
- Surface feature that is created from one sketch
- Sketch picture
- Pen sketch
- Any item that supports **Context menu RMB > Edit Sketch**

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::EditSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditSketch.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
