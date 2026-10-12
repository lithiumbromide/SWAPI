---
title: "AddRebuildSaveMark Method (IConfigurationManager)"
project: "SOLIDWORKS API Help"
interface: "IConfigurationManager"
member: "AddRebuildSaveMark"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddRebuildSaveMark.html"
---

# AddRebuildSaveMark Method (IConfigurationManager)

Adds marks indicating whether the specified configurations need to be rebuilt and their configuration data saved every time the model document is saved.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddRebuildSaveMark( _
   ByVal WhichConfigurations As System.Integer, _
   ByVal ConfigNames As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfigurationManager
Dim WhichConfigurations As System.Integer
Dim ConfigNames As System.Object
Dim value As System.Boolean

value = instance.AddRebuildSaveMark(WhichConfigurations, ConfigNames)
```

### C#

```csharp
System.bool AddRebuildSaveMark(
   System.int WhichConfigurations,
   System.object ConfigNames
)
```

### C++/CLI

```cpp
System.bool AddRebuildSaveMark(
   System.int WhichConfigurations,
   System.Object^ ConfigNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichConfigurations`: One of the following options in [swInConfigurationOpts_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInConfigurationOpts_e.html):

  - swAllConfiguration
  - swSpecifyConfiguration
  - swThisConfiguration
  - swSpeedpakConfiguration
- `ConfigNames`: Array of configuration names to which to apply the mark; valid only if WhichConfigurations is set to swInConfigurationOpts_e.swSpecifyConfiguration

### Return Value

True if configurations marked successfully, false if not

## VBA Syntax

See [ConfigurationManager::AddRebuildSaveMark](ms-its:sldworksapivb6.chm::/sldworks~ConfigurationManager~AddRebuildSaveMark.html).

## Examples

[Work With Configurations (VBA)](Work_with_Configurations_Example_VB.htm)

## See Also

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html)
[IConfiguration::NeedsRebuild Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~NeedsRebuild.html)
[IModelDoc2::EditRebuild3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.html)
[IModelDocExtension::EditRebuildAll Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~EditRebuildAll.html)
[IModelDocExtension::ForceRebuildAll Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ForceRebuildAll.html)
[IConfiguration::AddRebuildSaveMark Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRebuildSaveMark.html)
[IConfigurationManager::RemoveMarkForAllConfigurations Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~RemoveMarkForAllConfigurations.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
