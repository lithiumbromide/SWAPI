---
title: "ISetConfigurations Method (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "ISetConfigurations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~ISetConfigurations.html"
---

# ISetConfigurations Method (IBomFeature)

Sets the configurations used in this BOM table.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetConfigurations( _
   ByVal OnlyVisible As System.Boolean, _
   ByVal Count As System.Integer, _
   ByRef Visible As System.Boolean, _
   ByRef Names As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim OnlyVisible As System.Boolean
Dim Count As System.Integer
Dim Visible As System.Boolean
Dim Names As System.String
Dim value As System.Boolean

value = instance.ISetConfigurations(OnlyVisible, Count, Visible, Names)
```

### C#

```csharp
System.bool ISetConfigurations(
   System.bool OnlyVisible,
   System.int Count,
   ref System.bool Visible,
   ref System.string Names
)
```

### C++/CLI

```cpp
System.bool ISetConfigurations(
   System.bool OnlyVisible,
   System.int Count,
   System.bool% Visible,
   System.String^% Names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OnlyVisible`: Indicator of the contents of the arrays (see **Remarks**)
- `Count`: Number of items in Visible and Names
- `Visible`: - in-process, unmanaged C++: Pointer to an array of Booleans indicating the visibility of the configurations

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `Names`: - in-process, unmanaged C++: Pointer to an array of strings of the names of the configurations

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

True if configurations are set, false if not

## Remarks

Although this method works on all styles of BOM tables (top-level only, parts-only, indented subassemblies), it is only necessary for top-level only style tables. For the other style tables, where only a single configuration is shown at a time, using [IBomFeature::Configuration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~Configuration.html) is simpler and more efficient.

**NOTE:** If the **Restrict top-level only BOMs to one configuration** option on the **Document Properties > Tables > Bill of Materials** dialog or [IModelDocExtension::GetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceToggle.html)([swUserPreferenceToggle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceToggle_e.html).swOneConfigOnlyTopLevelBom) returns true, then only the active or default configuration of the drawing view is inserted in the BOM.

The view associated with this BOM can contain a model with multiple configurations. For a top-level only style BOM table, there can be several Quantity columns, each showing the results for a different configuration. For the other styles of BOM tables, only a particular configuration can be shown in the table, and that configuration can be changed. To determine the BOM table style, use the [IBomFeature::TableType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~TableType.html) property.

| If OnlyVisible is... | Then Names contains the names of... | And Visible... |
| --- | --- | --- |
| True | Only the configurations currently shown in the BOM table. For a top-level only style BOM table, this could be any number of configurations. For the other styles of BOM tables, it is one configuration name. | Can be passed in as null. If it is passed in as non-null, the array contains true for all items. |
| False | All configurations available. | Contains Booleans that correspond to each item in Names indicating if that particular configuration is shown in the BOM table or not. |

To get the number of configurations, use [IBomFeature::GetConfigurationCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~GetConfigurationCount.html).

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)
[IBomFeature::SetConfigurations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~SetConfigurations.html)
[IBomFeature::IGetConfigurations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~IGetConfigurations.html)

## Availability

SOLIDWORKS 2004 FCS, revision Number 12
