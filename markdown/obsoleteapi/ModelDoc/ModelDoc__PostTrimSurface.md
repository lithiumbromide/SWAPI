---
title: "ModelDoc::PostTrimSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__PostTrimSurface.htm"
---

# ModelDoc::PostTrimSurface

This method is obsolete and has been superseded by [ModelDoc2::PostTrimSurface](sldworksAPI.chm::/ModelDoc2/ModelDoc2__PostTrimSurface.htm).

Description

This method sets the option for the trim surface post-process type.

Syntax (OLE Automation)

void ModelDoc.PostTrimSurface ( bSewSurfaceIn)

| Input: | (BOOL) bSewSurfaceIn | TRUE if you want to use the sew surface in option, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->PostTrimSurface ( bSewSurfaceIn )

| Input: | (VARIANT_BOOL) bSewSurfaceIn | TRUE if you want to use the sew surface in option, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
