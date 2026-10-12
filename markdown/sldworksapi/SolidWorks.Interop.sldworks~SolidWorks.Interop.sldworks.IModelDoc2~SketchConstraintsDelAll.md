---
title: "SketchConstraintsDelAll Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SketchConstraintsDelAll"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstraintsDelAll.html"
---

# SketchConstraintsDelAll Method (IModelDoc2)

Deletes all of the constraints on the currently selected sketch segment.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SketchConstraintsDelAll()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.SketchConstraintsDelAll()
```

### C#

```csharp
void SketchConstraintsDelAll()
```

### C++/CLI

```cpp
void SketchConstraintsDelAll();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::SketchConstraintsDelAll](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SketchConstraintsDelAll.html).

## Examples

[Delete All Constraints in Selected Sketch (VBA)](Delete_All_Constraints_in_Selected_Sketch_Example_VB.htm)

## Remarks

Only the constraints on the currently selected sketch segment are deleted. If two or more sketch segments are selected, this method has no effect.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SketchAddConstraints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchAddConstraints.html)
[IModelDoc2::SketchConstrainCoincident Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainCoincident.html)
[IModelDoc2::SketchConstrainConcentric Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainConcentric.html)
[IModelDoc2::SketchConstrainParallel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainParallel.html)
[IModelDoc2::SketchConstrainPerp Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainPerp.html)
[IModelDoc2::SketchConstraintsDel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstraintsDel.html)
[IModelDoc2::SketchConstrainTangent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainTangent.html)
[IModelDoc2::SkToolsAutoConstr Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SkToolsAutoConstr.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
