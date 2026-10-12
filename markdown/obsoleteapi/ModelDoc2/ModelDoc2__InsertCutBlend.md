---
title: "ModelDoc2::InsertCutBlend"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertCutBlend.htm"
---

# ModelDoc2::InsertCutBlend

This method is obsolete and has been superseded by [ModelDoc2::InsertCutBlend2](ModelDoc2__InsertCutBlend2.htm).

Description

This method inserts a lofted cut based on the selected profiles and guide curves. Selection of guide curves is optional; however, selection of the profiles must be in an order consistent with the desired direction of the loft.

Syntax (OLE Automation)

ModelDoc2.InsertCutBlend ( closed )

| Input: | (VARIANT_BOOL) closed | TRUE for a closed loft, FALSE for an open loft; if TRUE and if you have selected less than three profiles, any selected guide curves must be closed curves |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->InsertCutBlend ( closed )

| Input: | (VARIANT_BOOL) closed | TRUE for a closed loft, FALSE for an open loft; if TRUE and if you have selected less than three profiles, any selected guide curves must be closed curves |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use of guide curves is recommended especially when selection of profiles is done in the FeatureManager design tree.

You can use any number of profiles; however, if you have selected less that three profiles, then any selected guide curves must be closed curves.

Use ModelDocExtension::SelectByID to select the profiles and guide curves. The mark for:

- profile selections should be a 1.
- any guide curve selection, if provided, should be a 2.
