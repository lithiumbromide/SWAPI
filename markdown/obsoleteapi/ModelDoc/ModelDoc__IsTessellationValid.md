---
title: "ModelDoc::IsTessellationValid"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__IsTessellationValid.htm"
---

# ModelDoc::IsTessellationValid

This method is obsolete and has been superseded by [ModelDoc2::IsTessellationValid](sldworksAPI.chm::/ModelDoc2/ModelDoc2__IsTessellationValid.htm).

Description

This method is designed to work in coordination with Face2::IGetFacetData to determine if the current set of facets is valid.

Syntax (OLE Automation)

retval = ModelDoc.IsTessellationValid ( )

| Return: | (BOOL) retval | TRUE if the facet data is valid, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IsTessellationValid ( &retval )

| Return: | (VARIANT_BOOL) retval | TRUE if the facet data is valid, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is used to capture operations that invalidate the current set of facets, yet does not send a RegenNotify event. For example, if the user changes the rendering tolerance, the RegenNotify event would not be sent, yet the current set of facets would be invalid. However, this action would trigger a SolidWorks RepaintNotify from where you could call this mehtod before attempting to use your current set of facet data.

If FALSE is returned from IsTessellationValid, then valid facet information would not be available until SolidWorks completes a repaint operation (RepaintPostNotify). In other words, SolidWorks does not have any valid facet information at this time, and any facet data obtained in earlier calls is invalid. Not until the repaint operation is complete (RepaintPostNotify) can you call IGetFacetData again. As a result, the user would see a flash of SolidWorks tessellation in the graphics window before your application would be able to obtain the facet data again and redraw it to the SolidWorks display.

See Face2::IGetFacetData for more information.
