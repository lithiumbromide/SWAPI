---
title: "GetInstanceIndex Method (IDimPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDimPatternFeatureData"
member: "GetInstanceIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceIndex.html"
---

# GetInstanceIndex Method (IDimPatternFeatureData)

Gets the index of the pattern instance in the FeatureManager design tree in the variable pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetInstanceIndex( _
   ByVal InstanceName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimPatternFeatureData
Dim InstanceName As System.String
Dim value As System.Integer

value = instance.GetInstanceIndex(InstanceName)
```

### C#

```csharp
System.int GetInstanceIndex(
   System.string InstanceName
)
```

### C++/CLI

```cpp
System.int GetInstanceIndex(
   System.String^ InstanceName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InstanceName`: Name of the pattern instance (see **Remarks**)

### Return Value

Index of InstanceName in the FeatureManager design tree

## VBA Syntax

See [DimPatternFeatureData::GetInstanceIndex](ms-its:sldworksapivb6.chm::/sldworks~DimPatternFeatureData~GetInstanceIndex.html).

## Remarks

Use [IDimPatternFeatureData::GetInstanceNameByIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceNameByIndex.html) to get InstanceName.

## See Also

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.html)
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.html)
[IDimPatternFeatureData::GetInstanceCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceCount.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
