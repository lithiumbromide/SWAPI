---
title: "GetEdgesCount Method (IHemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHemFeatureData"
member: "GetEdgesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~GetEdgesCount.html"
---

# GetEdgesCount Method (IHemFeatureData)

Gets the number of edges for this hem.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdgesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IHemFeatureData
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

See [HemFeatureData::GetEdgesCount](ms-its:sldworksapivb6.chm::/sldworks~HemFeatureData~GetEdgesCount.html).

## Remarks

Call this method before calling [IHemFeatureData::IGetEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHemFeatureData~IGetEdges.html).

## See Also

[IHemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData.html)
[IHemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData_members.html)
[IHemFeatureData::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~ISetEdges.html)
[IHemFeatureData::Edges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~Edges.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10,1
