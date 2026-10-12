---
title: "DeSelect Method (ISketchPoint)"
project: "SOLIDWORKS API Help"
interface: "ISketchPoint"
member: "DeSelect"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~DeSelect.html"
---

# DeSelect Method (ISketchPoint)

Deselects the sketch point.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeSelect() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPoint
Dim value As System.Boolean

value = instance.DeSelect()
```

### C#

```csharp
System.bool DeSelect()
```

### C++/CLI

```cpp
System.bool DeSelect();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the sketch point is deselected, false if not

## VBA Syntax

See [SketchPoint::DeSelect](ms-its:sldworksapivb6.chm::/sldworks~SketchPoint~DeSelect.html).

## Remarks

This method does not work well when a PropertyManager page is open or a command is running. Use [IModelDoc2::DeSelectByID](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~DeSelectByID.html) instead of using this method. IModelDoc2::DeSelectByID handles selection correctly whether or not a command is running.

To select or deselect a sketch point, the owning document of that ISketchPoint object needs to be open and visible.

Sketch point selections are accessible through the [ISelectionMgr](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr.html) of the owning document of the SIketchPoint object, even if the owning document is not active.

Selection or deselection does not work for a sketch point in a document within a drawing. Selection or deselection of sketch points owned by the drawing does work, but only when the drawing document is active.

If the owning sketch of a sketch point was active, or inactive, when the sketch point was obtained, then it must be active, or inactive, to deselect it. For example, if the owning sketch of a sketch point was active when the sketch point was obtained, then the owning sketch must be active to select or deselect the sketch point. Likewise, if the owning sketch of a sketch point was inactive when the sketch point was obtained, then the owning sketch must be inactive to select or deselect the sketch point

## See Also

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.html)
[ISketchPoint::Select4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Select4.html)

## Availability

SOLIDWORKS 99, datecode 1999207
