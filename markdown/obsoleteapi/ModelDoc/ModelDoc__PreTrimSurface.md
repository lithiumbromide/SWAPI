---
title: "ModelDoc::PreTrimSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__PreTrimSurface.htm"
---

# ModelDoc::PreTrimSurface

This method is obsolete and has been superseded by [ModelDoc2::PreTrimSurface](sldworksAPI.chm::/ModelDoc2/ModelDoc2__PreTrimSurface.htm).

Description

This method sets the mutual trim option before trimming a surface.

Syntax (OLE Automation)

void ModelDoc.PreTrimSurface ( bMutualTrimIn)

| Input: | (BOOL) bMutualTrimIn | TRUE to use the mutual trim option, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->PreTrimSurface ( bMutualTrimIn )

| Input: | (VARIANT_BOOL) bMutualTrimIn | TRUE to use the mutual trim option, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
