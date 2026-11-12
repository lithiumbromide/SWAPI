---
title: "ModelDoc::EditDatumTargetSymbol"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__EditDatumTargetSymbol.htm"
---

# ModelDoc::EditDatumTargetSymbol

This method is obsolete and has been superseded by [ModelDoc2::EditDatumTargetSymbol](sldworksAPI.chm::/ModelDoc2/ModelDoc2__EditDatumTargetSymbol.htm).

Description

This method edits a datum target symbol.

Syntax (OLE Automation)

retval = ModelDoc.EditDatumTargetSymbol ( datum1, datum2, datum3, areaStyle, areaOutside, value1, value2, valueStr1, valueStr2, arrowsSmart, arrowStyle, leaderLineStyle, leaderBent, showArea, showSymbol )

| Input: | (BSTR) datum1 | Datum reference string 1 |
| --- | --- | --- |
| Input: | (BSTR) datum2 | Datum reference string 2 |
| Input: | (BSTR) datum3 | Datum reference string 3 |
| Input: | (short) areaStyle | 0 = point, 1 = circle, 2 = rectangle |
| Input: | (BOOLEAN) areaOutside | TRUE to display target area dimensions size outside, FALSE otherwise |
| Input: | (double) value1 | Numeric datum target area diameter or width |
| Input: | (double) value2 | Numeric datum target area height |
| Input: | (BSTR) valueStr1 | Datum target area diameter or width |
| Input: | (BSTR) valueStr2 | Datum target area height |
| Input: | (BOOLEAN) arrowsSmart | TRUE if you want smart arrows, FALSE otherwise |
| Input: | (short) arrowStyle | Arrow head style for example, open, closed, and so on) as defined in swArrowStyle_e |
| Input: | (short) leaderLineStyle | Leader line type as defined in swLeaderStyle_e |
| Input: | (BOOLEAN) leaderBent | TRUE if you want a bent leader line, FALSE otherwise |
| Input: | (BOOLEAN) showArea | TRUE if you want to show the target area, FALSE otherwise |
| Input: | (BOOLEAN) showSymbol | TRUE if you want to display the target symbol, FALSE otherwise |
| Return: | (BOOLEAN) retval | TRUE if symbol was edited successfully |

Syntax (COM)

status = ModelDoc->EditDatumTargetSymbol ( datum1, datum2, datum3, areaStyle, areaOutside, value1, value2, valueStr1, valueStr2, arrowsSmart, arrowStyle, leaderLineStyle, leaderBent, showArea, showSymbol, &retval )

| Input: | (BSTR) datum1 | Datum reference string 1 |
| --- | --- | --- |
| Input: | (BSTR) datum2 | Datum Reference string 2 |
| Input: | (BSTR) datum3 | Datum reference string 3 |
| Input: | (short) areaStyle | 0 = point, 1 = circle, 2 = rectangle |
| Input: | (VARIANT_BOOL) areaOutside | TRUE to display target area dimensions size outside, FALSE otherwise |
| Input: | (double) value1 | Numeric datum target area diameter or width |
| Input: | (double) value2 | Numeric datum target area height |
| Input: | (BSTR) valueStr1 | Datum target area diameter or width |
| Input: | (BSTR) valueStr2 | Datum target area height |
| Input: | (VARIANT_BOOL) arrowsSmart | TRUE if you want smart arrows, FALSE otherwise |
| Input: | (short) arrowStyle | Arrow head style (for example, open, closed, and so on.) as defined in swArrowStyle_e |
| Input: | (short) leaderLineStyle | Leader line type as defined in swLeaderStyle_e |
| Input: | (VARIANT_BOOL) leaderBent | TRUE if you want a bent leader line, FALSE otherwise |
| Input: | (VARIANT_BOOL) showArea | TRUE if you want to show the target area, FALSE otherwise |
| Input: | (VARIANT_BOOL) showSymbol | TRUE if you want to display the target symbol, FALSE otherwise |
| Output: | (VARIANT_BOOL) retval | TRUE if symbol was edited successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
