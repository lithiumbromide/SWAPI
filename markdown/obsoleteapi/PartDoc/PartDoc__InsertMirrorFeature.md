---
title: "PartDoc::InsertMirrorFeature"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__InsertMirrorFeature.htm"
---

# PartDoc::InsertMirrorFeature

This method is obsolete and has been superseded by [FeatureManager::InsertMirrorFeature](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertMirrorFeature.htm).

Description

This method mirrors selected features and faces about a selected plane or planar face.

Syntax (OLE Automation)

retval = PartDoc.InsertMirrorFeature ( GeometryPattern )

| Input: | (BOOL) GeometryPattern | TRUE to mirror only the feature geometry, FALSE to solve the entire feature |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the feature is successfully created, FALSE if not |

Syntax (COM)

status = PartDoc->InsertMirrorFeature ( GeometryPattern, &retval )

| Input: | (VARIANT_BOOL) GeometryPattern | TRUE to mirror only the feature geometry, FALSE to solve the entire feature |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the feature is successfully created, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Unlike PartDoc::MirrorFeature, this method tries to create the mirror feature without displaying a dialog box to get information from the end-user. It relies on preselected and marked entities and arguments.

- Any features to be mirrored must be preselected and marked with a value of 1.
- Any faces to be mirrored must be preselected and marked with a value of 128.
- The plane or planar face to mirror about needs must be preselected and marked with a value of 2.

For information on selecting and marking entities, see ModelDocExtension::SelectByID.

This method returns a TRUE or FALSE to indicate whether or not the mirror all feature was created. If it is successful, the newly created feature remains selected after the method runs. You can use SelectionMgr::GetSelectedObject3 to retrieve this object.
