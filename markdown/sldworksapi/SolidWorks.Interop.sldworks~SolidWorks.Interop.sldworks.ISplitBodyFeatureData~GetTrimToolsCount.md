---
title: "GetTrimToolsCount Method (ISplitBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitBodyFeatureData"
member: "GetTrimToolsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetTrimToolsCount.html"
---

# GetTrimToolsCount Method (ISplitBodyFeatureData)

Gets the number of trimming surfaces used as trim tools in this Split feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTrimToolsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitBodyFeatureData
Dim value As System.Integer

value = instance.GetTrimToolsCount()
```

### C#

```csharp
System.int GetTrimToolsCount()
```

### C++/CLI

```cpp
System.int GetTrimToolsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of trimming surfaces used as trim tools in this Split feature

## VBA Syntax

See [SplitBodyFeatureData::GetTrimToolsCount](ms-its:sldworksapivb6.chm::/sldworks~SplitBodyFeatureData~GetTrimToolsCount.html).

## Remarks

Call this method before calling [ISplitBodyFeatureData::IGetTrimTools](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitBodyFeatureData~IGetTrimTools.html) to determine the size of the array for that method.

## See Also

[ISplitBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.html)
[ISplitBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.html)
[ISplitBodyFeatureData::TrimTools Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~TrimTools.html)
[ISplitBodyFeatureData::ISetTrimTools Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~ISetTrimTools.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
