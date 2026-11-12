---
title: "ModelDoc::IsOpenedViewOnly"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__IsOpenedViewOnly.htm"
---

# ModelDoc::IsOpenedViewOnly

This method is obsolete and has been superseded by [ModelDoc2::IsOpenedViewOnly](sldworksAPI.chm::/ModelDoc2/ModelDoc2__IsOpenedViewOnly.htm).

Description

This method determines if a SolidWorks document is open in view-only mode.

Syntax (OLE Automation)

retval = ModelDoc.IsOpenedViewOnly ( )

| Return: | (Boolean)retval | TRUE if this document is view-only, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IsOpenedViewOnly ( &retval )

| Output: | (VARIANT_BOOL)retval | TRUE if this document is view-only, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

SolidWorks loads files using multi-threading. When a file is being loaded, the graphics are displayed immediately and the user is able to perform certain zoom and pan functions. If the view is shaded, you also have the option to rotate the view. Until all data and references have been loaded, the file is in view-only mode. Also, a file can be in view-only mode if the user has chosen to load the file for viewing purposes. A user can do this by selecting File, Open and toggling the view-only button to on. Your application should check for view-only mode to determine how to proceed.

When a file is in view-only mode, many API queries will return NULL or empty data.
