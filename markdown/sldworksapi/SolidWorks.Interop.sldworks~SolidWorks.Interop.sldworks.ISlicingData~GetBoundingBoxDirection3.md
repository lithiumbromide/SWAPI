---
title: "GetBoundingBoxDirection3 Method (ISlicingData)"
project: "SOLIDWORKS API Help"
interface: "ISlicingData"
member: "GetBoundingBoxDirection3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection3.html"
---

# GetBoundingBoxDirection3 Method (ISlicingData)

Gets bounding box direction 3 (left manipulator for linear slicing, inner radius for radial slicing).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBoundingBoxDirection3() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISlicingData
Dim value As System.Double

value = instance.GetBoundingBoxDirection3()
```

### C#

```csharp
System.double GetBoundingBoxDirection3()
```

### C++/CLI

```cpp
System.double GetBoundingBoxDirection3();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

For linear slicing:

-500.0 < left manipulator < 0.0

For angular slicing:

0.0 < inner radius < outer radius

## VBA Syntax

See [SlicingData::GetBoundingBoxDirection3](ms-its:sldworksapivb6.chm::/sldworks~SlicingData~GetBoundingBoxDirection3.html).

## Examples

See the [ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html) example.

## Remarks

This method is only valid after you have pre-selected the first slicing plane.

Use these methods to get the slicing volume for including or excluding geometry for slicing:

- [ISlicingData::GetBoundingBoxDirection1](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection1.html)
- [ISlicingData::GetBoundingBoxDirection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection2.html)
- ISlicingData::GetBoundingBoxDirection3
- [ISlicingData::GetBoundingBoxDirection4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection4.html)

## See Also

[ISlicingData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html)
[ISlicingData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData_members.html)
[ISlicingData::SetBoundingBoxDirection3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~SetBoundingBoxDirection3.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
