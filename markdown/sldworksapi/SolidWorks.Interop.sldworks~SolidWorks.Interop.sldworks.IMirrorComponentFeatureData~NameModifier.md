---
title: "NameModifier Property (IMirrorComponentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorComponentFeatureData"
member: "NameModifier"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~NameModifier.html"
---

# NameModifier Property (IMirrorComponentFeatureData)

Gets or sets the prefix or suffix to add to the file or configuration names of the components to be mirrored.

## Syntax

### Visual Basic (Declaration)

```vb
Property NameModifier As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorComponentFeatureData
Dim value As System.String

instance.NameModifier = value

value = instance.NameModifier
```

### C#

```csharp
System.string NameModifier {get; set;}
```

### C++/CLI

```cpp
property System.String^ NameModifier {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Prefix or suffix text; "Mirror" by default

## VBA Syntax

See [MirrorComponentFeatureData::NameModifier](ms-its:sldworksapivb6.chm::/sldworks~MirrorComponentFeatureData~NameModifier.html).

## Examples

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html) example.

## Remarks

This property is valid only if:

- [IMirrorComponentFeatureData::NameModifierType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~NameModifierType.html) is either [swMirrorComponentNameModifier_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMirrorComponentNameModifier_e.html).swMirrorComponentName_Prefix or swMirrorComponentNameModifier_e.swMirrorComponentNameName_Suffix,

- and -

- [IMirrorComponentFeatureData::OppositeHandComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~OppositeHandComponents.html) is not Nothing or null,

- and -

- [IMirrorComponentFeatureData::MirroredComponentFilenames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirroredComponentFilenames.html) is not Nothing or null.

If [IMirrorComponentFeatureData::CreateDerivedConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~CreateDerivedConfigurations.html) is:

- True, then this property prepends a prefix or appends a suffix to the configuration name of the original component to create new opposite-hand version configuration names.
- False, then this property prepends a prefix or appends a suffix to the orginal component file name to create new opposite-hand version file names.

## See Also

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html)
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
