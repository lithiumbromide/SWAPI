---
title: "ModelDoc::AddRelation"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AddRelation.htm"
---

# ModelDoc::AddRelation

This method is obsolete and has been superseded by [ModelDoc2::AddRelation](../ModelDoc2/ModelDoc2__AddRelation.htm).

Description

This method adds a new relation. For example, to set the D2 dimension to be twice the value of the D1 dimension, you could use this method.

Syntax (OLE Automation)

void ModelDoc.AddRelation ( relStr)

| Input: | (BSTR) relStr | String containing the relationship to add |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->AddRelation ( relStr )

| Input: | (BSTR) relStr | String containing the relationship to add |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method adds a new relation. For example, to set the D2 dimension to be twice the value of the D1 dimension, you could specify this value for relStr:

"""D2@Sketch1"" = (""D1@Sketch1"" * 2)"
