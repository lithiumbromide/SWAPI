---
title: "ShowConfigurationDescriptions Property (IConfigurationManager)"
project: "SOLIDWORKS API Help"
interface: "IConfigurationManager"
member: "ShowConfigurationDescriptions"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ShowConfigurationDescriptions.html"
---

# ShowConfigurationDescriptions Property (IConfigurationManager)

Gets or sets whether to display configuration descriptions in ConfigurationManager.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowConfigurationDescriptions As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfigurationManager
Dim value As System.Boolean

instance.ShowConfigurationDescriptions = value

value = instance.ShowConfigurationDescriptions
```

### C#

```csharp
System.bool ShowConfigurationDescriptions {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowConfigurationDescriptions {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display configuration descriptions, false to not

## VBA Syntax

See [ConfigurationManager::ShowConfigurationDescriptions](ms-its:sldworksapivb6.chm::/sldworks~ConfigurationManager~ShowConfigurationDescriptions.html).

## Examples

[Work With Configurations (VBA)](Work_with_Configurations_Example_VB.htm)

## Remarks

If you set this property to false, you cannot set [IConfigurationManager::ShowConfigurationNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ShowConfigurationNames.html) to false. Either the name or the description of a configuration must be shown.

## See Also

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
