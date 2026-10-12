---
title: "AddConfiguration2 Method (IConfigurationManager)"
project: "SOLIDWORKS API Help"
interface: "IConfigurationManager"
member: "AddConfiguration2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddConfiguration2.html"
---

# AddConfiguration2 Method (IConfigurationManager)

Creates a new configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddConfiguration2( _
   ByVal Name As System.String, _
   ByVal Comment As System.String, _
   ByVal AlternateName As System.String, _
   ByVal Options As System.Integer, _
   ByVal ParentConfigName As System.String, _
   ByVal Description As System.String, _
   ByVal Rebuild As System.Boolean _
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
Dim Rebuild As System.Boolean
Dim value As Configuration

value = instance.AddConfiguration2(Name, Comment, AlternateName, Options, ParentConfigName, Description, Rebuild)
```

### C#

```csharp
Configuration AddConfiguration2(
   System.string Name,
   System.string Comment,
   System.string AlternateName,
   System.int Options,
   System.string ParentConfigName,
   System.string Description,
   System.bool Rebuild
)
```

### C++/CLI

```cpp
Configuration^ AddConfiguration2(
   System.String^ Name,
   System.String^ Comment,
   System.String^ AlternateName,
   System.int Options,
   System.String^ ParentConfigName,
   System.String^ Description,
   System.bool Rebuild
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of the configuration
- `Comment`: Comment displayed in Configuration Properties
- `AlternateName`: Alternate configuration name (i.e., user-specified name); used if Options is set to swConfigurationOptions2_e_UseAlternateName
- `Options`: Combination of one or more configuration options as defined in [swConfigurationOptions2_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConfigurationOptions2_e.html) (see **Remarks**)
- `ParentConfigName`: Name of parent configuration
- `Description`: Text that identifies the configuration
- `Rebuild`: True to rebuild the model after adding this configuration, false to not

### Return Value

Newly created [configuration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration.html)

## VBA Syntax

See [ConfigurationManager::AddConfiguration2](ms-its:sldworksapivb6.chm::/sldworks~ConfigurationManager~AddConfiguration2.html).

## Examples

[Work with Configurations (VBA)](Work_with_Configurations_Example_VB.htm)

## Remarks

The Options argument can be a combination of any of the following values:

- swConfigOption_SuppressByDefault
- swConfigOption_HideByDefault
- swConfigOption_MinFeatureManager
- swConfigOption_UseAlternateName

## See Also

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html)
[IAssemblyDoc::AddComponentConfiguration Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponentConfiguration.html)
[IModelDoc2::AddConfiguration3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddConfiguration3.html)
[IConfiguration::GetChildren Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetChildren.html)
[IConfiguration::GetParent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParent.html)
[IConfiguration::Name Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Name.html)
[IConfigurationManager::ActiveConfiguration Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
