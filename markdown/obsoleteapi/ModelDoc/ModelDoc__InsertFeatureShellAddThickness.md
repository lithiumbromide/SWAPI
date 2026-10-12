---
title: "ModelDoc::InsertFeatureShellAddThickness"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertFeatureShellAddThickness.htm"
---

# ModelDoc::InsertFeatureShellAddThickness

This method is obsolete and has been superseded by [ModelDoc2::InsertFeatureShellAddThickness](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertFeatureShellAddThickness.htm).

Description

This method adds thickness to a face in multi-thickness shell feature. This method modifies the behavior of ModelDoc::InsertFeatureShell so that a multi-thickness shell is created.

Syntax (OLE Automation)

void ModelDoc.InsertFeatureShellAddThickness ( thickness )

| Input: | (double) thickness | Shell thickness in meters |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->InsertFeatureShellAddThickness ( thickness )

| Input: | (double) thickness | Shell thickness in meters |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Make selections for the shell feature using SelectByMark with a mark number of 1 for the removed faces and 2 for the faces that have the alternate thicknesses. Call this function once for each of the faces that have selection with a mark of 2, then call ModelDoc::InsertFeatureShell.
