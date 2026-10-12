---
title: "InsertMateReference2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertMateReference2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMateReference2.html"
---

# InsertMateReference2 Method (IFeatureManager)

Inserts a mate reference for a part or assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertMateReference2( _
   ByVal BstrMateReferenceName As System.String, _
   ByVal PrimaryReferenceEntity As Entity, _
   ByVal PrimaryReferenceType As System.Integer, _
   ByVal PrimaryReferenceAlignment As System.Integer, _
   ByVal PrimaryReferenceAlignAxes As System.Boolean, _
   ByVal SecondaryReferenceEntity As Entity, _
   ByVal SecondaryReferenceType As System.Integer, _
   ByVal SecondaryReferenceAlignment As System.Integer, _
   ByVal SecondaryReferenceAlignAxes As System.Boolean, _
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
Dim PrimaryReferenceAlignAxes As System.Boolean
Dim SecondaryReferenceEntity As Entity
Dim SecondaryReferenceType As System.Integer
Dim SecondaryReferenceAlignment As System.Integer
Dim SecondaryReferenceAlignAxes As System.Boolean
Dim TertiaryReferenceEntity As Entity
Dim TertiaryReferenceType As System.Integer
Dim TertiaryReferenceAlignment As System.Integer
Dim value As Feature

value = instance.InsertMateReference2(BstrMateReferenceName, PrimaryReferenceEntity, PrimaryReferenceType, PrimaryReferenceAlignment, PrimaryReferenceAlignAxes, SecondaryReferenceEntity, SecondaryReferenceType, SecondaryReferenceAlignment, SecondaryReferenceAlignAxes, TertiaryReferenceEntity, TertiaryReferenceType, TertiaryReferenceAlignment)
```

### C#

```csharp
Feature InsertMateReference2(
   System.string BstrMateReferenceName,
   Entity PrimaryReferenceEntity,
   System.int PrimaryReferenceType,
   System.int PrimaryReferenceAlignment,
   System.bool PrimaryReferenceAlignAxes,
   Entity SecondaryReferenceEntity,
   System.int SecondaryReferenceType,
   System.int SecondaryReferenceAlignment,
   System.bool SecondaryReferenceAlignAxes,
   Entity TertiaryReferenceEntity,
   System.int TertiaryReferenceType,
   System.int TertiaryReferenceAlignment
)
```

### C++/CLI

```cpp
Feature^ InsertMateReference2(
   System.String^ BstrMateReferenceName,
   Entity^ PrimaryReferenceEntity,
   System.int PrimaryReferenceType,
   System.int PrimaryReferenceAlignment,
   System.bool PrimaryReferenceAlignAxes,
   Entity^ SecondaryReferenceEntity,
   System.int SecondaryReferenceType,
   System.int SecondaryReferenceAlignment,
   System.bool SecondaryReferenceAlignAxes,
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
- `PrimaryReferenceAlignAxes`: True to align with the axes of the coordinate system or origin when forming a mate, false to not
- `SecondaryReferenceEntity`: Pointer to the secondary mate, the [IEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) object
- `SecondaryReferenceType`: Secondary mate's reference type as defined by [swMateReferenceType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceType_e.html)
- `SecondaryReferenceAlignment`: Secondary mate's alignment type as defined [swMateReferenceAlignment_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceAlignment_e.html)
- `SecondaryReferenceAlignAxes`: True to align with the axes of the coordinate system or origin when forming a mate, false to not
- `TertiaryReferenceEntity`: Pointer to the tertiary mate, the [IEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) object
- `TertiaryReferenceType`: Tertiary mate's reference type as defined by [swMateReferenceType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceType_e.html)
- `TertiaryReferenceAlignment`: Tertiary mate's reference alignment as defined by [swMateReferenceAlignment_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceAlignment_e.html)

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertMateReference2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertMateReference2.html).

## Examples

[Edit Mate Reference (C#)](Edit_Mate_Reference_Example_CSharp.htm)
[Edit Mate Reference (VB.NET)](Edit_Mate_Reference_Example_VBNET.htm)
[Edit Mate Reference (VBA)](Edit_Mate_Reference_Example_VB.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IMateReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
