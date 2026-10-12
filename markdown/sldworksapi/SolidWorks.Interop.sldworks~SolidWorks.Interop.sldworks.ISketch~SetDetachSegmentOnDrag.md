---
title: "SetDetachSegmentOnDrag Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "SetDetachSegmentOnDrag"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~SetDetachSegmentOnDrag.html"
---

# SetDetachSegmentOnDrag Method (ISketch)

Sets the Detach Segment on Drag setting.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDetachSegmentOnDrag( _
   ByVal Detach As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim Detach As System.Boolean
Dim value As System.Boolean

value = instance.SetDetachSegmentOnDrag(Detach)
```

### C#

```csharp
System.bool SetDetachSegmentOnDrag(
   System.bool Detach
)
```

### C++/CLI

```cpp
System.bool SetDetachSegmentOnDrag(
   System.bool Detach
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Detach`: True to select Detach Segment on Drag, false to not

### Return Value

True if Detach Segment on Drag is set, false if not

## VBA Syntax

See [Sketch::SetDetachSegmentOnDrag](ms-its:sldworksapivb6.chm::/sldworks~Sketch~SetDetachSegmentOnDrag.html).

## Remarks

Although this setting can be returned or set at any time, SOLIDWORKS sets it to false upon exiting or entering a sketch. Thus, this method is only useful if called while a sketch is active.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetDetachSegmentOnDrag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetDetachSegmentOnDrag.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
