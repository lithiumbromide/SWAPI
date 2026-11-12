---
title: "ModelDoc2::InsertMacroFeature"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertMacroFeature.htm"
---

# ModelDoc2::InsertMacroFeature

This method is obsolete and has been superseded by [FeatureManager::InsertMacroFeature](../FeatureManager/FeatureManager__InsertMacroFeature.htm).

Description

This method inserts a macro feature into the model.

Syntax (OLE Automation)

retval = ModelDoc2.InsertMacroFeature ( cmdFile, cmdModule, cmdProcedure, paramNames, paramTypes, paramValues, pmFile, pmModule, pmProcedure )

| Input: | (BSTR) cmdFile | Macro file executed during feature regeneration |
| --- | --- | --- |
| Input: | (BSTR) cmdModule | Source module executed during feature regeneration |
| Input: | (BSTR) cmdProcedure | Source procedure executed during feature regeneration |
| Input: | (Variant) paramNames | Array of parameter names |
| Input: | (Variant) paramTypes | Array of parameter types as defined in swMacroFeatureParamType_e |
| Input: | (Variant) paramValues | Array of parameter values |
| Input: | (BSTR) pmFile | Macro file executed after edit definition is selected |
| Input: | (BSTR) pmModule | Source module executed after edit definition is selected |
| Input: | (BSTR) pmProcedure | Source procedure executed after edit definition is selected |
| Output: | (LPDISPATCH) retval | Pointer to macro feature |

Syntax (COM)

status = ModelDoc2->IInsertMacroFeature ( cmdFile, cmdModule, cmdProcedure, paramCount, paramNames, paramTypes, paramValues, pmFile, pmModule, pmProcedure, &retval )

| Input: | (BSTR) cmdFile | Macro file executed during feature regeneration |
| --- | --- | --- |
| Input: | (BSTR) cmdModule | Source module executed during feature regeneration |
| Input: | (BSTR) cmdProcedure | Source procedure executed during feature regeneration |
| Input: | (long) paramCount | Number of parameters |
| Input: | (BSTR) *paramNames | Array of size paramCount |
| Input: | (long) *paramTypes | Array of parameter types as defined in swMacroFeatureParamType_e of size paramCount |
| Input: | (BSTR) *paramValues | Array of size paramCount |
| Input: | (BSTR) pmFile | Macro file executed after edit definition is selected |
| Input: | (BSTR) pmModule | Source module executed after edit definition is selected |
| Input: | (BSTR) pmProcedure | Source procedure executed after edit definition is selected |
| Output: | (LPFEATURE) retval | Pointer to macro feature |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
