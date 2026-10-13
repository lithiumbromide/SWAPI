---
title: "AddRebuildSaveMark Property (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "AddRebuildSaveMark"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRebuildSaveMark.html"
---

# AddRebuildSaveMark Property (IConfiguration)

Adds or removes the mark indicating whether the configuration needs to be rebuilt and its configuration data saved every time you save the model document.

## Syntax

### Visual Basic (Declaration)

```vb
Property AddRebuildSaveMark As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Boolean

instance.AddRebuildSaveMark = value

value = instance.AddRebuildSaveMark
```

### C#

```csharp
System.bool AddRebuildSaveMark {get; set;}
```

### C++/CLI

```cpp
property System.bool AddRebuildSaveMark {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to mark the configuration as needing to be rebuilt and its configuration data saved every time you save the model document, false to mark the configuration as not needing to be rebuilt and its configuration data not saved every time you save the model document

## VBA Syntax

See [Configuration::AddRebuildSaveMark](ms-its:sldworksapivb6.chm::/sldworks~Configuration~AddRebuildSaveMark.html).

## Examples

[Save Configuration Data (C#)](Save_Configuration_Data_Example_CSharp.htm)
[Save Configuration Data (VB.NET)](Save_Configuration_Data_Example_VBNET.htm)
[Save Configuration Data (VBA)](Save_Configuration_Data_Example_VB.htm)

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::NeedsRebuild Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~NeedsRebuild.html)
[IModelDoc2::EditRebuild3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.html)
[IModelDoc2::ForceRebuild3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.html)
[IModelDocExtension::NeedsRebuild2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.html)
[IModelDocExtension::EditRebuildAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~EditRebuildAll.html)
[IModelDocExtension::ForceRebuildAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ForceRebuildAll.html)
[IConfigurationManager::AddRebuildSaveMark Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddRebuildSaveMark.html)
[IConfigurationManager::RemoveMarkForAllConfigurations Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~RemoveMarkForAllConfigurations.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
