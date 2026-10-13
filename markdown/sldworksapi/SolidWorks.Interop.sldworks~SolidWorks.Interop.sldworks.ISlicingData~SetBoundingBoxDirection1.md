---
title: "SetBoundingBoxDirection1 Method (ISlicingData)"
project: "SOLIDWORKS API Help"
interface: "ISlicingData"
member: "SetBoundingBoxDirection1"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~SetBoundingBoxDirection1.html"
---

# SetBoundingBoxDirection1 Method (ISlicingData)

Sets bounding box direction 1 (top manipulator for both linear and radial slicing).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetBoundingBoxDirection1( _
   ByVal Direction As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISlicingData
Dim Direction As System.Double
Dim value As System.Boolean

value = instance.SetBoundingBoxDirection1(Direction)
```

### C#

```csharp
System.bool SetBoundingBoxDirection1(
   System.double Direction
)
```

### C++/CLI

```cpp
System.bool SetBoundingBoxDirection1(
   System.double Direction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Direction`: 0.0 < top manipulator < 500.0 (see **Remarks**)

### Return Value

True if direction 1 of bounding box successfully set, false if not

## VBA Syntax

See [SlicingData::SetBoundingBoxDirection1](ms-its:sldworksapivb6.chm::/sldworks~SlicingData~SetBoundingBoxDirection1.html).

## Examples

See the [ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html) example.

## Remarks

Use these methods to adjust the slicing volume to include or exclude geometry for slicing:

- ISlicingData::SetBoundingBoxDirection1
- [ISlicingData::SetBoundingBoxDirection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~SetBoundingBoxDirection2.html)
- [ISlicingData::SetBoundingBoxDirection3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~SetBoundingBoxDirection3.html)
- [ISlicingData::SetBoundingBoxDirection4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~SetBoundingBoxDirection4.html)

This method fails when:

- Direction exceeds the specified limits.
- The bounding box cannot be created because [ISlicingData::PlaneReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~PlaneReferences.html) has not been set.

## See Also

[ISlicingData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html)
[ISlicingData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData_members.html)
[ISlicingData::GetBoundingBoxDirection1 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection1.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
