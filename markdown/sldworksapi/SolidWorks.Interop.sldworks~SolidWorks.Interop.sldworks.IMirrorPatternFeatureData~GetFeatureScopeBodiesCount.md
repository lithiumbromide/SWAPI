---
title: "GetFeatureScopeBodiesCount Method (IMirrorPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPatternFeatureData"
member: "GetFeatureScopeBodiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~GetFeatureScopeBodiesCount.html"
---

# GetFeatureScopeBodiesCount Method (IMirrorPatternFeatureData)

Gets the number of solid bodies affected by the mirror pattern feature in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatureScopeBodiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPatternFeatureData
Dim value As System.Integer

value = instance.GetFeatureScopeBodiesCount()
```

### C#

```csharp
System.int GetFeatureScopeBodiesCount()
```

### C++/CLI

```cpp
System.int GetFeatureScopeBodiesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of solid bodies affected

## VBA Syntax

See [MirrorPatternFeatureData::GetFeatureScopeBodiesCount](ms-its:sldworksapivb6.chm::/Sldworks~MirrorPatternFeatureData~GetFeatureScopeBodiesCount.html).

## Remarks

Call this method before calling [IMirrorPatternFeatureData::IGetFeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMirrorPatternFeatureData~IGetFeatureScopeBodies.html) to get the size of the array for that method.

## See Also

[IMirrorPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData.html)
[IMirrorPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData_members.html)
[IMirrorPatternFeatureData::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~ISetFeatureScopeBodies.html)
[IMirrorPatternFeatureData::FeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~FeatureScope.html)
[IMirrorPatternFeatureData::FeatureScopeBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~FeatureScopeBodies.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
