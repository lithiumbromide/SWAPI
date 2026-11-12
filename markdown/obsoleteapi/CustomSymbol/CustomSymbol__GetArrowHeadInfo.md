---
title: "CustomSymbol::GetArrowHeadInfo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetArrowHeadInfo.htm"
---

# CustomSymbol::GetArrowHeadInfo

This method is obsolete and has been superseded by [Note::GetArrowHeadInfo](sldworksAPI.chm::/Note/Note__GetArrowHeadInfo.htm).

Description

This method gets the arrow head information for this symbol.

Syntax (OLE Automation)

retval = CustomSymbol.GetArrowHeadInfo ( )

| Return: | (VARIANT) retval | VARIANT of type SafeArray of doubles (see below) |
| --- | --- | --- |

Syntax (COM)

status = CustomSymbol->IGetArrowHeadInfo ( &retval )

| Output: | (double*)retval | Pointer to array of doubles (see below) |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if Successful |

Remarks

This method returns an array of doubles that describe the geometry of the arrowhead on the far end of the leader line. Note that this information is independent of whether this SFSymbol has an arrowhead.

Format of return information is the following array of doubles:

retval[0] = Arrow length (leader into arrowhead)

retval[1] = Arrowhead length

retval[2] = Arrowhead width

retval[3] = Arrowhead style as defined in swArrowStyle_e
