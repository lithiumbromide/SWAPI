---
title: "GetDetachSegmentOnDrag Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetDetachSegmentOnDrag"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetDetachSegmentOnDrag.html"
---

# GetDetachSegmentOnDrag Method (ISketch)

Gets the Detach Segment on Drag setting.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDetachSegmentOnDrag() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Boolean

value = instance.GetDetachSegmentOnDrag()
```

### C#

```csharp
System.bool GetDetachSegmentOnDrag()
```

### C++/CLI

```cpp
System.bool GetDetachSegmentOnDrag();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if Detach Segment on Drag is selected, false if not

## VBA Syntax

See [Sketch::GetDetachSegmentOnDrag](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetDetachSegmentOnDrag.html).

## Remarks

Although this setting can be returned or set at any time, SOLIDWORKS sets it to false upon exiting or entering a sketch. Thus, this method is only useful if called while a sketch is active.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::SetDetachSegmentOnDrag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~SetDetachSegmentOnDrag.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
