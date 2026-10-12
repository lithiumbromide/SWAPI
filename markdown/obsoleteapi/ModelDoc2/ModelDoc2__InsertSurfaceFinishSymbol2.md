---
title: "ModelDoc2::InsertSurfaceFinishSymbol2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertSurfaceFinishSymbol2.htm"
---

# ModelDoc2::InsertSurfaceFinishSymbol2

This method is obsolete and has been superseded by [ModelDocExtension::InsertSurfaceFinishSymbol3](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__InsertSurfaceFinishSymbol3.htm).

Description

This method creates a surface-finish symbol based on the last selection.

Syntax (OLE Automation)

retval = ModelDoc2.InsertSurfaceFinishSymbol2 ( symType, leaderType, locX, locY, locZ, laySymbol, arrowType, machAllowance, otherVals, prodMethod, sampleLen, maxRoughness, minRoughness, roughnessSpacing)

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
| Input: | (BSTR) prodMethod | Production method and treatment |
| Input: | (BSTR) sampleLen | Sampling length |
| Input: | (BSTR) maxRoughness | Maximum roughness |
| Input: | (BSTR) minRoughness | Minimum roughness |
| Input: | (BSTR) roughnessSpacing | Roughness spacing |
| Return: | (BOOL) retval | TRUE if the finish symbol is inserted successfully, FALSE otherwise |

Syntax (COM)

status = ModelDoc2->InsertSurfaceFinishSymbol2 ( symType, leaderType, locX, locY, locZ, laySymbol, arrowType, machAllowance, otherVals, prodMethod, sampleLen, maxRoughness, minRoughness, roughnessSpacing, &retval )

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
| Output: | (VARIANT_BOOL) retval | TRUE if the finish symbol is inserted successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The SolidWorks software uses the location parameters for this method only if the surface finish symbol has a leader – leaderType != swNO_LEADER.
