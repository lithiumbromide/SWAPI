---
title: "DeSelect Method (ISketchHatch)"
project: "SOLIDWORKS API Help"
interface: "ISketchHatch"
member: "DeSelect"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~DeSelect.html"
---

# DeSelect Method (ISketchHatch)

Deselects the sketch hatch.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeSelect() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchHatch
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

True if the sketch hatch is deselected, false if not

## VBA Syntax

See [SketchHatch::DeSelect](ms-its:sldworksapivb6.chm::/sldworks~SketchHatch~DeSelect.html).

## Remarks

This method does not work well when a PropertyManager page is open or a command is running. Use [IModelDoc2::DeSelectByID](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~DeSelectByID.html) instead of using this method. IModelDoc2::DeSelectByID handles selection correctly whether or not a command is running.

To select or deselect a sketch hatch, the owning document of the ISketchHatch object needs to be open and visible.

ISketchHatch selections are accessible through the [ISelectionMgr](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr.html) of the owning document of the [ISketchHatch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchHatch.html) object, even if the owning document is not active.

Selection or deselection does not work for a sketch hatch in a component within an assembly. Selection or deselection does not work for a sketch hatch in a document within a drawing. Selection or deselection of sketch hatches owned by the top-level assembly or drawing works, but only if the assembly document or the drawing document is active.

If the owning sketch of a sketch hatch is active (inactive) when the sketch hatch is obtained, then it must be active (inactive) to deselect it. For example, if the owning sketch of a sketch hatch was active when the sketch hatch was obtained, then the owning sketch must be active to select or deselect the sketch hatch. Likewise, if the owning sketch of a sketch hatch was inactive when the sketch hatch was obtained, then the owning sketch must be inactive to select or deselect the sketch hatch.

## See Also

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html)
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.html)
[ISketchHatch::Select4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~Select4.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
