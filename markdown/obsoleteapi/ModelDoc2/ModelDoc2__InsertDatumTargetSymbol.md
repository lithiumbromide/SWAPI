---
title: "ModelDoc2::InsertDatumTargetSymbol"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertDatumTargetSymbol.htm"
---

# ModelDoc2::InsertDatumTargetSymbol

This method is obsolete and has been superseded by [ModelDocExtension::InsertDatumTargetSymbol2](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__InsertDatumTargetSymbol2.htm).

Description

This method creates a datum target symbol.

Syntax (OLE Automation)

retval = ModelDoc2.InsertDatumTargetSymbol ( datum1, datum2, datum3, areaStyle, areaOutside, value1, value2, valueStr1, valueStr2, arrowsSmart, arrowStyle, leaderLineStyle, leaderBent, showArea, showSymbol )

| Input: | (BSTR) datum1 | Datum reference string 1 |
| --- | --- | --- |
| Input: | (BSTR) datum2 | Datum reference string 2 |
| Input: | (BSTR) datum3 | Datum reference string 3 |
| Input: | (short) areaStyle | 0 = point 1 = circle 2 = rectangle |
| Input: | (VARIANT_BOOL) areaOutside | TRUE displays the target area dimensions size outside |
| Input: | (double) value1 | Numeric datum target area diameter or width |
| Input: | (double) value2 | Numeric datum target area height |
| Input: | (BSTR) valueStr1 | String value for datum target area diameter or width |
| Input: | (BSTR) valueStr2 | String value for datum target area height |
| Input: | (VARIANT_BOOL) arrowsSmart | TRUE uses smart arrows |
| Input: | (short) arrowStyle | Arrow head style as defined in swArrowStyle_e |
| Input: | (short) leaderLineStyle | Leaderline type as defined in swLeaderStyle_e |
| Input: | (VARIANT_BOOL) leaderBent | TRUE creates a bent leader line |
| Input: | (VARIANT_BOOL) showArea | TRUE shows the target area |
| Input: | (VARIANT_BOOL) showSymbol | TRUE displays the target symbol |
| Output: | (VARIANT_BOOL )retval | TRUE if created successfully; FALSE otherwise |

Syntax (COM)

status = ModelDoc2->InsertDatumTargetSymbol ( datum1, datum2, datum3, areaStyle, areaOutside, value1, value2, valueStr1, valueStr2, arrowsSmart, arrowStyle, leaderLineStyle, leaderBent, showArea, showSymbol, &retval )

| Input: | (BSTR) datum1 | Datum reference string 1 |
| --- | --- | --- |
| Input: | (BSTR) datum2 | Datum reference string 2 |
| Input: | (BSTR) datum3 | Datum reference string 3 |
| Input: | (short) areaStyle | 0 = point 1 = circle 2 = rectangle |
| Input: | (VARIANT_BOOL) areaOutside | TRUE displays the target area dimensions size outside |
| Input: | (double) value1 | Numeric datum target area diameter or width |
| Input: | (double) value2 | Numeric datum target area height |
| Input: | (BSTR) valueStr1 | String value for datum target area diameter or width |
| Input: | (BSTR) valueStr2 | String value for datum target area height |
| Input: | (VARIANT_BOOL) arrowsSmart | TRUE uses smart arrows |
| Input: | (short) arrowStyle | Arrow head style as defined in swArrowStyle_e |
| Input: | (short) leaderLineStyle | Leaderline type as defined in swLeaderStyle_e |
| Input: | (VARIANT_BOOL) leaderBent | TRUE creates a bent leader line |
| Input: | (VARIANT_BOOL) showArea | TRUE shows the target area |
| Input: | (VARIANT_BOOL) showSymbol | TRUE displays the target symbol |
| Output: | (VARIANT_BOOL) retval | TRUE if created successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
