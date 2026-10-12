---
title: "FeatureManager::InsertMacroFeature"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__InsertMacroFeature.htm"
---

# FeatureManager::InsertMacroFeature

This method is obsolete and has been superseded by [FeatureManager::InsertMacroFeature2](FeatureManager__InsertMacroFeature2.htm).

Description

This method inserts a macro feature in this model.

Syntax (OLE Automation)

retval = FeatureManager.InsertMacroFeature ( baseName, progId, macroMethods, paramNames, paramTypes, paramValues, editBody, options )

| Input: | (BSTR) baseName | Name of the base feature (see Remarks ) |
| --- | --- | --- |
| Input: | (BSTR) progId | Indicates whether to use COM or VBA callback methods (see Remarks ) |
| Input: | (VARIANT) macroMethods | Array of size 9 in string (see Remarks ) |
| Input: | (VARIANT) paramNames | Array of parameters of size paramCount |
| Input: | (VARIANT) paramTypes | Array of types of parameters of size paramCount as defined by swMacroFeatureParamType_e in long |
| Input: | (VARIANT) paramValues | Array of values of parameters of size paramCount in string |
| Input: | (LPBODY2) editBody | Body to modify in the macro feature |
| Input: | (long) options | Placement of the macro feature in the FeatureManager design tree as defined by swMacroFeatureOptions_e |
| Output: | (LPFEATURE) retval | Pointer to the macro feature |

Syntax (COM)

status = FeatureManager->IInsertMacroFeature ( baseName, progId, macroMethods, paramCount, paramNames, paramTypes, paramValues, editBody, options, &retval )

| Input: | (BSTR) baseName | Name of the base feature (see Remarks ) |
| --- | --- | --- |
| Input: | (BSTR) progId | Indicates whether to use COM or VBA callback methods (see Remarks ) |
| Input: | (BSTR) *macroMethods | Array of size 9 in string (see Remarks ) |
| Input: | (long) paramCount | Number of parameters |
| Input: | (BSTR) *paramNames | Array of parameters of size paramCount |
| Input: | (long) *paramTypes | Array of types of parameters of size paramCount as defined by swMacroFeatureParamType_e in long |
| Input: | (BSTR) *paramValues | Array of values of parameters of size paramCount in string |
| Input: | (LPBODY2) editBody | Body to modify in the macro feature |
| Input: | (long) options | Placement of the macro feature in the FeatureManager design tree as defined by swMacroFeatureOptions_e |
| Output: | (LPFEATURE) retval | Pointer to the macro feature |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

baseName

- The argument baseName is serialized within the feature and cannot be changed.
- You can find out the name of the base feature by using MacroFeatureData::GetBaseName.
- The baseName argument is also used to generate the name of the feature when the feature is first created.

ProgId

| To create a macro feature using the OLE version from VB or VBA... | Then the input arguments should be... |
| --- | --- |
| COM callback methods | InsertMacroFeature ( progId, empty, ... ) |
| VBA callback methods | InsertMacroFeature ( "", callBackkMethods ... ) |

The progId argument is the name of the program ID for the component that implements the COM callback methods.

macroMethods

The macroMethods argument is implemented from VBA only and is a nine (9) element array of strings consisting of the following values:

Filename should be the full pathname to the macro file. If the procedures are all self-contained in the same macro file that calls FeatureManager::InsertMacroFeature, then a call to SldWorks::GetCurrentMacroPathName will provide all of the information necessary for the Filename.

If a security procedure is not used, then Filename, Module, and Procedure must all be empty strings.

Procedure names must have an swm prefix in the name. This prefix identifies the procedures to execute.

See Overview of Programming Macro Features for additional information about declaring procedures.
