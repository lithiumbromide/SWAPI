---
title: "GetBoundingBoxDirection2 Method (ISlicingData)"
project: "SOLIDWORKS API Help"
interface: "ISlicingData"
member: "GetBoundingBoxDirection2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection2.html"
---

# GetBoundingBoxDirection2 Method (ISlicingData)

Gets bounding box direction 2 (right manipulator for linear slicing, bottom manipulator for radial slicing).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBoundingBoxDirection2() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISlicingData
Dim value As System.Double

value = instance.GetBoundingBoxDirection2()
```

### C#

```csharp
System.double GetBoundingBoxDirection2()
```

### C++/CLI

```cpp
System.double GetBoundingBoxDirection2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

For linear slicing:

0.0 < right manipulator < 500.0

For radial slicing:

-500.0 < bottom manipulator < 0.0

## VBA Syntax

See [SlicingData::GetBoundingBoxDirection2](ms-its:sldworksapivb6.chm::/sldworks~SlicingData~GetBoundingBoxDirection2.html).

## Examples

See the [ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html) example.

## Remarks

This method is only valid after you have pre-selected the first slicing plane.

Use these methods to get the slicing volume for including or excluding geometry for slicing:

- [ISlicingData::GetBoundingBoxDirection1](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection1.html)
- ISlicingData::GetBoundingBoxDirection2
- [ISlicingData::GetBoundingBoxDirection3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection3.html)
- [ISlicingData::GetBoundingBoxDirection4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection4.html)

## See Also

[ISlicingData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html)
[ISlicingData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData_members.html)
[ISlicingData::SetBoundingBoxDirection2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~SetBoundingBoxDirection2.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
