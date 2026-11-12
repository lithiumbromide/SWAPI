---
title: "GetInstanceDimensionName Method (IDimPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDimPatternFeatureData"
member: "GetInstanceDimensionName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceDimensionName.html"
---

# GetInstanceDimensionName Method (IDimPatternFeatureData)

Gets the name of the pattern dimension for the pattern instance in this variable pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetInstanceDimensionName( _
   ByVal InstanceName As System.String, _
   ByVal ControllingDimName As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDimPatternFeatureData
Dim InstanceName As System.String
Dim ControllingDimName As System.String
Dim value As System.String

value = instance.GetInstanceDimensionName(InstanceName, ControllingDimName)
```

### C#

```csharp
System.string GetInstanceDimensionName(
   System.string InstanceName,
   System.string ControllingDimName
)
```

### C++/CLI

```cpp
System.String^ GetInstanceDimensionName(
   System.String^ InstanceName,
   System.String^ ControllingDimName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InstanceName`: Name of the pattern instance (see **Remarks**)
- `ControllingDimName`: Controlling dimension of the pattern instance (see **Remarks**)

### Return Value

Name of the pattern dimension

## VBA Syntax

See [DimPatternFeatureData::GetInstanceDimensionName](ms-its:sldworksapivb6.chm::/sldworks~DimPatternFeatureData~GetInstanceDimensionName.html).

## Examples

[Insert Variable Pattern Feature (C#)](Insert_Advanced_Variable_Pattern_Feature_Example_CSharp.htm)
[Insert Variable Pattern Feature (VB.NET)](Insert_Advanced_Variable_Pattern_Feature_Example_VBNET.htm)
[Insert Variable Pattern Feature (VBA)](Insert_Advanced_Variable_Pattern_Feature_Example_VB.htm)

## Remarks

| Use.. | To get... |
| --- | --- |
| IDimPatternFeatureData::GetInstanceNameByIndex | InstanceName |
| IDimPatternFeatureData::GetControllingDimensionName | ControllingDimName |

## See Also

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.html)
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.html)
[IDimPatternFeatureData::SetInstanceDimensionValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~SetInstanceDimensionValue.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
