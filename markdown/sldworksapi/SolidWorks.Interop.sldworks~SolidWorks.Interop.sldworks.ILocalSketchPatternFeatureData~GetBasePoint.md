---
title: "GetBasePoint Method (ILocalSketchPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalSketchPatternFeatureData"
member: "GetBasePoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~GetBasePoint.html"
---

# GetBasePoint Method (ILocalSketchPatternFeatureData)

Gets the data for the base point from which this sketch-driven component pattern feature is created.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBasePoint() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalSketchPatternFeatureData
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

See [LocalSketchPatternFeatureData::GetBasePoint](ms-its:sldworksapivb6.chm::/sldworks~LocalSketchPatternFeatureData~GetBasePoint.html).

## See Also

[ILocalSketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData.html)
[ILocalSketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
