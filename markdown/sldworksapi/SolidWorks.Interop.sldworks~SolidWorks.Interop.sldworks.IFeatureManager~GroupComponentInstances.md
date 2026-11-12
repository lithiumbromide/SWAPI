---
title: "GroupComponentInstances Property (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "GroupComponentInstances"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GroupComponentInstances.html"
---

# GroupComponentInstances Property (IFeatureManager)

Gets or sets whether to group the same components in the same configuration in an assembly into a folder in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Property GroupComponentInstances As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Boolean

instance.GroupComponentInstances = value

value = instance.GroupComponentInstances
```

### C#

```csharp
System.bool GroupComponentInstances {get; set;}
```

### C++/CLI

```cpp
property System.bool GroupComponentInstances {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to group the same components in the same configuration in an assembly into a folder in the FeatureManager design tree, false to ungroup them

## VBA Syntax

See [FeatureManager::GroupComponentInstances](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~GroupComponentInstances.html).

## Examples

[Group and Ungroup Components (C#)](Group_Components_Example_CSharp.htm)
[Group and Ungroup Components (VB.NET)](Group_Components_Example_VBNET.htm)
[Group and Ungroup Components (VBA)](Group_Components_Example_VB.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IAssemblyDoc::UngroupComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UngroupComponents.html)
[IAssemblyDoc::ReorderComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorderComponents.html)
[IAssemblyDoc::ReorganizeComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorganizeComponents.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
