---
title: "GetInstanceSuppressStateByName Method (IDimPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDimPatternFeatureData"
member: "GetInstanceSuppressStateByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceSuppressStateByName.html"
---

# GetInstanceSuppressStateByName Method (IDimPatternFeatureData)

Gets whether the pattern instance with the specified name is suppressed in this variable pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetInstanceSuppressStateByName( _
   ByVal InstanceName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimPatternFeatureData
Dim InstanceName As System.String
Dim value As System.Boolean

value = instance.GetInstanceSuppressStateByName(InstanceName)
```

### C#

```csharp
System.bool GetInstanceSuppressStateByName(
   System.string InstanceName
)
```

### C++/CLI

```cpp
System.bool GetInstanceSuppressStateByName(
   System.String^ InstanceName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InstanceName`: Name of the pattern instance (see **Remarks**)

### Return Value

True if the pattern instance is suppressed, false if not

## VBA Syntax

See [DimPatternFeatureData::GetInstanceSuppressStateByName](ms-its:sldworksapivb6.chm::/sldworks~DimPatternFeatureData~GetInstanceSuppressStateByName.html).

## Remarks

Use [IDimPatternFeatureData::GetInstanceNameByIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceNameByIndex.html) to get InstanceName.

## See Also

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.html)
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.html)
[IDimPatternFeatureData::SetInstanceSuppressStateByName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~SetInstanceSuppressStateByName.html)
[IDimPatternFeatureData::GetInstanceSuppressStateByIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceSuppressStateByIndex.html)
[IDimPatternFeatureData::SetInstanceSuppressStateByIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~SetInstanceSuppressStateByIndex.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
