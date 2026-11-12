---
title: "ShowConfigurationNames Property (IConfigurationManager)"
project: "SOLIDWORKS API Help"
interface: "IConfigurationManager"
member: "ShowConfigurationNames"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ShowConfigurationNames.html"
---

# ShowConfigurationNames Property (IConfigurationManager)

Gets or sets whether to display configuration names in ConfigurationManager.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowConfigurationNames As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfigurationManager
Dim value As System.Boolean

instance.ShowConfigurationNames = value

value = instance.ShowConfigurationNames
```

### C#

```csharp
System.bool ShowConfigurationNames {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowConfigurationNames {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display configuration names, false to not

## VBA Syntax

See [ConfigurationManager::ShowConfigurationNames](ms-its:sldworksapivb6.chm::/sldworks~ConfigurationManager~ShowConfigurationNames.html).

## Examples

[Work With Configurations (VBA)](Work_with_Configurations_Example_VB.htm)

## Remarks

If you set this property to false, you cannot set [IConfigurationManager::ShowConfigurationDescriptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ShowConfigurationDescriptions.html) to false. Either the name or the description of a configuration must be shown.

## See Also

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
