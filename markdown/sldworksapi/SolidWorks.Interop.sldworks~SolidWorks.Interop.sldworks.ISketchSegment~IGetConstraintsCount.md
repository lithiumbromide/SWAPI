---
title: "IGetConstraintsCount Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "IGetConstraintsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetConstraintsCount.html"
---

# IGetConstraintsCount Method (ISketchSegment)

Gets the number of constraints on the sketch segment.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetConstraintsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
Dim value As System.Integer

value = instance.IGetConstraintsCount()
```

### C#

```csharp
System.int IGetConstraintsCount()
```

### C++/CLI

```cpp
System.int IGetConstraintsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of constraints on this sketch segment

## VBA Syntax

See [SketchSegment::IGetConstraintsCount](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~IGetConstraintsCount.html).

## Examples

[Get Sketch Segment Constraints (C++)](Get_Sketch_Segment_Constraints_Example_CPlusPlus_COM.htm)

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)
[IModelDoc2::SketchConstraintsDelAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstraintsDelAll.html)
[ISketdhSegment::GetConstraints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetConstraints.html)
[ISketdhSegment::IGetConstraints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetConstraints.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
