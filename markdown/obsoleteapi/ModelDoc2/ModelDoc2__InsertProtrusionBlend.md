---
title: "ModelDoc2::InsertProtrusionBlend"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertProtrusionBlend.htm"
---

# ModelDoc2::InsertProtrusionBlend

This method is obsolete and has been superseded by [ModelDoc2::InsertProtusionBlend2](ModelDoc2__InsertProtrusionBlend2.htm).

Description

This method inserts a blend protrusion.

Syntax (OLE Automation)

ModelDoc2.InsertProtrusionBlend ( closed )

| Input: | (VARIANT_BOOL) closed | TRUE for a closed loft, FALSE for an open loft; if TRUE and you have selected less that three profiles, any selected guide curves must be closed curves |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->InsertProtrusionBlend ( closed )

| Input: | (VARIANT_BOOL) closed | TRUE for a closed loft, FALSE for an open loft; if TRUE and you have selected less that three profiles, any selected guide curves must be closed curves |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use guide curves, especially when selection of profiles is done in the FeatureManager design tree.

You can use any number of profiles. However, if you have selected less than three profiles, any selected guide curves must be closed curves. Use ModelDocExtension::SelectByID to select the profiles and guide curves. The mark for:

- profile selections should be a 1
- any guide curve selection, if provided, should be a 2
