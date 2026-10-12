---
title: "BomFeature::FollowAssemblyOrder"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BomFeature/BomFeature__FollowAssemblyOrder.htm"
---

# BomFeature::FollowAssemblyOrder

This method is obsolete and has been superseded by [BomFeature::FollowAssemblyOrder2](sldworksAPI.chm::/BomFeature/BomFeature__FollowAssemblyOrder2.htm).

Description

This method sets the order of the item numbers to follow the order in which the assembly appears in the FeatureManager design tree.

Syntax (OLE Automation)

retval = BomFeature.FollowAssemblyOrder ()

| Output: | (VARIANT_BOOL) retval | TRUE if the order of the item numbers follows the order in which the assembly appears in the FeatureManager design tree, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = BomFeature->FollowAssemblyOrder ( &retval)

| Output: | (VARIANT_BOOL) retval | TRUE if the order of the item numbers follows the order in which the assembly appears in the FeatureManager design tree, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
