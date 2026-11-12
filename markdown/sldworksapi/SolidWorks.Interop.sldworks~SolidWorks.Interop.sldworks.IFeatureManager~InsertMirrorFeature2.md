---
title: "InsertMirrorFeature2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertMirrorFeature2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMirrorFeature2.html"
---

# InsertMirrorFeature2 Method (IFeatureManager)

Mirrors selected features, faces, bodies, and structure systems about a selected plane or planar face.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertMirrorFeature2( _
   ByVal BMirrorBody As System.Boolean, _
   ByVal BGeometryPattern As System.Boolean, _
   ByVal BMerge As System.Boolean, _
   ByVal BKnit As System.Boolean, _
   ByVal ScopeOptions As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim BMirrorBody As System.Boolean
Dim BGeometryPattern As System.Boolean
Dim BMerge As System.Boolean
Dim BKnit As System.Boolean
Dim ScopeOptions As System.Integer
Dim value As Feature

value = instance.InsertMirrorFeature2(BMirrorBody, BGeometryPattern, BMerge, BKnit, ScopeOptions)
```

### C#

```csharp
Feature InsertMirrorFeature2(
   System.bool BMirrorBody,
   System.bool BGeometryPattern,
   System.bool BMerge,
   System.bool BKnit,
   System.int ScopeOptions
)
```

### C++/CLI

```cpp
Feature^ InsertMirrorFeature2(
   System.bool BMirrorBody,
   System.bool BGeometryPattern,
   System.bool BMerge,
   System.bool BKnit,
   System.int ScopeOptions
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BMirrorBody`: True to mirror solid bodies; false to mirror a feature or face
- `BGeometryPattern`: True to mirror only the feature geometry, false to solve the entire feature; applies to mirroring features only
- `BMerge`: True to merge any mirrored solid bodies, false to not; applies to mirroring solid bodies only
- `BKnit`: True to knit surfaces, false to not; applies to mirroring surfaces only
- `ScopeOptions`: Feature scope as defined by [swFeatureScope_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureScope_e.html)

### Return Value

[Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertMirrorFeature2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertMirrorFeature2.html).

## Examples

See the [IMirrorSolidFeatureData::StructureSystemToPatternArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~StructureSystemToPatternArray.html) examples.

## Examples

[Get Mirror Pattern Feature Data (C#)](Get_Mirror_Pattern_Feature_Data_Example_CSharp.htm)
[Get Mirror Pattern Feature Data (VB.NET)](Get_Mirror_Pattern_Feature_Data_Example_VBNET.htm)
[Get Mirror Pattern Feature Data (VBA)](Get_Mirror_Feature_Data_Example_VB.htm)

## Remarks

This method attempts to create the mirror feature without displaying a dialog box to get information from the user. It relies on preselected and marked entities and arguments.

Structure systems 134217728

| Any of these entities to be mirrored... | Must be preselected and marked with a value of... |
| --- | --- |
| Features | 1 |
| Faces | 128 |
| Bodies | 256 |
| Structure systems | 134217728 |
| Planes or planar faces | 2 |

For information on selecting and marking entities, see [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IMirrorPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
