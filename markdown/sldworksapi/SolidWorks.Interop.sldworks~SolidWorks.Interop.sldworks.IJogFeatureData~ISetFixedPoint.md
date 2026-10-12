---
title: "ISetFixedPoint Method (IJogFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJogFeatureData"
member: "ISetFixedPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~ISetFixedPoint.html"
---

# ISetFixedPoint Method (IJogFeatureData)

Sets the fixed-point x, y, z coordinates for this jog feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetFixedPoint( _
   ByRef Point As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IJogFeatureData
Dim Point As System.Double

instance.ISetFixedPoint(Point)
```

### C#

```csharp
void ISetFixedPoint(
   ref System.double Point
)
```

### C++/CLI

```cpp
void ISetFixedPoint(
   System.double% Point
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Point`: - in-process, unmanaged C++: Pointer to an array of fixed-point coordinates

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.html)
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.html)
[IJogFeatureData::IGetFixedPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~IGetFixedPoint.html)
[IJogFeatureData::FixedPoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~FixedPoint.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
