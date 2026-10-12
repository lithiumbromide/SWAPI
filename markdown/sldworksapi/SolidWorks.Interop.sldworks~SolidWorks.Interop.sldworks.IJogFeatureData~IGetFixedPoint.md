---
title: "IGetFixedPoint Method (IJogFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJogFeatureData"
member: "IGetFixedPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~IGetFixedPoint.html"
---

# IGetFixedPoint Method (IJogFeatureData)

Gets the fixed-point x, y, z coordinates for this jog feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFixedPoint() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IJogFeatureData
Dim value As System.Double

value = instance.IGetFixedPoint()
```

### C#

```csharp
System.double IGetFixedPoint()
```

### C++/CLI

```cpp
System.double IGetFixedPoint();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of fixed-point coordinates

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.html)
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.html)
[IJogFeatureData::ISetFixedPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~ISetFixedPoint.html)
[IJogFeatureData::FixedPoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~FixedPoint.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
