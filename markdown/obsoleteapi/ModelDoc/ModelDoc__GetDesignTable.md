---
title: "ModelDoc::GetDesignTable"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetDesignTable.htm"
---

# ModelDoc::GetDesignTable

This method is obsolete and has been superseded by [ModelDoc2::GetDesignTable](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetDesignTable.htm).

Description

This method returns the DesignTable object associated with this part or assembly document.

Syntax (OLE Automation)

retval = ModelDoc.GetDesignTable ( )

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the DesignTable object |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IGetDesignTable ( &retval )

| Output: | (LPDESIGNTABLE) retval | Pointer to the DesignTable object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If this method called from a drawing document, NULL ise returned. To access design tables from a drawing document you must get the ModelDoc object associated with a particular drawing view, and then call this method from that ModelDoc object. To determine if a drawing view has a design table associated with it, use View::HasDesignTable.
