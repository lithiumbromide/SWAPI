---
title: "ComponentsToInstanceAlignToSelection Property (IMirrorComponentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorComponentFeatureData"
member: "ComponentsToInstanceAlignToSelection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentsToInstanceAlignToSelection.html"
---

# ComponentsToInstanceAlignToSelection Property (IMirrorComponentFeatureData)

Gets or sets the array of components whose orientation axes align to selected references.

## Syntax

### Visual Basic (Declaration)

```vb
Property ComponentsToInstanceAlignToSelection As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorComponentFeatureData
Dim value As System.Object

instance.ComponentsToInstanceAlignToSelection = value

value = instance.ComponentsToInstanceAlignToSelection
```

### C#

```csharp
System.object ComponentsToInstanceAlignToSelection {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ComponentsToInstanceAlignToSelection {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [MirrorComponentFeatureData::ComponentsToInstanceAlignToSelection](ms-its:sldworksapivb6.chm::/sldworks~MirrorComponentFeatureData~ComponentsToInstanceAlignToSelection.html).

## Examples

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html) example.

## Remarks

This property is valid only for components for which you are `not` creating opposite-hand versions. Use [IMirrorComponentFeatureData::OppositeHandComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~OppositeHandComponents.html) to specify components for which you are creating opposite-hand versions.

Use [IMirrorComponentFeatureData::ComponentOrientationsAlignToSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentOrientationsAlignToSelection.html) to specify the orientation of each component in this property's array. There is a one-to-one mapping between this property's array and IMirrorComponentFeatureData::ComponentOrientationsAlignToSelection.

Use [IMirrorComponentFeatureData::AlignmentReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~AlignmentReferences.html) to specify alignment references. There is a one-to-one mapping between this property's array and IMirrorComponentFeatureData::AlignmentReferences. If this property's array contains more elements than IMirrorComponentFeatureData::AlignmentReferences, then the feature will fail to be created.

## See Also

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html)
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
