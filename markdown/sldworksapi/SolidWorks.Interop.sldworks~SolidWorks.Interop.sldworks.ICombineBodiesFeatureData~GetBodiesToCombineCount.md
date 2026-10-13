---
title: "GetBodiesToCombineCount Method (ICombineBodiesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICombineBodiesFeatureData"
member: "GetBodiesToCombineCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~GetBodiesToCombineCount.html"
---

# GetBodiesToCombineCount Method (ICombineBodiesFeatureData)

Gets the number of bodies to combine.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBodiesToCombineCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICombineBodiesFeatureData
Dim value As System.Integer

value = instance.GetBodiesToCombineCount()
```

### C#

```csharp
System.int GetBodiesToCombineCount()
```

### C++/CLI

```cpp
System.int GetBodiesToCombineCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of bodies to combine

## VBA Syntax

See [CombineBodiesFeatureData::GetBodiesToCombineCount](ms-its:sldworksapivb6.chm::/sldworks~CombineBodiesFeatureData~GetBodiesToCombineCount.html).

## Remarks

Call this method before calling [ICombineBodiesFeatureData::IGetBodiesToCombine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICombineBodiesFeatureData~IGetBodiesToCombine.html) to determine the size of the array for that method.

## See Also

[ICombineBodiesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData.html)
[ICombineBodiesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData_members.html)
[IColorTable::ISetBodiesToCombine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~ISetBodiesToCombine.html)
[IColorTable::BodiesToCombine Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~BodiesToCombine.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
