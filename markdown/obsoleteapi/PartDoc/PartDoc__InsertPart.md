---
title: "PartDoc::InsertPart"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__InsertPart.htm"
---

# PartDoc::InsertPart

This method is obsolete and has been superseded by [PartDoc::InsertPart2.](sldworksAPI.chm::/PartDoc/PartDoc__InsertPart2.htm)

Description

This method inserts an existing part into this part document.

Syntax (OLE Automation)

retval = PartDoc.InsertPart ( fileName, ImportPlane, ImportAxis, ImportCThread )

| Input: | (BSTR) fileName | Name of part file |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) ImportPlane | TRUE if the planes from the part should be imported into this part, FALSE if not |
| Input: | (VARIANT_BOOL) ImportAxis | TRUE if the axes from the part should be imported into this part, FALSE if not |
| Input | (VARIANT_BOOL) ImportCThread | TRUE if the cosmetic threads from the part should be imported into this part, FALSE if not |
| Output: | (LPDISPATCH) retval | Dispatch pointer to the inserted feature |

Syntax (COM)

status = PartDoc->InsertPart ( fileName, ImportPlane, ImportAxis, ImportCThread, &retval )

| Input: | (BSTR) fileName | Name of part file |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) ImportPlane | TRUE if the planes from the part should be imported into this part, FALSE if not |
| Input: | (VARIANT_BOOL) ImportAxis | TRUE if the axes from the part should be imported into this part, FALSE if not |
| Input: | (VARIANT_BOOL) ImportCThread | TRUE if the cosmetic threads from the part should be imported into this part, FALSE if not |
| Output: | (LPFEATURE) retval | Pointer to the inserted feature |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method inserts the specified part at the origin of this part. To position the insert part at a different location or orientation or both, use FeatureManager::InsertMoveCopyBody2.

The interface returned by this method is LPFEATURE, which gives you access to the Feature APIs, such as Feature::Name to get or set the name of the feature.
