---
title: "ChildComponentDisplayInBOM Property (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "ChildComponentDisplayInBOM"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ChildComponentDisplayInBOM.html"
---

# ChildComponentDisplayInBOM Property (IConfiguration)

Gets or sets the child component display option of this configuration in the Bill of Materials (BOM) for an assembly or for a cutlist part (weldment and/or sheet metal).

## Syntax

### Visual Basic (Declaration)

```vb
Property ChildComponentDisplayInBOM As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Integer

instance.ChildComponentDisplayInBOM = value

value = instance.ChildComponentDisplayInBOM
```

### C#

```csharp
System.int ChildComponentDisplayInBOM {get; set;}
```

### C++/CLI

```cpp
property System.int ChildComponentDisplayInBOM {
   System.int get();
   void set (    System.int value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Child component display option as defined in

[swChildComponentInBOMOption_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swChildComponentInBOMOption_e.html)

## VBA Syntax

See

[Configuration::ChildComponentDisplayInBOM](ms-its:sldworksapivb6.chm::/sldworks~Configuration~ChildComponentDisplayInBOM.html)

.

## Examples

[Add Configuration and Promote Child Components in BOM (C#)](Add_Configuration_and_Promote_Child_Components_in_BOM_Example_CSharp.htm)

[Add Configuration and Promote Child Components in BOM (VB.NET)](Add_Configuration_and_Promote_Child_Components_in_BOM_Example_VBNET.htm)

[Add Configuration and Promote Child Components in BOM (VBA)](Add_Configuration_and_Promote_Child_Components_in_BOM_Example_VB.htm)

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)

[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)

[IModelDoc2::AddConfiguration3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddConfiguration3.html)

## Availability

SolidWorks 2013 SP3, Revision Number 22.3
