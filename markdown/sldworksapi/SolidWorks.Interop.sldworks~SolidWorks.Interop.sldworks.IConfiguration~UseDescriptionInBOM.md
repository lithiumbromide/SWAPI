---
title: "UseDescriptionInBOM Property (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "UseDescriptionInBOM"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~UseDescriptionInBOM.html"
---

# UseDescriptionInBOM Property (IConfiguration)

Gets or sets whether the [description](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~Description.html) of the configuration is displayed in the bill of materials.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseDescriptionInBOM As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Boolean

instance.UseDescriptionInBOM = value

value = instance.UseDescriptionInBOM
```

### C#

```csharp
System.bool UseDescriptionInBOM {get; set;}
```

### C++/CLI

```cpp
property System.bool UseDescriptionInBOM {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True displays the description of the configuration in the bill of materials, false does not

## VBA Syntax

See [Configuration::UseDescriptionInBOM](ms-its:sldworksapivb6.chm::/sldworks~Configuration~UseDescriptionInBOM.html).

## Examples

[Display Configuration Description in Bill of Materials (C#)](Display_Configuration_Description_in_Bill_of_Materials_Example_CSharp.htm)
[Display Configuration Description in Bill of Materials (VB.NET)](Display_Configuration_Description_in_Bill_of_Materials_Example_VBNET.htm)
[Display Configuration Description in Bill of Materials (VBA)](Display_Configuration_Description_in_Bill_of_Materials_Example_VB.htm)

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
