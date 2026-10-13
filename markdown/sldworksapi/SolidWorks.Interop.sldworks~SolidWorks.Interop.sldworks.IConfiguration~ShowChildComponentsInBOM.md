---
title: "ShowChildComponentsInBOM Property (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "ShowChildComponentsInBOM"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ShowChildComponentsInBOM.html"
---

# ShowChildComponentsInBOM Property (IConfiguration)

Obsolete. Superseded by [IConfiguration::ChildComponentDisplayInBOM.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ChildComponentDisplayInBOM.html)

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowChildComponentsInBOM As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Boolean

instance.ShowChildComponentsInBOM = value

value = instance.ShowChildComponentsInBOM
```

### C#

```csharp
System.bool ShowChildComponentsInBOM {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowChildComponentsInBOM {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True displays child components in a BOM, false does not

## VBA Syntax

See [Configuration::ShowChildComponentsInBOM](ms-its:sldworksapivb6.chm::/sldworks~Configuration~ShowChildComponentsInBOM.html).

## Examples

[Change Configuration Properties (VBA)](Change_Configuration_Properties_Example_VB.htm)
[Traverse Hierarchy of Configurations (VBA)](Traverse_Hierarchy_of_Configurations_Example_VB.htm)

## Remarks

This property applies only to assembly configurations. SOLIDWORKS always returns false when you get this property on a part configuration. Setting this property on a part configuration has no effect.

How the components appear in the report is mainly controlled by the display format of a BOM. However, this property does affect the output format. Specifically, if this property is set to false, the report includes only the subassembly, not the component parts of this model configuration (even if the BOM report requests that all parts be displayed).

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)

## Availability

SOLIDWORKS 2000 SP01, Revision Number 8.1
