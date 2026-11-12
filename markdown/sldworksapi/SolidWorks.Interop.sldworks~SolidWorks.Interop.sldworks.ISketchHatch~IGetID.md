---
title: "IGetID Method (ISketchHatch)"
project: "SOLIDWORKS API Help"
interface: "ISketchHatch"
member: "IGetID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~IGetID.html"
---

# IGetID Method (ISketchHatch)

Gets the ID for this sketch hatch.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetID() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchHatch
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

Array with two longs or integers (see [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm)) identifying this sketch hatch ID (see **Remarks**)

## VBA Syntax

See [SketchHatch::IGetID](ms-its:sldworksapivb6.chm::/sldworks~SketchHatch~IGetID.html).

## Remarks

The ID of the sketch hatch:

- is an ordered pair (i1, i2). The combination of these two numbers is always unique within a specific sketch.
- cannot be assigned by applications or users.
- is not the same as a [persistent reference ID](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm).

Each entity within a specific sketch has a unique ID. However, a sketch line can have the same ID values as a sketch arc within the same sketch. Likewise, in a second sketch, you may find a different sketch element with the same ID. Therefore, your application must keep track of:

- sketch element type (that is, point, line, arc, spline, and so on)
- owning sketch name
- sketch element ID to uniquely identify a sketched item

You can determine the sketch element type by using [ISketchSegment::GetType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~GetType.html).

## See Also

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html)
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.html)
[ISketchHatch::GetID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~GetID.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
