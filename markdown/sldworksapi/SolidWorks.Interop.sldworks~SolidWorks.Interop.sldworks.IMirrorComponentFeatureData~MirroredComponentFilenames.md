---
title: "MirroredComponentFilenames Property (IMirrorComponentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorComponentFeatureData"
member: "MirroredComponentFilenames"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirroredComponentFilenames.html"
---

# MirroredComponentFilenames Property (IMirrorComponentFeatureData)

Gets or sets the file names of the opposite-hand component versions.

## Syntax

### Visual Basic (Declaration)

```vb
Property MirroredComponentFilenames As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorComponentFeatureData
Dim value As System.Object

instance.MirroredComponentFilenames = value

value = instance.MirroredComponentFilenames
```

### C#

```csharp
System.object MirroredComponentFilenames {get; set;}
```

### C++/CLI

```cpp
property System.Object^ MirroredComponentFilenames {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of file names

## VBA Syntax

See [MirrorComponentFeatureData::MirroredComponentFilenames](ms-its:sldworksapivb6.chm::/sldworks~MirrorComponentFeatureData~MirroredComponentFilenames.html).

## Examples

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html) example.

## Remarks

This property is valid only if:

- [IMirrorComponentFeatureData::NameModifierType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~NameModifierType.html) is set to [swMirrorComponentNameModifier_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMirrorComponentNameModifier_e.html).swMirrorComponentName_Custom,

- and -

- [IMirrorComponentFeatureData::OppositeHandComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~OppositeHandComponents.html) is not Nothing or null.

If [IMirrorComponentFeatureData::CreateDerivedConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~CreateDerivedConfigurations.html) is:

- True, then use this property to specify the configuration names to be added to the opposite-hand versions.
- False, then use this property to specify file names to use to create the opposite-hand versions.

## See Also

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html)
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
