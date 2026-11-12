---
title: "FeatureManager::InsertMoveCopyBody"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/FeatureManager__InsertMoveCopyBody.htm"
---

# FeatureManager::InsertMoveCopyBody

This method is obsolete and has been superseded by [FeatureManager::InsertMoveCopyBody2](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertMoveCopyBody2.htm).

Description

This method moves, rotates, and makes copies of the selected solid bodies or surfaces.

Syntax (OLE Automation)

retval = FeatureManager.InsertMoveCopyBody ( transX, transY, transZ, transDist, rotPointX, rotPointY, rotPointZ, rotAngleX, rotAngleY, rotAngleZ, bCopy, numCopies )

| Input: | (double) transX | Value for delta X; applies to translation |
| --- | --- | --- |
| Input: | (double) transY | Value for delta Y; applies to translation |
| Input: | (double) transZ | Value for delta Z; applies to translation |
| Input: | (double) transDist | Distance; applies to translation |
| Input: | (double) rotPointX | Value for X rotation origin; applies to rotation |
| Input: | (double) rotPointY | Value for Y rotation origin; applies to rotation |
| Input: | (double) rotPointZ | Value for Z rotation origin; applies to rotation |
| Input: | (double) rotAngleX | Value for X rotation angle; applies to rotation |
| Input: | (double) rotAngleY | Value for Y rotation angle; applies to rotation |
| Input: | (double) rotAngleZ | Value for Z rotation angle; applies to rotation |
| Input: | (VARIANT_BOOL) bCopy | TRUE if a copy operation, FALSE if a move operation |
| Input: | (long) numCopies | Number of copies to create |
| Output: | (LPFEATURE) retval | Pointer to the Feature object |

Syntax (COM)

status = FeatureManager->InsertMoveCopyBody ( transX, transY, transZ, transDist, rotPointX, rotPointY, rotPointZ, rotAngleX, rotAngleY, rotAngleZ, bCopy, numCopies, &retval )

| Input: | (double) transX | Value for delta X; applies to translation |
| --- | --- | --- |
| Input: | (double) transY | Value for delta Y; applies to translation |
| Input: | (double) transZ | Value for delta Z; applies to translation |
| Input: | (double) transDist | Distance; applies to translation |
| Input: | (double) rotPointX | Value for X rotation origin; applies to rotation |
| Input: | (double) rotPointY | Value for Y rotation origin; applies to rotation |
| Input: | (double) rotPointZ | Value for Z rotation origin; applies to rotation |
| Input: | (double) rotAngleX | Value for X rotation angle; applies to rotation |
| Input: | (double) rotAngleY | Value for Y rotation angle; applies to rotation |
| Input: | (double) rotAngleZ | Value for Z rotation angle; applies to rotation |
| Input: | (VARIANT_BOOL) bCopy | TRUE if a copy operation, FALSE if a move operation |
| Input: | (long) numCopies | Number of copies to create |
| Output: | (LPFEATURE) retval | Pointer to the feature object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method applies either to the specified translation or rotation. If you specify both translation and rotation, only the translation is applied.

See the Insert, Surface, Move/Copy command in the SolidWorks Help for details about moving, rotating, and copying solid bodies and surfaces.
