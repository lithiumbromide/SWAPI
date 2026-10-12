---
title: "DeSelect Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "DeSelect"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~DeSelect.html"
---

# DeSelect Method (ISketchSegment)

Deselects the sketch segment.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeSelect() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
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

True if the sketch segment is deselected successfully, false if not

## VBA Syntax

See [SketchSegment::DeSelect](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~DeSelect.html).

## Remarks

This method does not work well when a PropertyManager page is open or a command is running. Use [IModelDoc2::DeSelectByID](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~DeSelectByID.html) instead of using this method. IModelDoc2::DeSelectByID handles selection correctly whether or not a command is running.

To select or deselect a sketch segment, the owning document of that ISketchSegment object needs to be open and visible.

ISketchSegment selections are accessible through the [ISelectionMgr](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr.html) of the owning document of the sketch segment object, even if the owning document is not active.

Selection or deselection does not work for a sketch segment in a document within a drawing. Selection or deselection of sketch segments owned by the drawing does work, but only if the drawing document is active.

If the owning sketch of a sketch segment was active, or inactive, when the sketch segment was obtained, then it must be active, or inactive, to deselect it. For example, if the owning sketch of a sketch segment was active when the sketch segment was obtained, then the owning sketch must be active to select or deselect the sketch segment. Likewise, if the owning sketch of a sketch segment was inactive when the sketch segment was obtained, then the owning sketch must be inactive to select or deselect the sketch segment.

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)
[ISketchSegment::Select4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Select4.html)

## Availability

SOLIDWORKS 99, datecode 1999207
