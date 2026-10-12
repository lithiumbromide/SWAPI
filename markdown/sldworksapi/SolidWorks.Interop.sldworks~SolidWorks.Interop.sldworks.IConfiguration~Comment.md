---
title: "Comment Property (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "Comment"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Comment.html"
---

# Comment Property (IConfiguration)

Gets or sets the configuration comment.

## Syntax

### Visual Basic (Declaration)

```vb
Property Comment As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.String

instance.Comment = value

value = instance.Comment
```

### C#

```csharp
System.string Comment {get; set;}
```

### C++/CLI

```cpp
property System.String^ Comment {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Comment for the configuration

## VBA Syntax

See [Configuration::Comment](ms-its:sldworksapivb6.chm::/sldworks~Configuration~Comment.html).

## Examples

[Change Configuration Properties (VBA)](Change_Configuration_Properties_Example_VB.htm)
[Traverse Hierarchy of Configurations (VBA)](Traverse_Hierarchy_of_Configurations_Example_VB.htm)
[Get List of Configurations (C#)](Get_List_Of_Configurations_Example_CSharp.htm)
[Get List of Configurations (VB.NET)](Get_List_Of_Configurations_Example_VBNET.htm)
[Get List of Configurations (VBA)](Get_List_Of_Configurations_Example_VB.htm)

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
