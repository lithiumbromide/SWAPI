---
title: "GetConfigurationCount Method (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "GetConfigurationCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetConfigurationCount.html"
---

# GetConfigurationCount Method (IBomFeature)

Gets the number of configurations available to this BOM table or used in this BOM table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConfigurationCount( _
   ByVal OnlyVisible As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim OnlyVisible As System.Boolean
Dim value As System.Integer

value = instance.GetConfigurationCount(OnlyVisible)
```

### C#

```csharp
System.int GetConfigurationCount(
   System.bool OnlyVisible
)
```

### C++/CLI

```cpp
System.int GetConfigurationCount(
   System.bool OnlyVisible
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OnlyVisible`: True to get the number of configurations currently displayed in this table, false to get the total number of configurations available in this table

### Return Value

Number of configurations in this BOM table or available to this BOM table

## VBA Syntax

See [BomFeature::GetConfigurationCount](ms-its:sldworksapivb6.chm::/sldworks~BomFeature~GetConfigurationCount.html).

## Remarks

The view associated with this BOM can contain a model with multiple configurations.

For a top-level only style BOM table, there can be several Quantity columns, each showing the results for a different configuration. For the other styles of BOM tables, only a particular configuration can be shown in the table, and that configuration can be changed. To determine the style of the BOM table, use [IBomFeature::TableType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~TableType.html).

| If OnlyVisible is... | Then the value returned is... |
| --- | --- |
| True | Number of configurations currently shown in the BOM table. For a top-level only style BOM table, this could be any number from 0 to the total number of configurations available. For the other styles of BOM tables, this value is always 1. |
| false | Total number of configurations available. |

To get the configuration names, call [IBomFeature::GetConfigurations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~GetConfigurations.html) or [IBomFeature::IGetConfigurations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~IGetConfigurations.html).

Call this method before calling IBomFeature::IGetConfigurations to get the number of configurations.

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12
