---
title: "ModelDoc::FeatureChamferType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FeatureChamferType.htm"
---

# ModelDoc::FeatureChamferType

This method is obsolete and has been superseded by [ModelDoc2::FeatureChamferType](../ModelDoc2/ModelDoc2__FeatureChamferType.htm).

Description

This method creates a chamfer feature according to the type specified (angle-distance, distance-distance, or vertex chamfer).

Syntax (OLE Automation)

(void) ModelDoc.FeatureChamferType ( chamferType, width, angle, flip, otherDist, vertexChamDist1, vertexChamDist2, vertexChamDist3 )

| Input: | (short) chamferType | Chamfer type see swChamferType_e |
| --- | --- | --- |
| Input: | (double) width | Width for angle-distance chamfers, one distance for distance-distance chamfers |
| Input: | (double) angle | Angle for angle-distance chamfers |
| Input: | (BOOL) flip | Flip flag |
| Input: | (double) otherDist | Other distance for distance-distance chamfers |
| Input: | (double) vertexChamDist1 | First distance for vertex chamfers |
| Input: | (double) vertexChamDist2 | Second distance for vertex chamfers |
| Input: | (double) vertexChamDist3 | Last distance for vertex chamfers |

Syntax (COM)

status = ModelDoc->FeatureChamferType ( chamferType, width, angle, flip, otherDist, vertexChamDist1, vertexChamDist2, vertexChamDist3 )

| Input: | (short) chamferType | Chamfer type see swChamferType_e |
| --- | --- | --- |
| Input: | (double) width | Width for angle-distance chamfers, one distance for distance-distance chamfers |
| Input: | (double) angle | Angle for angle-distance chamfers |
| Input: | (VARIANT_BOOL) flip | Flip flag |
| Input: | (double) otherDist | Other distance for distance-distance chamfers |
| Input: | (double) vertexChamDist1 | First distance for vertex chamfers |
| Input: | (double) vertexChamDist2 | Second distance for vertex chamfers |
| Input: | (double) vertexChamDist3 | Last distance for vertex chamfers |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Both angle-distance and distance-distance chamfers are edge chamfers. All measurements are from edges. An angle-distance chamfer requires an angle and a distance; a distance-distance chamfer requires two distances for both sides of the chamfered edges.

A vertex chamfer only works on a vertex with three adjacent edges of the same convexity. The distance values specified measure from the vertex along three adjacent edges. For non-linear edges, this value is an arc length value. It is not a chordal value.

To determine the edge ordering used by this method, use Vertex::EnumEdgesOriented.
