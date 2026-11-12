---
title: "ModelDoc::RayIntersections"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__RayIntersections.htm"
---

# ModelDoc::RayIntersections

This method is obsolete and has been superseded by [ModelDoc2::RayIntersections](sldworksAPI.chm::/ModelDoc2/ModelDoc2__RayIntersections.htm).

Description

This method intersects a given set of rays with a specified set of bodies. The resulting information, a set of intersection points, intersection normals, and the bodies that were hit from your bodiesIn array, can be retrieved by calling ModelDoc::GetRayIntersectionsPoints and ModelDoc::GetRayIntersectionsTopology.

Syntax (OLE Automation)

retval = ModelDoc.RayIntersections ( bodiesIn, basePointsIn, vectorsIn, options, hitRadius, offset )

| Input: | (VARIANT) bodiesIn | SafeArray of Dispatch pointers; these are the Body objects that will be hit by the rays |
| --- | --- | --- |
| Input: | (VARIANT) basePointsIn | SafeArray of doubles containing the x,y,z base points of each ray |
| Input: | (VARIANT) vectorsIn | SafeArray of doubles containing the direction vectors of each ray |
| Input: | (long) options | Any number of options as defined in swRayPtsOpts_e; concatenate any options using the "or" operator. |
| Input: | (double) hitRadius | Radius of hit cylinder; this is used mainly in grazing cases to establish a hit |
| Input: | (double) offset | Length tolerance to use to establish whether a hit on a face represents the entry or exit of the ray from the body |
| Return: | (long) retval | Number of intersections found |

Syntax (COM)

status = ModelDoc->IRayIntersections ( bodiesIn, numBodies, basePointsIn, vectorsIn, numRays, options, hitRadius, offset, &retval )

| Input: | (LPBODY*) bodiesIn | Array of pointers to the Body objects; these are the Body objects that will be hit by the rays |
| --- | --- | --- |
| Input: | (long) numBodies | Number of bodies in the bodiesIn array |
| Input: | (double*) basePointsIn | Array containing the x,y,z base points of each ray |
| Input: | (double*) vectorsIn | Array containing the direction vectors of each ray |
| Input: | (long) numRays | Number of rays specified; this should be equal to the number of elements in the (basePointsIn / 3) or (vectorsIn / 3) arrays |
| Input: | (long) options | Any number of options selected as defined in swRayPtsOpts_e; concatenate these options using the "or" operator |
| Input: | (double) hitRadius | Radius of hit cylinder used mainly in grazing cases to establish a hit |
| Input: | (double) offset | Length tolerance to use to establish whether a hit on a face represents the entry or exit of the ray from the body |
| Output: | (long) retval | Number of intersections found |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The method performs the intersection operations between the specified bodies and the ray vectors provided. To get the results of the intersection operations, you must call ModelDoc::GetRayIntersectionsPoints and ModelDoc::GetRayIntersectionsTopology.

Information returned by ModelDoc::GetRayIntersectionsPoints and ModelDoc::GetRayIntersectionsTopology depends partially on the value of the options argument. Valid values, which can take values from the swRayPtsOpts_e enumerator, can be concatenated together using bitwise operations. Refer to ModelDoc::GetRayIntersectionsPoints to see which data is always output regardless of the values specified in the options argument.

For the COM interface, the return value, the intersection count, must be used in determining the size of arrays to allocate for return values from ModelDoc::GetRayIntersectionsPoints and ModelDoc::GetRayIntersectionsTopology.

For each ray that hits an edge or a vertex, the offset distance is added in both the positive and negative directions along the ray and the points computed will be tested for spatial inclusion in the hit body. This will be used to determine if the ray was entering, leaving, or just grazing the body at the hit point. Entry and exit onto faces can be computed more simply and does not require such an offset.
