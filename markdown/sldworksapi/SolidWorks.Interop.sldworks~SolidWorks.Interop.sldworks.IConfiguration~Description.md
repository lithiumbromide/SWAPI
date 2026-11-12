---
title: "Description Property (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "Description"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Description.html"
---

# Description Property (IConfiguration)

Gets or sets the description of the configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Property Description As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.String

instance.Description = value

value = instance.Description
```

### C#

```csharp
System.string Description {get; set;}
```

### C++/CLI

```cpp
property System.String^ Description {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Description of the configuration

## VBA Syntax

See [Configuration::Description](ms-its:sldworksapivb6.chm::/sldworks~Configuration~Description.html).

## Examples

[Change Configuration Properties (VBA)](Change_Configuration_Properties_Example_VB.htm)
[Traverse Hierarchy of Configurations (VBA)](Traverse_Hierarchy_of_Configurations_Example_VB.htm)
[Display Configuration Description in Bill of Materials (C#)](Display_Configuration_Description_in_Bill_of_Materials_Example_CSharp.htm)
[Display Configuration Description in Bill of Materials (VB.NET)](Display_Configuration_Description_in_Bill_of_Materials_Example_VBNET.htm)
[Display Configuration Description in Bill of Materials (VBA)](Display_Configuration_Description_in_Bill_of_Materials_Example_VB.htm)

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::UseDescriptionInBOM Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~UseDescriptionInBOM.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
