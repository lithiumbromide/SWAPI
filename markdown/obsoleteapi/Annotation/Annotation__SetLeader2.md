---
title: "Annotation::SetLeader2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Annotation/Annotation__SetLeader2.htm"
---

# Annotation::SetLeader2

This method is obsolete and has been superseded by [Annotation::SetLeader3](sldworksAPI.chm::/Annotation/Annotation__SetLeader3.htm).

Description

This method sets the leader display characteristics for this annotation.

Syntax (OLE Automation)

retval = Annotation.SetLeader2 ( leader, leaderSide, smartArrowHeadStyle, bentLeader, perpendicular, allAround )

| Input: | (BOOL) leader | TRUE to enable leader display, FALSE to disable it |
| --- | --- | --- |
| Input: | (long) leaderSide | Leader side as defined in swLeaderSide_e |
| Input: | (BOOL) smartArrowHeadStyle | TRUE to enable smart arrowhead style, False to disable it |
| Input: | (BOOL) bentLeader | TRUE to enable bent leader display, FALSE to disable it |
| Input: | (BOOL) perpendicular | TRUE to enable perpendicular bent leader display, FALSE to disable it |
| Input: | (BOOL) allArround | TRUE to enable all around symbol display, FALSE to disable it |
| Return: | (long) retval | Indication whether the operation was successful (see Remarks ) |

Syntax (COM)

status = Annotation->SetLeader2 ( leader, leaderSide, smartArrowHeadStyle, bentLeader, perpendicular, allAround, &retval )

| Input: | (VARIANT_BOOL) leader | TRUE to enable leader display, FALSE to disable it |
| --- | --- | --- |
| Input: | (long) leaderSide | Leader side as defined in swLeaderSide_e |
| Input: | (VARIANT_BOOL) smartArrowHeadStyle | TRUE to enable smart arrowhead style, FALSE to disable it |
| Input: | (VARIANT_BOOL) bentLeader | TRUE to enable bent leader display, FALSE to disable it |
| Input: | (VARIANT_BOOL) perpendicular | True to enable perpendicular bent leader display, FALSE to disable it |
| Input: | (VARIANT_BOOL) allArround | TRUE to enable all around symbol display, FALSE to disable it |
| Output: | (long) retval | Indication whether the operation was successful (see Remarks ) |
| Return: | (HRESULT) status | S_OK if successfu |

Remarks

These parameters are characteristics of the annotation, not individual leaders, and you can get or set them whether or not leaders are displayed.

| Use... | To... |
| --- | --- |
| Annotation::GetLeader | Determine whether leader display is enabled or disabled |
| Annotation::GetLeaderSide | Get the leader attachment side setting |
| Annotation::GetSmartArrowHeadStyle | Determine whether smart arrowhead style is enabled or disabled |
| Annotation::GetBentLeader | Determine whether bent leader display is enabled or disabled |
| Annotation::GetLeaderPerpendicular | Determine whether perpendicular bent leader display is enabled or disabled |
| Annotation::GetLeaderAllAround | Determine whether all around symbol display is enabled or disabled |

You can set the leader side, smart arrowhead style, and bent leader values at any time. However, if leader display is disabled, you cannot affect the display of the annotation by setting these values. You can also set the perpendicular bent leader and all around symbol display at any time, but if bent leaders are disabled, you cannot affect the display of the annotation by setting these values.

The return status of this operation can have the following values:

| 0 | Leader characteristics were successfully set |
| --- | --- |
| -1 | Leader characteristics were not set because of an unknown error |
| -2 | Leader attachment side setting is invalid |
| -3 | Leaders are not supported on this type of annotation |
| -4 | Leaders cannot be disabled on this type of annotation |
| -5 | Bent leaders cannot be disabled on this type of annotation |

If leader display is enabled, then this method changes the visible model. To see those changes, the graphics window must be redrawn using ModelDoc2::GraphicsRedraw2.
