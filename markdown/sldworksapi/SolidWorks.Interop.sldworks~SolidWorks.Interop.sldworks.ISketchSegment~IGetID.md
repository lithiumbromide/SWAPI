---
title: "IGetID Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "IGetID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetID.html"
---

# IGetID Method (ISketchSegment)

Gets the ID for this sketch segment.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetID() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
Dim value As System.Integer

value = instance.IGetID()
```

### C#

```csharp
System.int IGetID()
```

### C++/CLI

```cpp
System.int IGetID();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array with two longs or integers (see [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm)) identifying this sketch segment ID

## VBA Syntax

See [SketchSegment::IGetID](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~IGetID.html).

## Remarks

The ID of the sketch segment:

- is an ordered pair (i1, i2). For the specific sketch segment type, for example, line, arc, spline, and so on), the combination of these two numbers is always unique within a specific sketch.
- cannot be assigned by applications or users.
- is not the same as a [persistent reference ID](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm).

Each entity within a specific sketch has a unique ID. However, a sketch line may have the same ID values as a sketch arc within the same sketch. Likewise, in a second sketch, you may find a different sketch element with the same ID Therefore, your application must keep track of:

- sketch element type (that is, point, line, arc, spline, and so on)
- owning sketch name
- sketch element id to uniquely identify a sketched item

You can determine the sketch element type by using [ISketchSegment::GetType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~GetType.html).

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)
[ISketchSegment::GetID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetID.html)

## Availability

SOLIDWORKS 99, datecode 1999207
