---
title: "GetBasePoint Method (ISketchPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISketchPatternFeatureData"
member: "GetBasePoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~GetBasePoint.html"
---

# GetBasePoint Method (ISketchPatternFeatureData)

Gets the base point data from which this sketch pattern is created.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBasePoint() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPatternFeatureData
Dim value As System.Object

value = instance.GetBasePoint()
```

### C#

```csharp
System.object GetBasePoint()
```

### C++/CLI

```cpp
System.Object^ GetBasePoint();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles describing the x, y, and z values of the base point

## VBA Syntax

See [SketchPatternFeatureData::GetBasePoint](ms-its:sldworksapivb6.chm::/sldworks~SketchPatternFeatureData~GetBasePoint.html).

## Examples

See the [ISketchPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html) examples.

## See Also

[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html)
[ISketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members.html)
[ISketchPatternFeatureData::IGetBasePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~IGetBasePoint.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
