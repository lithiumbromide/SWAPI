---
title: "SimpleFilletFeatureData::GetFilletItemAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SimpleFilletFeatureData/SimpleFilletFeatureData__GetFilletItemAtIndex.htm"
---

# SimpleFilletFeatureData::GetFilletItemAtIndex

This method is obsolete and has been superseded by [SimpleFilletFeatureData2::GetFilletItemAtIndex](sldworksAPI.chm::/SimpleFilletFeatureData2/SimpleFilletFeatureData2__GetFilletItemAtIndex.htm).

Description

This method gets the fillet item at the specified index.

Syntax (OLE Automation)

pFilletItem = SimpleFilletFeatureData.GetFilletItemAtIndex ( index )

| Input: | (int) index | Index at which fillet item is required |
| --- | --- | --- |
| Return: | (LPDISPATCH) pFilletItem | Pointer to a dispatch object, the fillet item ( edge, face, loop, or NULL if the operation fails) |

Syntax (COM)

status = SimpleFilletFeatureData->IGetFilletItemAtIndex ( index, &pFilletItem )

| Input: | (int) index | Index at which fillet item is required |
| --- | --- | --- |
| Output: | (LPUNKNOWN) pFilletItem | Pointer to a dispatch object, the fillet item ( edge, face, loop, or NULL if the operation fails) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
