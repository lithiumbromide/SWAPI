---
title: "CreateDerivedConfigurations Property (IMirrorComponentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorComponentFeatureData"
member: "CreateDerivedConfigurations"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~CreateDerivedConfigurations.html"
---

# CreateDerivedConfigurations Property (IMirrorComponentFeatureData)

Gets or sets whether to create a derived configuration of the opposite-hand components in the original assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Property CreateDerivedConfigurations As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorComponentFeatureData
Dim value As System.Boolean

instance.CreateDerivedConfigurations = value

value = instance.CreateDerivedConfigurations
```

### C#

```csharp
System.bool CreateDerivedConfigurations {get; set;}
```

### C++/CLI

```cpp
property System.bool CreateDerivedConfigurations {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to create a derived configuration of the opposite-hand components in the original assembly, false (default) to create new part files

## VBA Syntax

See [MirrorComponentFeatureData::CreateDerivedConfigurations](ms-its:sldworksapivb6.chm::/sldworks~MirrorComponentFeatureData~CreateDerivedConfigurations.html).

## Examples

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html) example.

## Remarks

This property is valid only:

- If [IMirrorComponentFeatureData::OppositeHandComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~OppositeHandComponents.html) is not Nothing or null.
- At creation time. You cannot edit this property after it is set.

| If this property is... | And IMirrorComponentFeatureData::NameModifierType is... | Then use... |
| --- | --- | --- |
| True | swMirrorComponentName_Prefix - or - swMirrorComponentName_Suffix | IMirrorComponentFeatureData::NameModifier to prepend a prefix or append a suffix to the configuration name of the original component to create a derived configuration name for the new opposite-hand versions. |
| True | swMirrorComponentName_Custom | IMirrorComponentFeatureData::MirroredComponentFilenames to specify the derived configuration name. |
| False | swMirrorComponentName_Prefix - or - swMirrorComponentName_Suffix | IMirrorComponentFeatureData::NameModifier to prepend a prefix or append a suffix to the orginal component file name to create a new opposite-hand version file name. |
| False | swMirrorComponentName_Custom | IMirrorComponentFeatureData::MirroredComponentFilenames to specify the opposite-hand version file names. |

If you set this property to false, you can also specify the following import features:

- [IMirrorComponentFeatureData::BreakLinksToOriginalPart](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~BreakLinksToOriginalPart.html) (if set to false, you can also set [IMirrorComponentFeatureData::DimXpertScheme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~DimXpertScheme.html) and/or [IMirrorComponentFeatureData::MirrorTransferOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirrorTransferOptions.html))
- [IMirrorComponentFeatureData::PreserveZAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~PreserveZAxis.html)
- [IMirrorComponentFeatureData::PropagateFromOriginalPart](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~PropagateFromOriginalPart.html)

## See Also

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html)
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
