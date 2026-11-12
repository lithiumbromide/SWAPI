---
title: "Programming Multibody Parts"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Programming_Multibody_Parts.htm"
---

# Programming Multibody Parts

This topic provides information about programming multibody parts using the SOLIDWORKS API.

- [Obsoleted methods and their replacements](#Deprecated)
- [Changes to base features](#Changes)
- [Modifying the definition of solid features that use feature scope](#Modifying)

### Obsoleted methods and their replacements

When programming multibody parts:

| Do not use... | Instead, use... | Because... |
| --- | --- | --- |
| IFeature::GetBody | IFeature::GetFaces IFace2::GetBody | A feature can affect more than one body. Therefore, getting the faces created by a feature and getting the bodies to which the faces belong is a better way to get a feature's body or bodies. |
| IPartDoc::Body IPartDoc::IBodyObject2 | IPartDoc::GetBodies2 IPartDoc::GetRelatedBodies IPartDoc::EnumBodies3 IPartDoc::EnumRelatedBodies2 | It no longer makes sense to get the body of a part if it contains multiple bodies. In a single-body part, IPartDoc::Body and IPartDoc::IBodyObject2 still return the body, but in a multibody part, they return NULL. |

[Back to top](#Top)

### Changes to base features

Most of the methods for creating base features (cut and boss, including thin features) belong to [IFeatureManager](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeatureManager.html):

| Extrude Revolve Sweep | Loft Thicken |
| --- | --- |

These methods may include any of the following parameters that support multibody parts:

| If this parameter... | Is set to... | Then... |
| --- | --- | --- |
| Merge | True | Merging occurs and feature scope applies. |
|  | False | Merging does not occur and feature scope does not apply. |
| UseFeatScope | True | All currently selected bodies are affected. |
|  | False | All applicable bodies are affected. |
| UseAutoSelect | True | All applicable bodies are added to the selection list, which the user can edit. |
|  | False | User must select bodies. |

NOTES:

- The Merge parameter applies to bosses, but not to cuts.
- When the UseFeatScope parameter is set to false, it applies to all bodies including new bodies placed before the feature in the FeatureManager design tree.
- The UseAutoSelect parameter applies to the existing bodies only.

Examples

```vb
IFeatureManager.FeatureExtrusion3(Sd As Boolean, Flip As Boolean, Dir As Boolean, T1 As Long, T2 As Long, D1 As Double, D2 As Double, Dchk1 As Boolean, Dchk2 As Boolean, Ddir1 As Boolean, Ddir2 As Boolean, Dang1 As Double, Dang2 As Double, OffsetReverse1 As Boolean, OffsetReverse2 As Boolean, TranslateSurface1 As Boolean, TranslateSurface2 As Boolean, Merge As Boolean, UseFeatScope As Boolean, UseAutoSelect As Boolean, T0 as Long, StartOffset as Double, FlipStartOffset as Boolean) As Feature
```

```vb
IFeatureManager.FeatureCut4(Sd As Boolean, Flip As Boolean, Dir As Boolean, T1 As Long, T2 As Long, D1 As Double, D2 As Double, Dchk1 As Boolean, Dchk2 As Boolean, Ddir1 As Boolean, Ddir2 As Boolean, Dang1 As Double, Dang2 As Double, OffsetReverse1 As Boolean, OffsetReverse2 As Boolean, TranslateSurface1 As Boolean, TranslateSurface2 As Boolean, NormalCut As Boolean, UseFeatScope As Boolean, UseAutoSelect As Boolean, AssemblyFeatureScope as Boolean, AutoSelectComponents as Boolean, PropagateFeatureToParts as Boolean, T0 as Long, StartOffset as Double, FlipStartOffset as Boolean, OptimizeGeometry as Boolean) As Feature
```

In the following example, three solid bodies exist: Extrude1, Extrude2, and Extrude3. To create a through-all cut through Extrude1 and Extrude3, you could do something like the following. Notice the use of the Mark parameter.

```vb
Part.ModelDocExtension.SelectByID2 "Sketch5", "SKETCH", 0, 0, 0, 1, 0, Nothing, swSelectOptionDefault   'cut profile
Part.ModelDocExtension.SelectByID2 "Extrude3", "SOLIDBODY", 0, 0, 0, 1, 1, Nothing, swSelectOptionDefault   'body to affect
Part.ModelDocExtension.SelectByID2 "Extrude1", "SOLIDBODY", 0, 0, 0, 1, 1, Nothing, swSelectOptionDefault   'body to affect
Part.FeatureManager.FeatureCut4 1, 0, 0, 1, 0, 0.058, 0.058, 0, 0, 0, 0, 0.01, 0.01, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0.0, 0, 0 'use feature scope, do not use Autoselect
```

You can observe this by recording a macro and playing it back.

In the following example, again three solid bodies exist: Extrude1, Extrude2, and Extrude. However, in this example, a through-all extrusion boss is created and merges with Extrude1 and Extrude3. Notice the use of the Mark parameter and that Merge is set to true.

```vb
Part.ModelDocExtension.SelectByID2  "Sketch4", "SKETCH", 0, 0, 0, 1, 0, Nothing, swSelectOptionDefault   'boss profile
Part.ModelDocExtension.SelectByID2  "Extrude3", "SOLIDBODY", 0, 0, 0, 1, 1, Nothing, swSelectOptionDefault   'body to affect
Part.ModelDocExtension.SelectByID2  "Extrude1", "SOLIDBODY", 0,0,0, 1, 1, Nothing, swSelectOptionDefault   'body to affect
Part.FeatureManager.FeatureExtrusion3 1, 0, 1, 1, 0, 0.047, 0.047, 0, 0, 0, 0, 0.01, 0.01, 0, 0, 0, 0, 1, 1, 0, 0, 0.0, 0 'merge, use feature scope, do not use Autoselect
```

[Back to top](#Top)

### Modifying the definition of solid features that use feature scope

The [IExtrudeFeatureData2](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IExtrudeFeatureData2.html), [ILoftFeatureData](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ILoftFeatureData.html), [IRevolveFeatureData2](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IRevolveFeatureData2.html), [ISweepFeatureData](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISweepFeatureData.html), and [IThickenFeatureData](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IThickenFeatureData.html) have methods and properties that support multibody parts:

| Methods: | GetFeatureScopeBodiesCount IGetFeatureScopeBodies ISetFeatureScopeBodies |
| --- | --- |
| Properties: | AutoSelect (VARIANT_BOOL) FeatureScope (VARIANT_BOOL) FeatureScopeBodies (VARIANT array of bodies) |

When you get or set FeatureScopeBodies, that feature then affects all bodies in that array. Make sure that any bodies that you set in this array all exist and that [IBody2](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IBody2.html) objects are valid when the feature is in its rolled-back state (after AccessSelections is called). If the bodies are not available, then you might have to reorder features in the FeatureManager design tree to achieve the desired result.

Also, if FeatureScope is set to false or merge is set to true, then GetFeatureScopeBodiesCount returns 0 and FeatureScopeBodies is an empty array.

[Back to top](#Top)
