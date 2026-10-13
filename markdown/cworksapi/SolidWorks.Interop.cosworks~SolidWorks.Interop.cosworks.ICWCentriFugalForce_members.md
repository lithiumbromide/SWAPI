---
title: "ICWCentriFugalForce Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCentriFugalForce_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce_members.html"
---

# ICWCentriFugalForce Interface Members

The following tables list the members exposed by [ICWCentriFugalForce](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AngularAcceleration | Gets or sets the angular acceleration used for centrifugal loading. |
| Property | AngularVelocity | Gets or sets the angular velocity used for centrifugal loading. |
| Property | ReverseAngAccelerationDirection | Obsolete. Superseded by ICWCentrifugalForce::ReverseAngAccelerationDirection2 . |
| Property | ReverseAngAccelerationDirection2 | Gets or sets whether to reverse the direction of angular acceleration. |
| Property | ReverseAngVelocityDirection | Obsolete. Superseded by ICWCentrifugalForce::ReverseAngVelocityDirection2 . |
| Property | ReverseAngVelocityDirection2 | Gets or sets whether to reverse the direction of angular velocity. |
| Property | Unit | Gets or sets the unit system for centrifugal load parameters. |
| Property | UseTimeCurve | Obsolete. Superseded by ICWCentrifugalForce::UseTimeCurve2 . |
| Property | UseTimeCurve2 | Gets or sets whether to use a time curve for this centrifugal force. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | CFForceBeginEdit | Starts editing a centrifugal force. |
| Method | CFForceEndEdit | Ends editing of a centrifugal force. |
| Method | GetTimeCurve | Gets the time curve data. |
| Method | SetReferenceEntity | Replaces the direction reference entity. |
| Method | SetTimeCurve | Obsolete. Superseded by ICWCentrifugalForce::SetTimeCurve2 . |
| Method | SetTimeCurve2 | Defines a time curve. |

[Top](#topBookmark)

## See Also

[ICWCentriFugalForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
