---
title: "SuppressNewComponentModels Property (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "SuppressNewComponentModels"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SuppressNewComponentModels.html"
---

# SuppressNewComponentModels Property (IConfiguration)

Gets or sets whether new components are suppressed in this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Property SuppressNewComponentModels As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Boolean

instance.SuppressNewComponentModels = value

value = instance.SuppressNewComponentModels
```

### C#

```csharp
System.bool SuppressNewComponentModels {get; set;}
```

### C++/CLI

```cpp
property System.bool SuppressNewComponentModels {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True suppresses the new component in this configuration, false resolves it

## VBA Syntax

See [Configuration::SuppressNewComponentModels](ms-its:sldworksapivb6.chm::/sldworks~Configuration~SuppressNewComponentModels.html).

## Examples

[Change Configuration Properties (VBA)](Change_Configuration_Properties_Example_VB.htm)
[Traverse Hierarchy of Configurations (VBA)](Traverse_Hierarchy_of_Configurations_Example_VB.htm)

## Remarks

This setting applies only to inactive configurations.

This property applies only to assembly configurations. SOLIDWORKS always returns false when you get this property on a part configuration. Setting this property on a part configuration has no effect.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::HideNewComponentModels Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~HideNewComponentModels.html)
[IConfiguration::GetComponentSuppressionState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetComponentSuppressionState.html)

## Availability

SOLIDWORKS 99, datecode 1999207
