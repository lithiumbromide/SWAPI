---
title: "PartDoc::ForceRebuild"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__ForceRebuild.htm"
---

# PartDoc::ForceRebuild

This method is obsolete and has been superseded by [ModelDoc2::ForceRebuild3](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ForceRebuild3.htm).

Description

This method forces a rebuild of the entire part. This is equivalent to interactively pressing Ctrl-Q.

Syntax (OLE Automation)

void PartDoc.ForceRebuild ()

Syntax (COM)

status = PartDoc->ForceRebuild ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

This command rebuilds every piece of your model regardless of whether or not it needs to be rebuilt. This operation may take a long time.
