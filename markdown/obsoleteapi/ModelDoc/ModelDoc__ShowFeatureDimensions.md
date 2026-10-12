---
title: "ModelDoc::ShowFeatureDimensions"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ShowFeatureDimensions.htm"
---

# ModelDoc::ShowFeatureDimensions

This method is obsolete and has been superseded by [ModelDoc2::ShowFeatureDimensions](../ModelDoc2/ModelDoc2__ShowFeatureDimensions.htm).

Description

This method causes all of the dimension of the selected feature to be displayed in this document.

Syntax (OLE Automation)

void ModelDoc.ShowFeatureDimensions ( )

Syntax (COM)

status = ModelDoc->ShowFeatureDimensions ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

This method only applies to part and assembly documents; it has no effect if used in a drawing document.
