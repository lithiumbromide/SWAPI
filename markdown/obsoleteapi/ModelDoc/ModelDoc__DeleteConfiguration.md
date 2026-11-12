---
title: "ModelDoc::DeleteConfiguration"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__DeleteConfiguration.htm"
---

# ModelDoc::DeleteConfiguration

This method is obsolete and has been superseded by [ModelDoc::DeleteConfiguration2](ModelDoc__DeleteConfiguration2.htm).

Description

This method deletes a configuration. The configuration you delete cannot be the active configuration.

Syntax (OLE Automation)

void ModelDoc.DeleteConfiguration ( configurationName)

| Input: | (BSTR) configurationName | Name of the configuration to delete |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->DeleteConfiguration ( configurationName )

| Input: | (BSTR) configurationName | Name of the configuration to delete |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
