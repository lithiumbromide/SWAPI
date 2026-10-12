---
title: "EnableConfigurationTree Property (IConfigurationManager)"
project: "SOLIDWORKS API Help"
interface: "IConfigurationManager"
member: "EnableConfigurationTree"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~EnableConfigurationTree.html"
---

# EnableConfigurationTree Property (IConfigurationManager)

Gets or sets whether to update the ConfigurationManager tree.

## Syntax

### Visual Basic (Declaration)

```vb
Property EnableConfigurationTree As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfigurationManager
Dim value As System.Boolean

instance.EnableConfigurationTree = value

value = instance.EnableConfigurationTree
```

### C#

```csharp
System.bool EnableConfigurationTree {get; set;}
```

### C++/CLI

```cpp
property System.bool EnableConfigurationTree {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to update the ConfigurationManager tree, false to not (see Remarks)

## VBA Syntax

See [ConfigurationManager::EnableConfigurationTree](ms-its:sldworksapivb6.chm::/sldworks~ConfigurationManager~EnableConfigurationTree.html).

## Remarks

This property is set to true by default. Setting this property to false will increase the performance of SOLIDWORKS when performing multiple operations that affect the ConfigurationManager tree, such as deleting configurations. However, set this property back to true after performing such operations so that the ConfigurationManager tree will update thereafter.

## See Also

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html)

## Availability

SOLIDWORKSs 2007 SP4, Revision Number 15.4
