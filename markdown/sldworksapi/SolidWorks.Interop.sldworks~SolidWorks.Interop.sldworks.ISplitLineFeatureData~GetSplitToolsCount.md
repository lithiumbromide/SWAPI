---
title: "GetSplitToolsCount Method (ISplitLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitLineFeatureData"
member: "GetSplitToolsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~GetSplitToolsCount.html"
---

# GetSplitToolsCount Method (ISplitLineFeatureData)

Gets the number of tools used to make the split.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSplitToolsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitLineFeatureData
Dim value As System.Integer

value = instance.GetSplitToolsCount()
```

### C#

```csharp
System.int GetSplitToolsCount()
```

### C++/CLI

```cpp
System.int GetSplitToolsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of tools used to make the split

## VBA Syntax

See [SplitLineFeatureData::GetSplitToolsCount](ms-its:sldworksapivb6.chm::/sldworks~SplitLineFeatureData~GetSplitToolsCount.html).

## Remarks

Call this method before calling [ISplitLineFeatureData::IGetSplitTools](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitLineFeatureData~IGetSplitTools.html) to determine the size of the array for that method.

## See Also

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html)
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.html)
[ISplitLineFeatureData::ISetSplitTools Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~ISetSplitTools.html)
[ISplitLineFeatureData::SplitTools Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SplitTools.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
