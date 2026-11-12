---
title: "GetSplitTargetsCount Method (ISplitLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitLineFeatureData"
member: "GetSplitTargetsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~GetSplitTargetsCount.html"
---

# GetSplitTargetsCount Method (ISplitLineFeatureData)

Gets the number of faces or bodies to split.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSplitTargetsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitLineFeatureData
Dim value As System.Integer

value = instance.GetSplitTargetsCount()
```

### C#

```csharp
System.int GetSplitTargetsCount()
```

### C++/CLI

```cpp
System.int GetSplitTargetsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of faces or bodies to split

## VBA Syntax

See [SplitLineFeatureData::GetSplitTargetsCount](ms-its:sldworksapivb6.chm::/sldworks~SplitLineFeatureData~GetSplitTargetsCount.html).

## Remarks

Call this method before calling [ISplitLineFeatureData::IGetSplitTargets](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitLineFeatureData~IGetSplitTargets.html) to get the size of the array for that method.

## See Also

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html)
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.html)
[ISplitLineFeatureData::ISetSplitTargets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~ISetSplitTargets.html)
[ISplitLineFeatureData::SplitTargets Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SplitTargets.html)
[ISplitLineFeatureData::SplitAll Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SplitAll.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
