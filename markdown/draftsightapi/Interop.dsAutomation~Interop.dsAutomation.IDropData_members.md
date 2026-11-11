---
title: "IDropData Interface Members"
project: ""
interface: "IDropData_members"
member: ""
kind: "members"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDropData_members.html"
---

# IDropData Interface Members

The following tables list the members exposed by [IDropData](Interop.dsAutomation~Interop.dsAutomation.IDropData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | ColorData | Gets or sets the Color stored in this drop's MIME data. |
| Property | Html | Gets or sets the HTML for this drop's MIME data. |
| Property | ImageData | Gets or sets the image stored in this drop's MIME data. |
| Property | Text | Gets or sets the text stored in this drop's MIME data. |
| Property | Urls | Gets or sets the URLs stored in this drop's MIME data. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | Clear | Removes all the MIME type and data entries in this drop's MIME data. |
| Method | GetData | Gets the data stored in this drop for the specified MIME type. |
| Method | HasColorData | Gets whether this drop can return a color. |
| Method | HasHtml | Gets whether this drop can return HTML. |
| Method | HasImageData | Gets whether this drop can return an image. |
| Method | HasText | Gets whether this drop can return plain text. |
| Method | HasUrls | Gets whether this drop can return a list of URLs. |
| Method | RemoveFormat | Removes the data entry for the specified MIME type. |
| Method | SetData | Sets the data stored in this drop for the specified MIME type. |

[Top](#topBookmark)

## See Also

[IDropData Interface](Interop.dsAutomation~Interop.dsAutomation.IDropData.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
