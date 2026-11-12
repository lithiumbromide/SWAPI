---
title: "HideNewComponentModels Property (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "HideNewComponentModels"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~HideNewComponentModels.html"
---

# HideNewComponentModels Property (IConfiguration)

Gets or sets whether new components are hidden in this inactive configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Property HideNewComponentModels As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Boolean

instance.HideNewComponentModels = value

value = instance.HideNewComponentModels
```

### C#

```csharp
System.bool HideNewComponentModels {get; set;}
```

### C++/CLI

```cpp
property System.bool HideNewComponentModels {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True hides new components, false create new components as shown in this configuration

## VBA Syntax

See [Configuration::HideNewComponentModels](ms-its:sldworksapivb6.chm::/sldworks~Configuration~HideNewComponentModels.html).

## Examples

[Change Configuration Properties (VBA)](Change_Configuration_Properties_Example_VB.htm)
[Traverse Hierarchy of Configurations (VBA)](Traverse_Hierarchy_of_Configurations_Example_VB.htm)

## Remarks

This setting is only valid when the configuration is not the active configuration.

This property applies only to assembly configurations. SOLIDWORKS always returns false when you get this property on a part configuration. This property has no effect on part configurations.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[SuppressNewComponentModels Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SuppressNewComponentModels.html)

## Availability

SOLIDWORKS 99, datecode 1999207
