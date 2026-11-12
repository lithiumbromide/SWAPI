---
title: "Object Property (ITreeControlItem)"
project: "SOLIDWORKS API Help"
interface: "ITreeControlItem"
member: "Object"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem~Object.html"
---

# Object Property (ITreeControlItem)

Gets the SOLIDWORKS object associated with this item in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Object As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITreeControlItem
Dim value As System.Object

value = instance.Object
```

### C#

```csharp
System.object Object {get;}
```

### C++/CLI

```cpp
property System.Object^ Object {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

SOLIDWORKS object associated with this item in the FeatureManager design tree (see **Remarks**)

## VBA Syntax

See [TreeControlItem::Object](ms-its:sldworksapivb6.chm::/sldworks~TreeControlItem~Object.html).

## Examples

[Traverse FeatureManager Design Tree (VBA)](Traverse_FeatureManager_Design_Tree_VB.htm)
[Expand or Collapse FeatureManager Design Tree Nodes (VBA)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_VB.htm)
[Expand or Collapse FeatureManager Design Tree Nodes (VB.NET)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_Example_VBNET.htm)
[Expand or Collapse FeatureManager Design Tree Nodes (C#)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_Example_CSharp.htm)

## Remarks

Currently only [features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) and [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) are supported. Null is returned for sub-components of an assembly loaded hidden with a selective open.

Use [ITreeControlItem::ObjectType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITreeControlItem~ObjectType.html) to determine the SOLIDWORKS object type.

## See Also

[ITreeControlItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.html)
[ITreeControlItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem_members.html)

## Availability

SOLIDWORKS 2008 SP2, Revision Number 16.2
