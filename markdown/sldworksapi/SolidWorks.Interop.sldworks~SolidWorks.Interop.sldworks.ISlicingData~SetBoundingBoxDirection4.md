---
title: "SetBoundingBoxDirection4 Method (ISlicingData)"
project: "SOLIDWORKS API Help"
interface: "ISlicingData"
member: "SetBoundingBoxDirection4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~SetBoundingBoxDirection4.html"
---

# SetBoundingBoxDirection4 Method (ISlicingData)

Sets bounding box direction 4 (bottom manipulator for linear slicing, outer radius for radial slicing).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetBoundingBoxDirection4( _
   ByVal Direction As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISlicingData
Dim Direction As System.Double
Dim value As System.Boolean

value = instance.SetBoundingBoxDirection4(Direction)
```

### C#

```csharp
System.bool SetBoundingBoxDirection4(
   System.double Direction
)
```

### C++/CLI

```cpp
System.bool SetBoundingBoxDirection4(
   System.double Direction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Direction`: For linear slicing:

  -500.0 < bottom manipulator < 0

  For radial slicing:

  Inner radius < outer radius < user-interface maximum for this case

  (see **Remarks**)

### Return Value

True if direction 4 of bounding box successfully set, false if not

## VBA Syntax

See [SlicingData::SetBoundingBoxDirection4](ms-its:sldworksapivb6.chm::/sldworks~SlicingData~SetBoundingBoxDirection4.html).

## Examples

See the [ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html) example.

## Remarks

Use these methods to adjust the slicing volume to include or exclude geometry for slicing:

- [ISlicingData::SetBoundingBoxDirection1](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~SetBoundingBoxDirection1.html)
- [ISlicingData::SetBoundingBoxDirection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~SetBoundingBoxDirection2.html)
- [ISlicingData::SetBoundingBoxDirection3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~SetBoundingBoxDirection3.html)
- ISlicingData::SetBoundingBoxDirection4

This method fails when:

- Direction exceeds the specified limits.
- The bounding box cannot be created because [ISlicingData::PlaneReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~PlaneReferences.html) has not been set.

## See Also

[ISlicingData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html)
[ISlicingData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData_members.html)
[ISlicingData::GetBoundingBoxDirection4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection4.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
