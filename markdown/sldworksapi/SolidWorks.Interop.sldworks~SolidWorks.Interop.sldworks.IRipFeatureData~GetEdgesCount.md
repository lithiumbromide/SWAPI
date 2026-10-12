---
title: "GetEdgesCount Method (IRipFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRipFeatureData"
member: "GetEdgesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~GetEdgesCount.html"
---

# GetEdgesCount Method (IRipFeatureData)

Gets the number of edges for this rip feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdgesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRipFeatureData
Dim value As System.Integer

value = instance.GetEdgesCount()
```

### C#

```csharp
System.int GetEdgesCount()
```

### C++/CLI

```cpp
System.int GetEdgesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of edges

## VBA Syntax

See [RipFeatureData::GetEdgesCount](ms-its:sldworksapivb6.chm::/sldworks~RipFeatureData~GetEdgesCount.html).

## Examples

See the [IRipFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData.html) examples.

## Remarks

Call this method before calling [IRipFeatureData::IGetEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRipFeatureData~IGetEdges.html) to get the size of the array for that method.

## See Also

[IRipFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData.html)
[IRipFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData_members.html)
[IRipFeatureData::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~ISetEdges.html)
[IRipFeatureData::Edges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~Edges.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
