---
title: "FeatureManager::InsertMirrorFeature"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__InsertMirrorFeature.htm"
---

# FeatureManager::InsertMirrorFeature

This method is obsolete and has been superseded by [FeatureManager::InsertMirrorFeature2](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertMirrorFeature2.htm).

Description

This method mirrors selected features, faces, and bodies about a selected plane or planar face.

Syntax (OLE Automation)

retval = FeatureManager.InsertMirrorFeature ( bMirrorBody, bGeometryPattern, bMerge, bKnit )

| Input: | (VARIANT_BOOL) bMirrorBody | TRUE to mirror solid bodies; FALSE to mirror a feature or face |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) bGeometryPattern | TRUE to mirror only the feature geometry, FALSE to solve the entire feature; applies to mirroring features only |
| Input: | (VARIANT_BOOL) bMerge | TRUE to merge any mirrored solid bodies, FALSE to not; applies to mirroring solid bodies only |
| Input: | (VARIANT_BOOL) bKnit | TRUE to knit surfaces, FALSE to not; applies to mirroring surfaces only |
| Output: | (LPFEATURE) retval | Pointer to the Feature object |

Syntax (COM)

status = FeatureManager->InsertMirrorFeature ( bMirrorBody, bGeometryPattern, bMerge, bKnit, &retval )

| Input: | (VARIANT_BOOL) bMirrorBody | TRUE to mirror solid bodies; FALSE to mirror a feature |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) bGeometryPattern | TRUE to mirror only the feature geometry, FALSE to solve the entire feature; applies to mirroring features only |
| Input: | (VARIANT_BOOL) bMerge | TRUE to merge the solid bodies, FALSE to not; applies to mirroring solid bodies only |
| Input: | (VARIANT_BOOL) bKnit | TRUE to knit surfaces, FALSE to not; applies to mirroring surfaces only |
| Output: | (LPFEATURE) retval | Pointer to the Feature object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method attempts to create the mirror feature without displaying a dialog box to get information from the user. It relies on preselected and marked entities, as well as arguments.

| Any... | Must be preselected and marked with a value of... |
| --- | --- |
| Features to be mirrored | 1 |
| Faces to be mirrored | 128 |
| Bodies to be mirrored | 256 |
| Plane or planar face | 2 |

For information on selecting and marking entities, refer to ModelDocExtension::SelectByID2.
