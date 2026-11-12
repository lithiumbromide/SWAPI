---
title: "GetConfigurations Method (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "GetConfigurations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetConfigurations.html"
---

# GetConfigurations Method (IBomFeature)

Gets the configurations available to this BOM table or used in this BOM table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConfigurations( _
   ByVal OnlyVisible As System.Boolean, _
   ByRef Visible As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim OnlyVisible As System.Boolean
Dim Visible As System.Object
Dim value As System.Object

value = instance.GetConfigurations(OnlyVisible, Visible)
```

### C#

```csharp
System.object GetConfigurations(
   System.bool OnlyVisible,
   out System.object Visible
)
```

### C++/CLI

```cpp
System.Object^ GetConfigurations(
   System.bool OnlyVisible,
   [Out] System.Object^ Visible
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OnlyVisible`: True to get the names of configurations currently displayed in this table, false to get the names of configurations available to this table
- `Visible`: Array of BOOLEANs indicating the visibility of the configurations

### Return Value

Array of strings of the names of the configurations

## VBA Syntax

See [BomFeature::GetConfigurations](ms-its:sldworksapivb6.chm::/sldworks~BomFeature~GetConfigurations.html).

## Examples

[Insert BOM Table (C#)](Insert_BOM_Table_Example_CSharp.htm)
[Insert BOM Table (VB.NET)](Insert_BOM_Table_Example_VBNET.htm)
[Insert BOM Table (VBA)](Insert_BOM_Table_Example_VB.htm)

## Remarks

Although this method works on all styles of BOM tables (top-level only, parts-only, indented subassemblies), it is only necessary for top-level only style tables. For the other style tables, where only a single configuration is shown at a time, using [IBomFeature::Configuration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~Configuration.html) is simpler and more efficient.

The view associated with this BOM can contain a model with multiple configurations. For a top-level only style BOM table, there can be several Quantity columns, each showing the results for a different configuration. For the other styles of BOM tables, only a particular configuration can be shown in the table, and that configuration can be changed. To determine the BOM table style, use the [IBomFeature::TableType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~TableType.html) property.

| If OnlyVisible is... | Then Names contains the names of... | And Visible... |
| --- | --- | --- |
| True | Only the configurations currently shown in the BOM table. For a top-level only style BOM table, this could be any number of configurations. For the other styles of BOM tables, it is one configuration name. | Can be passed in as NULL. If it is passed in as non-NULL, the array contains True for all items. |
| False | All configurations available. | Contains BOOLEANs that correspond to each item in Names indicating if that particular configuration is shown in the BOM table or not. |

To get the number of configurations, use [IBomFeature::GetConfigurationCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~GetConfigurationCount.html).

To set the configurations, use [IBomFeature::SetConfigurations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~SetConfigurations.html).

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)
[IBomFeature::IGetConfigurations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~IGetConfigurations.html)
[IBomFeature::SetConfigurations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~SetConfigurations.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12
