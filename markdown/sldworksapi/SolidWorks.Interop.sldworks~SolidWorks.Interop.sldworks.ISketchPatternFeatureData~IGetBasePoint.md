---
title: "IGetBasePoint Method (ISketchPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISketchPatternFeatureData"
member: "IGetBasePoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~IGetBasePoint.html"
---

# IGetBasePoint Method (ISketchPatternFeatureData)

Gets the base point data from which this sketch pattern is created.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBasePoint() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPatternFeatureData
Dim value As System.Double

value = instance.IGetBasePoint()
```

### C#

```csharp
System.double IGetBasePoint()
```

### C++/CLI

```cpp
System.double IGetBasePoint();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles describing the x, y, and z coordinates of the base point
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [SketchPatternFeatureData::IGetBasePoint](ms-its:sldworksapivb6.chm::/sldworks~SketchPatternFeatureData~IGetBasePoint.html).

## See Also

[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html)
[ISketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members.html)
[ISketchPatternFeatureData::GetBasePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~GetBasePoint.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
