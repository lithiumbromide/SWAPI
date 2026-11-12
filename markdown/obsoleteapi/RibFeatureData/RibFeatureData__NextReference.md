---
title: "RibFeatureData::NextReference"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/RibFeatureData/RibFeatureData__NextReference.htm"
---

# RibFeatureData::NextReference

This method is obsolete and has been superseded by [RibFeatureData2::NextReference](sldworksAPI.chm::/RibFeatureData2/RibFeatureData2__NextReference.htm).

Description

For ribs with multiple contours, this method cycles through the possible sketch entities that can be used to define the Draft if it is used.

Syntax (OLE Automation)

Index = RibFeatureData.NextReference( )

| Return: | (int) Index | Index of the entity that is used |
| --- | --- | --- |

Syntax (COM)

status = RibFeatureData->NextReference( &Index)

| Output: | (int) Index | Index of the entity that is used |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method cycles through the entities. It starts at the beginning again once the last entity is reached.
