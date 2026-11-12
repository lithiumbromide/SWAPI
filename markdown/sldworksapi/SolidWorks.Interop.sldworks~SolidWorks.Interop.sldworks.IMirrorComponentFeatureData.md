---
title: "IMirrorComponentFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IMirrorComponentFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html"
---

# IMirrorComponentFeatureData Interface

Allows access to a mirror component feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IMirrorComponentFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorComponentFeatureData
```

### C#

```csharp
public interface IMirrorComponentFeatureData
```

### C++/CLI

```cpp
public interface class IMirrorComponentFeatureData
```

## VBA Syntax

See [MirrorComponentFeatureData](ms-its:sldworksapivb6.chm::/sldworks~MirrorComponentFeatureData.html).

## Examples

[Mirror Components II (VBA)](Mirror_Components_II_Example_VB.htm)
[Mirror Components II (VB.NET)](Mirror_Components_II_Example_VBNET.htm)
[Mirror Components II (C#)](Mirror_Components_II_Example_CSharp.htm)

## Remarks

Before calling [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html) to access this interface, you can pre-select the entities needed to create the mirror component feature:

| To specify... | Call IModelDocExtension::SelectByID2 using selection Mark... |
| --- | --- |
| Mirror plane | 1 |
| Components to mirror | 2 |
| Alignment references | 4 |

To create a basic Mirror Component feature, use at a minimum:

- [IMirrorComponentFeatureData::MirrorPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirrorPlane.html)
- [IMirrorComponentFeatureData::ComponentsToInstanceAlignToComponentOrigin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentsToInstanceAlignToComponentOrigin.html)
- (Optional) [IMirrorComponentFeatureData::MirrorType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirrorType.html) (if not explicitly set, defaults to [swMirrorComponentMirrorType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMirrorComponentMirrorType_e.html).swMirrorType_CenterOfBoundingBox)
- (Optional) [IMirrorComponentFeatureData::ComponentOrientationsAlignToComponentOrigin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentOrientationsAlignToComponentOrigin.html) (if not explicitly set, defaults to [swMirrorComponentOrientation2_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMirrorComponentOrientation2_e.html).swOrientation_MirroredX_MirroredY)

To create a mirror instance as a copy of the component, positioned symmetrically about a plane in one of four orientations (for fully symmetric components, all four orientations are true mirrors), use:

- MirrorPlane
- MirrorType
- ComponentOrientationsAlignToComponentOrigin
- [ComponentOrientationsAlignToSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentOrientationsAlignToSelection.html)
- ComponentsToInstanceAlignToComponentOrigin
- [ComponentsToInstanceAlignToSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentsToInstanceAlignToSelection.html)
- [AlignmentReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~AlignmentReferences.html)
- [FlipDirections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~FlipDirections.html)
- [SyncFlexibleSubAssemblies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~SyncFlexibleSubAssemblies.html)

To create a new opposite-hand version of the component (a true mirror of a nonsymmetric component), positioned symmetrically about a plane, use:

- MirrorPlane
- MirrorType
- [CreateDerivedConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~CreateDerivedConfigurations.html)
- [OppositeHandComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~OppositeHandComponents.html)
- [MirrorComponentsFolderLocation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirrorComponentsFolderLocation.html)
- [PlaceFilesInOneFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~PlaceFilesInOneFolder.html)
- [MirroredComponentFilenames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirroredComponentFilenames.html)
- [NameModifier](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~NameModifier.html)
- [NameModifierType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~NameModifierType.html)
- [ReplaceFileLocations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ReplaceFileLocations.html)
- [MirrorTransferOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirrorTransferOptions.html)
- [DimXpertScheme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~DimXpertScheme.html)
- [BreakLinksToOriginalPart](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~BreakLinksToOriginalPart.html)
- [PreserveZAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~PreserveZAxis.html)
- [PropagateFromOriginalPart](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~PropagateFromOriginalPart.html)

After specifying this interface as needed, call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) to create the feature.

This interface is analogous in functionality to the Mirror Components PropertyManager. See the following topics in the SOLIDWORKS Design user-interface help for more information:

- ****Comparing Types of Mirror Components****
- **Mirroring Components**

## Accessors

[IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html)

IFeatureManager::CreateDefinition

## Access Diagram

[MirrorComponentFeatureData](SWObjectModel.pdf#MirrorComponentFeatureData)

## See Also

[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IComponent2::IsMirrored Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsMirrored.html)
[IPartDoc::IsMirrored Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IsMirrored.html)
