---
title: "OppositeHandComponents Property (IMirrorComponentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorComponentFeatureData"
member: "OppositeHandComponents"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~OppositeHandComponents.html"
---

# OppositeHandComponents Property (IMirrorComponentFeatureData)

Gets or sets the array of components for which to create opposite-hand versions.

## Syntax

### Visual Basic (Declaration)

```vb
Property OppositeHandComponents As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorComponentFeatureData
Dim value As System.Object

instance.OppositeHandComponents = value

value = instance.OppositeHandComponents
```

### C#

```csharp
System.object OppositeHandComponents {get; set;}
```

### C++/CLI

```cpp
property System.Object^ OppositeHandComponents {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [MirrorComponentFeatureData::OppositeHandComponents](ms-its:sldworksapivb6.chm::/sldworks~MirrorComponentFeatureData~OppositeHandComponents.html).

## Examples

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html) example.

## Remarks

Use [IMirrorComponentFeatureData::ComponentsToInstanceAlignToComponentOrigin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentsToInstanceAlignToComponentOrigin.html) or [IMirrorComponentFeatureData::ComponentsToInstanceAlignToSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentsToInstanceAlignToSelection.html) to create non-opposite-hand versions of selected components.

## See Also

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html)
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.html)
[IMirrorComponentFeatureData::CreateDerivedConfigurations Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~CreateDerivedConfigurations.html)
[IMirrorComponentFeatureData::ReplaceFileLocations Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ReplaceFileLocations.html)
[IMirrorComponentFeatureData::NameModifier Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~NameModifier.html)
[IMirrorComponentFeatureData::NameModifierType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~NameModifierType.html)
[IMirrorComponentFeatureData::MirroredComponentFilenames Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirroredComponentFilenames.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
