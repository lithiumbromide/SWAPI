---
title: "GetBoundingBoxDirection1 Method (ISlicingData)"
project: "SOLIDWORKS API Help"
interface: "ISlicingData"
member: "GetBoundingBoxDirection1"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection1.html"
---

# GetBoundingBoxDirection1 Method (ISlicingData)

Gets bounding box direction 1 (top manipulator for both linear and radial slicing).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBoundingBoxDirection1() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISlicingData
Dim value As System.Double

value = instance.GetBoundingBoxDirection1()
```

### C#

```csharp
System.double GetBoundingBoxDirection1()
```

### C++/CLI

```cpp
System.double GetBoundingBoxDirection1();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

0.0 < top manipulator < 500.0

## VBA Syntax

See [SlicingData::GetBoundingBoxDirection1](ms-its:sldworksapivb6.chm::/sldworks~SlicingData~GetBoundingBoxDirection1.html).

## Examples

See the [ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html) example.

## Remarks

This method is only valid after you have pre-selected the first slicing plane.

Use these methods to get the slicing volume for including or excluding geometry for slicing:

- ISlicingData::GetBoundingBoxDirection1
- [ISlicingData::GetBoundingBoxDirection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection2.html)
- [ISlicingData::GetBoundingBoxDirection3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection3.html)
- [ISlicingData::GetBoundingBoxDirection4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~GetBoundingBoxDirection4.html)

## See Also

[ISlicingData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html)
[ISlicingData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData_members.html)
[ISlicingData::SetBoundingBoxDirection1 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~SetBoundingBoxDirection1.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
