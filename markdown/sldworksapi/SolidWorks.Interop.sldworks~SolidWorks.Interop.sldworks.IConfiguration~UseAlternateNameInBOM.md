---
title: "UseAlternateNameInBOM Property (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "UseAlternateNameInBOM"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~UseAlternateNameInBOM.html"
---

# UseAlternateNameInBOM Property (IConfiguration)

Gets or sets whether the [alternate name](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~AlternateName.html) (i.e., user-specified name) is displayed in the bill of materials for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseAlternateNameInBOM As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Boolean

instance.UseAlternateNameInBOM = value

value = instance.UseAlternateNameInBOM
```

### C#

```csharp
System.bool UseAlternateNameInBOM {get; set;}
```

### C++/CLI

```cpp
property System.bool UseAlternateNameInBOM {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True displays the alternate name in the bill of materials, false does not

## VBA Syntax

See [Configuration::UseAlternateNameInBOM](ms-its:sldworksapivb6.chm::/sldworks~Configuration~UseAlternateNameInBOM.html).

## Examples

[Change Configuration Properties (VBA)](Change_Configuration_Properties_Example_VB.htm)
[Traverse Hierarchy of Configurations (VBA)](Traverse_Hierarchy_of_Configurations_Example_VB.htm)
[Get List of Configurations (C#)](Get_List_Of_Configurations_Example_CSharp.htm)
[Get List of Configurations (VB.NET)](Get_List_Of_Configurations_Example_VBNET.htm)
[Get List of Configurations (VBA)](Get_List_Of_Configurations_Example_VB.htm)

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
