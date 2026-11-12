---
title: "GetBoundingBoxDirection4 Method (ISlicingData)"
project: "SOLIDWORKS API Help"
interface: "ISlicingData"
member: "GetBoundingBoxDirection4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection4.html"
---

# GetBoundingBoxDirection4 Method (ISlicingData)

Gets bounding box direction 4 (bottom manipulator for linear slicing, outer radius for radial slicing).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBoundingBoxDirection4() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISlicingData
Dim value As System.Double

value = instance.GetBoundingBoxDirection4()
```

### C#

```csharp
System.double GetBoundingBoxDirection4()
```

### C++/CLI

```cpp
System.double GetBoundingBoxDirection4();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

For linear slicing:

-500.0 < bottom manipulator < 0

For radial slicing:

Inner radius < outer radius < user-interface maximum for this case

## VBA Syntax

See [SlicingData::GetBoundingBoxDirection4](ms-its:sldworksapivb6.chm::/sldworks~SlicingData~GetBoundingBoxDirection4.html).

## Examples

See the [ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html) example.

## Remarks

This method is only valid after you have pre-selected the first slicing plane.

Use these methods to get the slicing volume for including or excluding geometry for slicing:

- [ISlicingData::GetBoundingBoxDirection1](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection1.html)
- [ISlicingData::GetBoundingBoxDirection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection2.html)
- [ISlicingData::GetBoundingBoxDirection3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection3.html)
- ISlicingData::GetBoundingBoxDirection4

## See Also

[ISlicingData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html)
[ISlicingData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData_members.html)
[ISlicingData::SetBoundingBoxDirection4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~SetBoundingBoxDirection4.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
