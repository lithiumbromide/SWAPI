---
title: "ModelDoc::InsertDome"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertDome.htm"
---

# ModelDoc::InsertDome

This method is obsolete and has been superseded by [ModelDoc2::InsertDome](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertDome.htm).

Description

This method inserts a dome.

Syntax (OLE Automation)

void ModelDoc.InsertDome ( height, reverseDir, doEllipticSurface)

| Input: | (double) height | Height for the dome in meters |
| --- | --- | --- |
| Input: | (BOOL) reverseDir | TRUE if you want to reverse the dome direction, FALSE otherwise |
| Input: | (BOOL) doEllipticSurface | TRUE if you want the dome to be an elliptical surface, FALSE otherwise |

Syntax (COM)

status = ModelDoc->InsertDome ( height, reverseDir, doEllipticSurface )

| Input: | (double) height | Hheight for the dome in meters |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) reverseDir | TRUE if you want to reverse the dome direction, FALSE otherwise |
| Input: | (VARIANT_BOOL) doEllipticSurface | TRUE if you want the dome to be an elliptical surface, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
