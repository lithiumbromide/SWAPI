---
title: "SetDynamicMirror Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "SetDynamicMirror"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SetDynamicMirror.html"
---

# SetDynamicMirror Method (ISketchManager)

Enables or disables dynamic sketch mirroring, which is the automatic mirroring of newly created sketch entities about a selected centerline.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDynamicMirror( _
   ByVal DynamicMirror As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim DynamicMirror As System.Boolean
Dim value As System.Boolean

value = instance.SetDynamicMirror(DynamicMirror)
```

### C#

```csharp
System.bool SetDynamicMirror(
   System.bool DynamicMirror
)
```

### C++/CLI

```cpp
System.bool SetDynamicMirror(
   System.bool DynamicMirror
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DynamicMirror`: True to enable dynamic sketch mirroring, false to disable it

### Return Value

True if setting this option to succeeds, false if fails

## VBA Syntax

See [SketchManager::SetDynamicMirror](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~SetDynamicMirror.html).

## Examples

[Dynamically Mirror Sketch Entities (VBA)](Dynamically_Mirror_Sketch_Entities_Example_VB.htm)

## Remarks

If enabling dynamic sketch mirroring, then:

- a sketch must be in edit mode.
- a line segment or linear edge of a model must be selected before calling this method.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::GetDynamicMirror Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~GetDynamicMirror.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
