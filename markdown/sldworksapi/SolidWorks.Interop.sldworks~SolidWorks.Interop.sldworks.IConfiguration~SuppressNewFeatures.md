---
title: "SuppressNewFeatures Property (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "SuppressNewFeatures"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SuppressNewFeatures.html"
---

# SuppressNewFeatures Property (IConfiguration)

Gets or sets whether to suppress new features in this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Property SuppressNewFeatures As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Boolean

instance.SuppressNewFeatures = value

value = instance.SuppressNewFeatures
```

### C#

```csharp
System.bool SuppressNewFeatures {get; set;}
```

### C++/CLI

```cpp
property System.bool SuppressNewFeatures {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True suppresses the new feature in this configuration, false does not

## VBA Syntax

See [Configuration::SuppressNewFeatures](ms-its:sldworksapivb6.chm::/sldworks~Configuration~SuppressNewFeatures.html).

## Examples

[Change Configuration Properties (VBA)](Change_Configuration_Properties_Example_VB.htm)
[Traverse Hierarchy of Configurations (VBA)](Traverse_Hierarchy_of_Configurations_Example_VB.htm)

## Remarks

This setting applies only to inactive configurations. This property applies to new mates and features for assembly configurations.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
