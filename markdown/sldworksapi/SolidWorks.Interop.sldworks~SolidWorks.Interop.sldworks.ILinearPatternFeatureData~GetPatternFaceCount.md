---
title: "GetPatternFaceCount Method (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "GetPatternFaceCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetPatternFaceCount.html"
---

# GetPatternFaceCount Method (ILinearPatternFeatureData)

Gets the number of seed faces in this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPatternFaceCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
Dim value As System.Integer

value = instance.GetPatternFaceCount()
```

### C#

```csharp
System.int GetPatternFaceCount()
```

### C++/CLI

```cpp
System.int GetPatternFaceCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of seed faces

## VBA Syntax

See [LinearPatternFeatureData::GetPatternFaceCount](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~GetPatternFaceCount.html).

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[ILinearPatternFeatureData::IGetPatternFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~IGetPatternFaceArray.html)
[ILinearPatternFeatureData::ISetPatternFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~ISetPatternFaceArray.html)
[ILinearPatternFeatureData::PatternFaceArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~PatternFaceArray.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
