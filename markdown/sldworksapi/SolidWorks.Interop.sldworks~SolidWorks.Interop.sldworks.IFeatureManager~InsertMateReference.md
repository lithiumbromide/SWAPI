---
title: "InsertMateReference Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertMateReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMateReference.html"
---

# InsertMateReference Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertMateReference2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertMateReference2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertMateReference( _
   ByVal BstrMateReferenceName As System.String, _
   ByVal PrimaryReferenceEntity As Entity, _
   ByVal PrimaryReferenceType As System.Integer, _
   ByVal PrimaryReferenceAlignment As System.Integer, _
   ByVal SecondaryReferenceEntity As Entity, _
   ByVal SecondaryReferenceType As System.Integer, _
   ByVal SecondaryReferenceAlignment As System.Integer, _
   ByVal TertiaryReferenceEntity As Entity, _
   ByVal TertiaryReferenceType As System.Integer, _
   ByVal TertiaryReferenceAlignment As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim BstrMateReferenceName As System.String
Dim PrimaryReferenceEntity As Entity
Dim PrimaryReferenceType As System.Integer
Dim PrimaryReferenceAlignment As System.Integer
Dim SecondaryReferenceEntity As Entity
Dim SecondaryReferenceType As System.Integer
Dim SecondaryReferenceAlignment As System.Integer
Dim TertiaryReferenceEntity As Entity
Dim TertiaryReferenceType As System.Integer
Dim TertiaryReferenceAlignment As System.Integer
Dim value As Feature

value = instance.InsertMateReference(BstrMateReferenceName, PrimaryReferenceEntity, PrimaryReferenceType, PrimaryReferenceAlignment, SecondaryReferenceEntity, SecondaryReferenceType, SecondaryReferenceAlignment, TertiaryReferenceEntity, TertiaryReferenceType, TertiaryReferenceAlignment)
```

### C#

```csharp
Feature InsertMateReference(
   System.string BstrMateReferenceName,
   Entity PrimaryReferenceEntity,
   System.int PrimaryReferenceType,
   System.int PrimaryReferenceAlignment,
   Entity SecondaryReferenceEntity,
   System.int SecondaryReferenceType,
   System.int SecondaryReferenceAlignment,
   Entity TertiaryReferenceEntity,
   System.int TertiaryReferenceType,
   System.int TertiaryReferenceAlignment
)
```

### C++/CLI

```cpp
Feature^ InsertMateReference(
   System.String^ BstrMateReferenceName,
   Entity^ PrimaryReferenceEntity,
   System.int PrimaryReferenceType,
   System.int PrimaryReferenceAlignment,
   Entity^ SecondaryReferenceEntity,
   System.int SecondaryReferenceType,
   System.int SecondaryReferenceAlignment,
   Entity^ TertiaryReferenceEntity,
   System.int TertiaryReferenceType,
   System.int TertiaryReferenceAlignment
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BstrMateReferenceName`: Name of mate reference
- `PrimaryReferenceEntity`: Pointer to the primary mate, the [IEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) object
- `PrimaryReferenceType`: Primary mate's reference type as defined by [swMateReferenceType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceType_e.html)
- `PrimaryReferenceAlignment`: Primary mate's reference alignment type as defined [swMateReferenceAlignment_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceAlignment_e.html)
- `SecondaryReferenceEntity`: Pointer to the secondary mate, the [IEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) object
- `SecondaryReferenceType`: Secondary mate's reference type as defined by [swMateReferenceType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceType_e.html)
- `SecondaryReferenceAlignment`: Secondary mate's alignment type as defined [swMateReferenceAlignment_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceAlignment_e.html)
- `TertiaryReferenceEntity`: Pointer to the tertiary mate, the [IEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) object
- `TertiaryReferenceType`: Tertiary mate's reference type as defined by [swMateReferenceType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceType_e.html)
- `TertiaryReferenceAlignment`: Tertiary mate's reference alignment as defined by [swMateReferenceAlignment_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceAlignment_e.html)

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertMateReference](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertMateReference.html).

## Remarks

Either select the mate references interactively or select them programmatically using [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) with marks of 1, 2, and 4. If the mate references are interactively selected, then specify NOTHING for PrimaryReferenceEntity, SecondaryReferenceEntity, and TertiaryReferenceEntity.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IMateReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
