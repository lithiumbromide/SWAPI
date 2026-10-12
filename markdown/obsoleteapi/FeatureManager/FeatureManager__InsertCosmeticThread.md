---
title: "FeatureManager::InsertCosmeticThread"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__InsertCosmeticThread.htm"
---

# FeatureManager::InsertCosmeticThread

This method is obsolete and has been superseded by [FeatureManager::InsertCosmeticThread2](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertCosmeticThread2.htm).

Description

This method inserts a cosmetic thread.

Syntax (OLE Automation)

retval = FeatureManager.InsertCosmeticThread ( type, depth, length, note )

| Input: | (short) type | Type as defined in swCosmeticThreadType_e |
| --- | --- | --- |
| Input: | (double) depth | Diameter of the cosmetic thread |
| Input: | (double) length | Length of the cosmetic thread |
| Input: | (BSTR) note | Callout text to display in the drawing document |
| Output: | (BSTR) retval | Name of the cosmetic thread feature |

Syntax (COM)

status = FeatureManager->InsertCosmeticThread ( type, depth, length, note, &retval )

| Input: | (short) type | Type as defined in swCosmeticThreadType_e |
| --- | --- | --- |
| Input: | (double) depth | Diameter of the cosmetic thread |
| Input: | (double) length | Length of the cosmetic thread |
| Input: | (BSTR) note | Callout text to display in the drawing document |
| Output: | (BSTR) retval | Name of the cosmetic thread feature |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method returns the name of the cosmetic thread feature, which you can use to retrieve the cosmetic thread feature in a part or assembly or the cosmetic thread annotation in a drawing.

| In a... | You... |
| --- | --- |
| Part - or - Assembly | Use PartDoc::FeatureByName - or - Use AssemblyDoc::FeatureByName |
| Drawing | Search through the cosmetic threads of the drawing views for the annotation by that name using Annotation::GetName |
