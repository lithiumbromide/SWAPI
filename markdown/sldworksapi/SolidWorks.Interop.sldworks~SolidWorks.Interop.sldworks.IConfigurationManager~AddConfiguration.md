---
title: "AddConfiguration Method (IConfigurationManager)"
project: "SOLIDWORKS API Help"
interface: "IConfigurationManager"
member: "AddConfiguration"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddConfiguration.html"
---

# AddConfiguration Method (IConfigurationManager)

Obsolete. Superseded by [IConfigurationManager::AddConfiguration2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddConfiguration2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddConfiguration( _
   ByVal Name As System.String, _
   ByVal Comment As System.String, _
   ByVal AlternateName As System.String, _
   ByVal Options As System.Integer, _
   ByVal ParentConfigName As System.String, _
   ByVal Description As System.String _
) As Configuration
```

### Visual Basic (Usage)

```vb
Dim instance As IConfigurationManager
Dim Name As System.String
Dim Comment As System.String
Dim AlternateName As System.String
Dim Options As System.Integer
Dim ParentConfigName As System.String
Dim Description As System.String
Dim value As Configuration

value = instance.AddConfiguration(Name, Comment, AlternateName, Options, ParentConfigName, Description)
```

### C#

```csharp
Configuration AddConfiguration(
   System.string Name,
   System.string Comment,
   System.string AlternateName,
   System.int Options,
   System.string ParentConfigName,
   System.string Description
)
```

### C++/CLI

```cpp
Configuration^ AddConfiguration(
   System.String^ Name,
   System.String^ Comment,
   System.String^ AlternateName,
   System.int Options,
   System.String^ ParentConfigName,
   System.String^ Description
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of the configuration
- `Comment`: Comment displayed in Configuration Properties
- `AlternateName`: Alternate configuration name (i.e., user-specified name); used if swConfigOption_UseAlternateName is set to true
- `Options`: Combination of one or more Boolean configuration options as defined in [swConfigurationOptions2_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConfigurationOptions2_e.html) (see **Remarks**)
- `ParentConfigName`: Name of parent configuration
- `Description`: Text that identifies the configuration

### Return Value

Newly created [configuration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration.html)

## VBA Syntax

See [ConfigurationManager::AddConfiguration](ms-its:sldworksapivb6.chm::/sldworks~ConfigurationManager~AddConfiguration.html).

## Examples

[Set Dimensions to Mid-Tolerance (VBA)](Set_Dimensions_to_Mid-Tolerance_Example_VB.htm)
[Add Derived Configurations (VBA)](Add_Derived_Configurations_Example_VB.htm)

## Remarks

The Options argument can be a combination of any of the following values:

- swConfigOption_SuppressByDefault - True if you want to suppress newly added features and mates in this configuration, false if not
- swConfigOption_HideByDefault - True if you want newly added components to be hidden, false if not
- swConfigOption_MinFeatureManager - True if you want newly added components to only display their component name in the FeatureManager design tree, false if you want newly added components to display their name and each of their features in the FeatureManager design tree

## See Also

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html)
[IAssembly::AddComponentConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponentConfiguration.html)
[IComponent2::Name2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Name2.html)
[IConfiguration::AlternateName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AlternateName.html)
[IConfiguration::GetParent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParent.html)
[IConfiguration::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetChildren.html)
[IConfiguration::IGetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetChildren.html)
[IConfiguration::Name Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Name.html)
[IConfigurationManager::ActiveConfiguration Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.html)
[IModelDoc2::AddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddConfiguration3.html)

## Availability

SOLIDWORKS 2003 SP1, Revision Number 11.1
