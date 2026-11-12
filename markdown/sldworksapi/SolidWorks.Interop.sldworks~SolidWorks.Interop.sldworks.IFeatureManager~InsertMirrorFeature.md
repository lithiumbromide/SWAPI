---
title: "InsertMirrorFeature Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertMirrorFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMirrorFeature.html"
---

# InsertMirrorFeature Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertMirrorFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertMirrorFeature2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertMirrorFeature( _
   ByVal BMirrorBody As System.Boolean, _
   ByVal BGeometryPattern As System.Boolean, _
   ByVal BMerge As System.Boolean, _
   ByVal BKnit As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim BMirrorBody As System.Boolean
Dim BGeometryPattern As System.Boolean
Dim BMerge As System.Boolean
Dim BKnit As System.Boolean
Dim value As Feature

value = instance.InsertMirrorFeature(BMirrorBody, BGeometryPattern, BMerge, BKnit)
```

### C#

```csharp
Feature InsertMirrorFeature(
   System.bool BMirrorBody,
   System.bool BGeometryPattern,
   System.bool BMerge,
   System.bool BKnit
)
```

### C++/CLI

```cpp
Feature^ InsertMirrorFeature(
   System.bool BMirrorBody,
   System.bool BGeometryPattern,
   System.bool BMerge,
   System.bool BKnit
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BMirrorBody`: True to mirror solid bodies; false to mirror a feature or face
- `BGeometryPattern`: True to mirror only the feature geometry, false to solve the entire feature; applies
  to mirroring features only
- `BMerge`: True to merge any mirrored solid bodies, false to not; applies to mirroring solid
  bodies only
- `BKnit`: True to knit surfaces, false to not; applies to mirroring surfaces only

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertMirrorFeature](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertMirrorFeature.html).

## Remarks

This method attempts to create the mirror feature without displaying a dialog box to get information from the user. It relies on preselected and marked entities, as well as arguments.

| Any... | Must be preselected and marked with a value of... |
| --- | --- |
| Features to be mirrored | 1 |
| Faces to be mirrored | 128 |
| Bodies to be mirrored | 256 |
| Plane or planar face | 2 |

For information on selecting and marking entities, see [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IMirrorSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData.html)
[IMirrorPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
