---
title: "ICallout Interface Members"
project: "SOLIDWORKS API Help"
interface: "ICallout_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.html"
---

# ICallout Interface Members

The following tables list the members exposed by [ICallout](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | EnablePushPin | Gets or sets whether to enable the pushpin for this callout. |
| Property | FontSize | Gets or sets the font size for this callout. |
| Property | IgnoreValue | Gets or sets whether to ignore the callout value in the given row. |
| Property | Label2 | Gets or sets the text for the label in the specified row of this callout. |
| Property | MultipleLeaders | Gets or sets the display of multiple leaders for this callout. |
| Property | OpaqueColor | Gets or sets the opaque (background) color for the labels for this callout. |
| Property | Position | Gets and sets the position of this callout. |
| Property | SkipColon | Gets and sets whether to add a colon at the end of the callout label. |
| Property | TargetStyle | Gets or sets the type of connection at the target point for this callout. |
| Property | TextBox | Gets or sets whether the callout text is enclosed within a box. |
| Property | TextColor | Gets or sets the color of the text in the specified row in this callout. |
| Property | TextFormat | Gets or sets the text format for this callout. |
| Property | Value | Gets or sets the value in for the specified row in this callout. |
| Property | ValueInactive | Gets or sets whether the user can edit the value in the specified row in this callout. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | Display | Shows or hides the independent (i.e., not attached to a selection) callout. |
| Method | GetLeader | Gets the leader properties of the callout. |
| Method | GetTargetPoint | Gets the target point for the specified row in this callout. |
| Method | SetLeader | Sets the leader properties of the callout. |
| Method | SetTargetPoint | Sets the target point for the specified row in this callout. |
| Method | UpdatePosition | Obsolete. Superseded by Callout::Position . |

[Top](#topBookmark)

## See Also

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
