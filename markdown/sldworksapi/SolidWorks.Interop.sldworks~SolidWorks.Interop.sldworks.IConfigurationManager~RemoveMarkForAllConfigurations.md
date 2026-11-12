---
title: "RemoveMarkForAllConfigurations Method (IConfigurationManager)"
project: "SOLIDWORKS API Help"
interface: "IConfigurationManager"
member: "RemoveMarkForAllConfigurations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~RemoveMarkForAllConfigurations.html"
---

# RemoveMarkForAllConfigurations Method (IConfigurationManager)

Remove all marks indicating whether configurations need to be rebuilt and their configuration data saved every time the model document is saved.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveMarkForAllConfigurations() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfigurationManager
Dim value As System.Boolean

value = instance.RemoveMarkForAllConfigurations()
```

### C#

```csharp
System.bool RemoveMarkForAllConfigurations()
```

### C++/CLI

```cpp
System.bool RemoveMarkForAllConfigurations();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if marks removed successfully, false if not

## VBA Syntax

See [ConfigurationManager::RemoveMarkForAllConfigurations](ms-its:sldworksapivb6.chm::/sldworks~ConfigurationManager~RemoveMarkForAllConfigurations.html).

## See Also

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html)
[IConfigurationManager::AddRebuildSaveMark Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddRebuildSaveMark.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
