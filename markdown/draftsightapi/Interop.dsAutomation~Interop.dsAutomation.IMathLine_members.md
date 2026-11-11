---
title: "IMathLine Interface Members"
project: ""
interface: "IMathLine_members"
member: ""
kind: "members"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathLine_members.html"
---

# IMathLine Interface Members

The following tables list the members exposed by [IMathLine](Interop.dsAutomation~Interop.dsAutomation.IMathLine.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | EndPoint | Gets or sets the end point of the bounded mathematical line or the second point on the Ray or InfiniteLine. |
| Property | StartPoint | Gets or sets the starting point of the bounded mathematical line or the Ray or the first point on the InfiniteLine. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetClosestPointTo | Gets the point on the mathematical line that is closest to the specified point. |
| Method | GetClosestPointToCircArc | Gets the point on the mathematical line that is closest to the specified mathematical circular Arc, and gets the point on the specified mathematical circular Arc that is closest to the mathematical line. |
| Method | GetClosestPointToEllipArc | Gets the point on the mathematical line that is closest to the specified mathematical elliptical Arc, and gets the point on the specified mathematical elliptical Arc that is closest to the mathematical line. |
| Method | GetClosestPointToLinearObject | Gets the point on the mathematical line that is closest to the specified linear object, and the gets point on the specified linear object that is closest to the mathematical line. |
| Method | GetDirection | Gets a unit vector that is parallel to this mathematical line, pointing in a positive direction. |
| Method | GetLength | Gets the length of the bounded mathematical line. |
| Method | GetType | Gets the type of this mathematical line. |
| Method | IntersectWithLinearObject | Gets the point where this mathematical line intersects the specified linear object. |
| Method | IntersectWithPlane | Gets the point where this mathematical line intersects with the specified intersecting plane. |
| Method | IsParallelToLine | Gets whether the specified mathematical line is parallel to this mathematical line within the specified tolerance. |
| Method | IsPerpendicularToLine | Gets whether the specified mathematical line is perpendicular to this mathematical line within the specified tolerance. |
| Method | TransformBy | Applies the specified mathematical transformation to this mathematical line. |

[Top](#topBookmark)

## See Also

[IMathLine Interface](Interop.dsAutomation~Interop.dsAutomation.IMathLine.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
