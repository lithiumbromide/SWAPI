---
title: "ComponentsToInstanceAlignToComponentOrigin Property (IMirrorComponentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorComponentFeatureData"
member: "ComponentsToInstanceAlignToComponentOrigin"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentsToInstanceAlignToComponentOrigin.html"
---

# ComponentsToInstanceAlignToComponentOrigin Property (IMirrorComponentFeatureData)

Gets or sets the array of components whose orientation axes align to origins.

## Syntax

### Visual Basic (Declaration)

```vb
Property ComponentsToInstanceAlignToComponentOrigin As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorComponentFeatureData
Dim value As System.Object

instance.ComponentsToInstanceAlignToComponentOrigin = value

value = instance.ComponentsToInstanceAlignToComponentOrigin
```

### C#

```csharp
System.object ComponentsToInstanceAlignToComponentOrigin {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ComponentsToInstanceAlignToComponentOrigin {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [MirrorComponentFeatureData::ComponentsToInstanceAlignToComponentOrigin](ms-its:sldworksapivb6.chm::/sldworks~MirrorComponentFeatureData~ComponentsToInstanceAlignToComponentOrigin.html).

## Examples

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html) example.

## Remarks

This property is valid only for components for which you are `not` creating opposite-hand versions. Use [IMirrorComponentFeatureData::OppositeHandComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~OppositeHandComponents.html) to specify components for which you are creating opposite-hand versions.

Use [IMirrorComponentFeatureData::ComponentOrientationsAlignToComponentOrigin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentOrientationsAlignToComponentOrigin.html) to specify the orientation of each component in this array.

## See Also

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html)
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
