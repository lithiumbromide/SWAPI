---
title: "SimpleFilletFeatureData::SetRadius"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SimpleFilletFeatureData/SimpleFilletFeatureData__SetRadius.htm"
---

# SimpleFilletFeatureData::SetRadius

This method is obsolete and has been superseded by [SimpleFilletFeatureData2::SetRadius](sldworksAPI.chm::/SimpleFilletFeatureData2/SimpleFilletFeatureData2__SetRadius.htm).

Description

This method sets the radius value for specified fillet item.

Syntax (OLE Automation)

void SimpleFilletFeatureData.SetRadius ( pFilletItem, radius )

| Input: | (LPDISPATCH) pFilletItem | Pointer to a dispatch object, the fillet item for which the radius value is desired |
| --- | --- | --- |
| Input: | ( double ) radius | Radius value |

Syntax (COM)

status = SimpleFilletFeatureData->ISetRadius ( pFilletItem, radius )

| Input: | (LPUNKNOWN) pFilletItem | Pointer to an unknown object, the fillet item for which the radius value is desired |
| --- | --- | --- |
| Input: | ( double ) radius | Radius value |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To obtain a pointer to a fillet Item, see SimpleFilletFeatureData::GetFilletItemAtIndex and the SimpleFilletFeatureData::FilletItemsCount. Fillets can be made from multiple edges or faces and these methods get a pointer to any of the entities that helped to create the particular fillet and pass it into pFilletItem of this method.
