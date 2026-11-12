---
title: "DrawingDoc::InsertSurfaceFinishSymbol"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__InsertSurfaceFinishSymbol.htm"
---

# DrawingDoc::InsertSurfaceFinishSymbol

This method is obsolete and has been superseded by [ModelDoc2::InsertSurfaceFinishSymbol2](../ModelDoc2/ModelDoc2__InsertSurfaceFinishSymbol2.htm).

Description

This method creates a surface finish symbol based on the last selection.

Syntax (OLE Automation)

retval = DrawingDoc.InsertSurfaceFinishSymbol ( symType, leaderType, locX, locY, locZ, laySymbol, arrowType, machAllowance, otherVals, prodMethod, sampleLen, maxRoughness, minRoughness, roughnessSpacing)

| Input: | (long) symType | Symbol type as defined in swSFSymType_e |
| --- | --- | --- |
| Input: | (long) leaderType | Leader type as defined in swLeaderStyle_e |
| Input: | (double) locX | X location for symbol |
| Input: | (double) locY | Y location for symbol |
| Input: | (double) locZ | Z location for symbol |
| Input: | (long) laySymbol | Direction of lay as defined in swSFLaySym_e |
| Input: | (long) arrowStyle | Arrowhead type as defined in swArrowStyle_e |
| Input: | (BSTR) machAllowance | Material removal allowance |
| Input: | (BSTR) otherVals | Other roughness values |
| Input: | (BSTR) prodMethod | Production method/treatment |
| Input: | (BSTR) sampleLen | Sampling length |
| Input: | (BSTR) maxRoughness | Maximum roughness |
| Input: | (BSTR) minRoughness | Minimum roughness |
| Input: | (BSTR) roughnessSpacing | Roughness spacing |
| Return: | (BOOL) retval | TRUE if the finish symbol was inserted successfully, FALSE if not |

Syntax (COM)

status = DrawingDoc->InsertSurfaceFinishSymbol ( symType, leaderType, locX, locY, locZ, laySymbol, arrowType, machAllowance, otherVals, prodMethod, sampleLen, maxRoughness, minRoughness, roughnessSpacing, &retval )

| Input: | (long) symType | Symbol type as defined in swSFSymType_e |
| --- | --- | --- |
| Input: | (long) leaderType | Leader type as defined in swLeaderStyle_e |
| Input: | (double) locX | X location for symbol |
| Input: | (double) locY | Y location for symbol |
| Input: | (double) locZ | Z location for symbol |
| Input: | (long) laySymbol | Direction of lay as defined in swSFLaySym_e |
| Input: | (long) arrowStyle | Arrowhead type as defined in swArrowStyle_e |
| Input: | (BSTR) machAllowance | Material removal allowance |
| Input: | (BSTR) otherVals | Other roughness values |
| Input: | (BSTR) prodMethod | Production method/treatment |
| Input: | (BSTR) sampleLen | Sampling length |
| Input: | (BSTR) maxRoughness | Maximum roughness |
| Input: | (BSTR) minRoughness | Minimum roughness |
| Input: | (BSTR) roughnessSpacing | Roughness spacing |
| Output: | (VARIANT_BOOL) retval | TRUE if the finish symbol was inserted successfully, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
