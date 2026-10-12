---
title: "SetInstanceSuppressStateByName Method (IDimPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDimPatternFeatureData"
member: "SetInstanceSuppressStateByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~SetInstanceSuppressStateByName.html"
---

# SetInstanceSuppressStateByName Method (IDimPatternFeatureData)

Sets whether a pattern instance with the specified name is suppressed in this variable pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetInstanceSuppressStateByName( _
   ByVal InstanceName As System.String, _
   ByVal SuppressState As System.Boolean _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDimPatternFeatureData
Dim InstanceName As System.String
Dim SuppressState As System.Boolean
Dim value As System.String

value = instance.SetInstanceSuppressStateByName(InstanceName, SuppressState)
```

### C#

```csharp
System.string SetInstanceSuppressStateByName(
   System.string InstanceName,
   System.bool SuppressState
)
```

### C++/CLI

```cpp
System.String^ SetInstanceSuppressStateByName(
   System.String^ InstanceName,
   System.bool SuppressState
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InstanceName`: Name of pattern instance to suppress (see **Remarks**)
- `SuppressState`: True if the pattern instance is suppressed, false if not

### Return Value

| If the pattern instance is... | Then Return Value is an... |
| --- | --- |
| Suppressed | Empty string indicating success |
| Not suppressed | Error string |

## VBA Syntax

See [DimPatternFeatureData::SetInstanceSuppressStateByName](ms-its:sldworksapivb6.chm::/sldworks~DimPatternFeatureData~SetInstanceSuppressStateByName.html).

## Remarks

Use [IDimPatternFeatureData::GetInstanceNameByIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceNameByIndex.html) to get InstanceName.

## See Also

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.html)
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.html)
[IDimPatternFeatureData::GetInstanceSuppressStateByName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceSuppressStateByName.html)
[IDimPatternFeatureData::GetInstanceSuppressStateByIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceSuppressStateByIndex.html)
[IDimPatternFeatureData::SetInstanceSuppressStateByIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~SetInstanceSuppressStateByIndex.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
