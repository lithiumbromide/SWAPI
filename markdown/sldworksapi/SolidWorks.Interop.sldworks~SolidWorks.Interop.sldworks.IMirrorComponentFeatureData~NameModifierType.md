---
title: "NameModifierType Property (IMirrorComponentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorComponentFeatureData"
member: "NameModifierType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~NameModifierType.html"
---

# NameModifierType Property (IMirrorComponentFeatureData)

Gets or sets the type of modifier to apply to the opposite-hand version file name.

## Syntax

### Visual Basic (Declaration)

```vb
Property NameModifierType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorComponentFeatureData
Dim value As System.Integer

instance.NameModifierType = value

value = instance.NameModifierType
```

### C#

```csharp
System.int NameModifierType {get; set;}
```

### C++/CLI

```cpp
property System.int NameModifierType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of file name modifier as defined in [swMirrorComponentNameModifier_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMirrorComponentNameModifier_e.html)

## VBA Syntax

See [MirrorComponentFeatureData::NameModifierType](ms-its:sldworksapivb6.chm::/sldworks~MirrorComponentFeatureData~NameModifierType.html).

## Examples

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html) example.

## Remarks

This property is valid only if:

- [IMirrorComponentFeatureData::OppositeHandComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~OppositeHandComponents.html) is not Nothing or null,

- and -

- [IMirrorComponentFeatureData::MirroredComponentFilenames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirroredComponentFilenames.html) is not Nothing or null.

If this property is not set, then it defaults to swMirrorComponentNameModifier_e.swMirrorComponentName_Prefix.

## See Also

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html)
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.html)
[IMirrorComponentFeatureData::NameModifier Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~NameModifier.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
