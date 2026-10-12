---
title: "IGetConfigurations Method (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "IGetConfigurations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~IGetConfigurations.html"
---

# IGetConfigurations Method (IBomFeature)

Gets the configurations available to this BOM table or used in this BOM table.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetConfigurations( _
   ByVal OnlyVisible As System.Boolean, _
   ByVal Count As System.Integer, _
   ByRef Visible As System.Boolean _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim OnlyVisible As System.Boolean
Dim Count As System.Integer
Dim Visible As System.Boolean
Dim value As System.String

value = instance.IGetConfigurations(OnlyVisible, Count, Visible)
```

### C#

```csharp
System.string IGetConfigurations(
   System.bool OnlyVisible,
   System.int Count,
   out System.bool Visible
)
```

### C++/CLI

```cpp
System.String^ IGetConfigurations(
   System.bool OnlyVisible,
   System.int Count,
   [Out] System.bool Visible
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OnlyVisible`: True to get the names of configurations currently displayed in this table, false
  to get the names of configurations available to this table
- `Count`: Number of items in the Visible and Names arguments
- `Visible`: Array of BOOLEANs indicating the visibility of the configurations

### Return Value

- in-process, unmanaged C++: Pointer to an array of strings of the names of the configurations

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Although this method works on all styles of BOM tables (top-level only, parts-only, indented subassemblies), it is only necessary for top-level only style tables. For the other style tables, where only a single configuration is shown at a time, using [IBomFeature::Configuration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~Configuration.html) is simpler and more efficient.

The view associated with this BOM can contain a model with multiple configurations. For a top-level only style BOM table, there can be several Quantity columns, each showing the results for a different configuration. For the other styles of BOM tables, only a particular configuration can be shown in the table, and that configuration can be changed. To determine the BOM table style, use the [IBomFeature::TableType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~TableType.html) property.

| If OnlyVisible is... | Then Names contains the names of... | And Visible... |
| --- | --- | --- |
| True | Only the configurations currently shown in the BOM table. For a top-level only style BOM table, this could be any number of configurations. For the other styles of BOM tables, it is one configuration name. | Can be passed in as NULL. If it is passed in as non-NULL, the array contains True for all items. |
| False | All configurations available. | Contains BOOLEANs that correspond to each item in Names indicating if that particular configuration is shown in the BOM table or not. |

To get the number of configurations, use [IBomFeature::GetConfigurationCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~GetConfigurationCount.html).

To set the configurations, use [IBomFeature::ISetConfigurations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~ISetConfigurations.html).

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)
[IBomFeature::ISetConfigurations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~ISetConfigurations.html)
[IBomFeature::GetConfigurations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetConfigurations.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12
