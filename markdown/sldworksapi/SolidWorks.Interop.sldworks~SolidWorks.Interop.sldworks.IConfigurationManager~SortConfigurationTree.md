---
title: "SortConfigurationTree Method (IConfigurationManager)"
project: "SOLIDWORKS API Help"
interface: "IConfigurationManager"
member: "SortConfigurationTree"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SortConfigurationTree.html"
---

# SortConfigurationTree Method (IConfigurationManager)

Specifies the order in which to list configurations in the ConfigurationManager.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SortConfigurationTree( _
   ByVal InSelType As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IConfigurationManager
Dim InSelType As System.Integer

instance.SortConfigurationTree(InSelType)
```

### C#

```csharp
void SortConfigurationTree(
   System.int InSelType
)
```

### C++/CLI

```cpp
void SortConfigurationTree(
   System.int InSelType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InSelType`: Order in which to list configurations in the ConfigurationManager as defined in [swConfigTreeSortType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConfigTreeSortType_e.html)

## VBA Syntax

See [ConfigurationManager::SortConfigurationTree](ms-its:sldworksapivb6.chm::/sldworks~ConfigurationManager~SortConfigurationTree.html).

## Examples

[Specify Order of Configurations (C#)](Specify_Order_of_Configurations_Example_CSharp.htm)
[Specify Order of Configurations (VB.NET)](Specify_Order_of_Configurations_Example_VBNET.htm)
[Specify Order of Configurations (VBA)](Specify_Order_of_Configurations_Example_VB.htm)

## See Also

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
