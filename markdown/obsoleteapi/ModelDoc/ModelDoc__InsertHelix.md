---
title: "ModelDoc::InsertHelix"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertHelix.htm"
---

# ModelDoc::InsertHelix

This method is obsolete and has been superseded by [ModelDoc2::InsertHelix](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertHelix.htm).

Description

This method creates a helix.

Syntax (OLE Automation)

void ModelDoc.InsertHelix ( reversed, clockwised, tapered, outward, helixdef, height, pitch, revolution, taperangle, startangle)

| Input: | (BOOL) reversed | TRUE will create helix in opposite direction of the circle used to define the helix diameter, FALSE will create the helix in direction of the circle's normal vector; the normal vector of a circle, for example, would be out of the screen if the circle were drawn in a CCW direction |
| --- | --- | --- |
| Input: | (BOOL) clockwised | TRUE for clockwise, FALSE for counter-clockwise |
| Input: | (BOOL) tapered | TRUE to taper the helix, FALSE for no taper |
| Input: | (BOOL) outward | TRUE to taper the helix outward, FALSE for inward |
| Input: | (long) helixdef | Helix definition; based on this value, fill in appropriate arguments: 0 = (pitch and rev) 1 = (height and rev) 2 = (height and pitch) 3 = (Spiral) |
| Input: | (double) height | Height of helix in meters |
| Input: | (double) pitch | Helix pitch |
| Input: | (double) revolution | Number of revolutions |
| Input: | (double) taperangle | Taper angle |
| Input: | (double) startangle | Start angle rotation from base axis in radians |

Syntax (COM)

status = ModelDoc->InsertHelix ( reversed, clockwised, tapered, outward, helixdef, height, pitch, revolution, taperangle, startangle )

| Input: | (VARIANT_BOOL) reversed | TRUE will create helix in opposite direction of the circle used to define the helix diameter, FALSE will create the helix in direction of the circle's normal vector; the normal vector of a circle, for example, would be out of the screen if the circle were drawn in a CCW direction |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) clockwised | TRUE for clockwise, FALSE for counter-clockwise |
| Input: | (VARIANT_BOOL) tapered | TRUE to taper the helix, FALSE for no taper |
| Input: | (VARIANT_BOOL) outward | TRUE to taper the helix outward, FALSE for inward |
| Input: | (long) helixdef | Helix definition; based on this value, fill in appropriate arguments: 0 = (pitch and rev) 1 = (height and rev) 2 = (height and pitch) 3 = (Spiral) |
| Input: | (double) height | Hheight of helix in meters |
| Input: | (double) pitch | Helix pitch |
| Input: | (double) revolution | Number of revolutions |
| Input: | (double) taperangle | Taper angle |
| Input: | (double) startangle | Start angle rotation from base axis in radians |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

When creating a helix defined as spiral, you need to specify the helix pitch and number of revolutions using the appropriate arguments.
