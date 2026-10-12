---
title: "SetConfigurations Method (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "SetConfigurations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~SetConfigurations.html"
---

# SetConfigurations Method (IBomFeature)

Sets the configurations used in this BOM table.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetConfigurations( _
   ByVal OnlyVisible As System.Boolean, _
   ByVal Visible As System.Object, _
   ByVal Names As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim OnlyVisible As System.Boolean
Dim Visible As System.Object
Dim Names As System.Object
Dim value As System.Boolean

value = instance.SetConfigurations(OnlyVisible, Visible, Names)
```

### C#

```csharp
System.bool SetConfigurations(
   System.bool OnlyVisible,
   System.object Visible,
   System.object Names
)
```

### C++/CLI

```cpp
System.bool SetConfigurations(
   System.bool OnlyVisible,
   System.Object^ Visible,
   System.Object^ Names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OnlyVisible`: Indicator of the contents of the arrays (see **Remarks**)
- `Visible`: Array of Booleans indicating the visibility of the configurations
- `Names`: Array of strings of the names of the configurations

### Return Value

True if configurations are set, false if not

## VBA Syntax

See [BomFeature::SetConfigurations](ms-its:sldworksapivb6.chm::/sldworks~BomFeature~SetConfigurations.html).

## Examples

[Insert BOM Table (C#)](Insert_BOM_Table_Example_CSharp.htm)
[Insert BOM Table (VB.NET)](Insert_BOM_Table_Example_VBNET.htm)
[Insert BOM Table (VBA)](Insert_BOM_Table_Example_VB.htm)

## Remarks

Although this method works on all styles of BOM tables (top-level only, parts-only, indented subassemblies), it is only necessary for top-level only style tables. For the other style tables, where only a single configuration is shown at a time, using [IBomFeature::Configuration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~Configuration.html) is simpler and more efficient.

**NOTE:** If the **Restrict top-level only BOMs to one configuration** option on the **Document Properties > Tables > Bill of Materials** dialog or [IModelDocExtension::GetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceToggle.html)([swUserPreferenceToggle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceToggle_e.html).swOneConfigOnlyTopLevelBom) returns true, then only the active or default configuration of the drawing view is inserted in the BOM.

The view associated with this BOM can contain a model with multiple configurations. For a top-level only style BOM table, there can be several Quantity columns, each showing the results for a different configuration. For the other styles of BOM tables, only a particular configuration can be shown in the table, and that configuration can be changed. To determine the BOM table style, use the [IBomFeature::TableType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~TableType.html) property.

| If OnlyVisible is... | Then Names contains the names of... | And Visible... |
| --- | --- | --- |
| True | Only the configurations currently shown in the BOM table. For a top-level only style BOM table, this could be any number of configurations. For the other styles of BOM tables, it is one configuration name. | Can be passed in as null or nothing. If it is passed in as non-null or non-nothing, then the array contains true for all items. |
| False | All configurations available. | Contains Booleans that correspond to each item in Names indicating if that particular configuration is shown in the BOM table or not. |

To get the number of configurations, use [IBomFeature::GetConfigurationCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~GetConfigurationCount.html).

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)
[IBomFeature::GetConfigurations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetConfigurations.html)
[IBomFeature::ISetConfigurations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~ISetConfigurations.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12
