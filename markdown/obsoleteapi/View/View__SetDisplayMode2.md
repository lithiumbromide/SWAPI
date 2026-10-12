---
title: "View::SetDisplayMode2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__SetDisplayMode2.htm"
---

# View::SetDisplayMode2

This method is obsolete and has been superseded by [View::SetDisplayMode3](sldworksAPI.chm::/View/View__SetDisplayMode3.htm).

Description

This method sets the display mode for this view.

Syntax (OLE Automation)

void = View.SetDisplayMode2 ( Mode, Facetted, Edges )

| Input: | (long) Mode | sw_WIREFRAME sw_HIDDEN_GREYED sw_HIDDEN |
| --- | --- | --- |
| Input: | (BOOL) Facetted | TRUE if the geometry is displayed faceted, FALSE if it is displayed exact |
| Input: | (BOOL) Edges | TRUE if edges are displayed when this view is in shaded mode, FALSE if not |
| Return: | (BOOL) retval | TRUE if the setting of the display mode was successful, FALSE if not |

Syntax (COM)

status = View->SetDisplayMode2 ( Mode, Facetted, Edges )

| Input: | (long) Mode | sw_WIREFRAME sw_HIDDEN_GREYED sw_HIDDEN |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) Facetted | TRUE if the geometry is displayed faceted, FALSE if it is displayed exact |
| Input: | (VARIANT_BOOL) Edges | TRUE if edges are displayed when this view is in shaded mode, FALSE if not |
| Output: | (VARIANT_BOOL) retval | TRUE if the setting of the display mode was successful, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The contents of a drawing view can be displayed in different modes, including Wireframe, HLR (Hidden Lines Removed), and HLV (Hidden Lines Visible), and Shaded. This is what the Mode argument indicates, and these values are contained in swDisplayMode_e. This enumeration also contains three other values , swFACETED_WIREFRAM, swFACETED_HIDDEN_GREY, and swFACETEDHIDDEN, which indicate faceted display of geometry. However, in this method, the Facetted argument is how faceted display is indicated, and if any of those three values are sued in the Mode argument, they will be treated the same as swWIREFRAME, sw_HIDDEN_GREY, and sw_HIDDEN, respectively.

| To determine if... | Then use... |
| --- | --- |
| Edges are displayed when this view is in shaded mode | View::GetDisplayEdgesInShadedMode |
| This view is display with faceted or precise geometry | View::GetFacettedHlrDisplay |
| The display mode of this drawing view | View::GetDisplayMode2 |

NOTE: Displaying geometry precisely can increase display quality, but can decrease performance. Setting the Facetted argument to TRUE can increase performance, but can decrease display quality.
