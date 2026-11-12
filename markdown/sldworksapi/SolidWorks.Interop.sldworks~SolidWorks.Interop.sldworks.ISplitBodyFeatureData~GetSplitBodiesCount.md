---
title: "GetSplitBodiesCount Method (ISplitBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitBodyFeatureData"
member: "GetSplitBodiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodiesCount.html"
---

# GetSplitBodiesCount Method (ISplitBodyFeatureData)

Gets the number of split bodies in this Split feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSplitBodiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitBodyFeatureData
Dim value As System.Integer

value = instance.GetSplitBodiesCount()
```

### C#

```csharp
System.int GetSplitBodiesCount()
```

### C++/CLI

```cpp
System.int GetSplitBodiesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of split bodies

## VBA Syntax

See [SplitBodyFeatureData::GetSplitBodiesCount](ms-its:sldworksapivb6.chm::/sldworks~SplitBodyFeatureData~GetSplitBodiesCount.html).

## Remarks

Call this method before calling [ISplitBodyFeatureData::IGetSplitBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitBodyFeatureData~IGetSplitBodies.html) to determine the size of the array for that method.

## See Also

[ISplitBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.html)
[ISplitBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.html)
[ISplitBodyFeatureData::GetSplitBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodies.html)
[ISplitBodyFeatureData::ISetSplitBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~ISetSplitBodies.html)
[ISplitBodyFeatureData::SetSplitBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
