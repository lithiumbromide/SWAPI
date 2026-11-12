---
title: "DrawingDoc::CreateSectionViewAt3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateSectionViewAt3.htm"
---

# DrawingDoc::CreateSectionViewAt3

This method is obsolete and has been superseded by [DrawingDoc::CreateSectionView4](sldworksAPI.chm::/DrawingDoc/DrawingDoc__CreateSectionViewAt4.htm).

Description

This method creates a section view at the specified location on the drawing.

Syntax (OLE Automation)

retval = DrawingDoc.CreateSectionViewAt3 ( x, y, z, notAligned, isOffsetSection, label, chgdirection, scwithmodel, partial, dispsurfcut, excludedComponents)

| Input: | (double) x | X position on the drawing sheet for the center of the drawing view |
| --- | --- | --- |
| Input: | (double) y | Y position on the drawing sheet for the center of the drawing view |
| Input: | (double) z | Z position on the drawing sheet for the center of the drawing view |
| Input: | (VARIANT_BOOL) notAligned | TRUE breaks the alignment from the parent view, FALSE snaps into alignment with the parent view |
| Input: | (VARIANT_BOOL) isOffsetSection | TRUE creates an aligned section view (two lines at an angle), FALSE creates a normal projection section view |
| Input: | (BSTR) label | String containing the letter for the label for this section view |
| Input: | (VARIANT_BOOL) chgdirection | TRUE changes the direction of this section view, FALSE does not |
| Input: | (VARIANT_BOOL) scwithmodel | TRUE scales the section view with the model, FALSE does not |
| Input: | (VARIANT_BOOL) partial | TRUE displays a partial section view, FALSE does not |
| Input: | (VARIANT_BOOL) dispsurfcut | TRUE if only the surfaces cut by the section line are to appear in the section view, FALSE if not |
| Input: | (VARIANT) excludedComponents | Array of components to exclude from section view |
| Output: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created View object |

Syntax (COM)

status = DrawingDoc->ICreateSectionViewAt3 ( x, y, z, notAligned, isOffsetSection, label, chgdirection, scwithmodel, partial, dispsurfcut, numExcludedComponents, pExcludedComponents, &retval)

| Input: | (double) x | X position on the drawing sheet for the center of the drawing view |
| --- | --- | --- |
| Input: | (double) y | Y position on the drawing sheet for the center of the drawing view |
| Input: | (double) z | Z position on the drawing sheet for the center of the drawing view |
| Input: | (VARIANT_BOOL) notAligned | TRUE breaks the alignment from the parent view, FALSE snaps into alignment with the parent view |
| Input: | (VARIANT_BOOL) isOffsetSection | TRUE creates an aligned section view (two lines at an angle), FALSE creates a normal projection section view |
| Input: | (BSTR) label | String containing the letter for the label for this section view |
| Input: | (VARIANT_BOOL) chgdirection | TRUE changes the direction of this section view, FALSE does not |
| Input: | (VARIANT_BOOL) scwithmodel | TRUE scales the section view with the model, FALSE does not |
| Input: | (VARIANT_BOOL) partial | TRUE displays a partial section view, FALSE does not |
| Input: | (VARIANT_BOOL) dispsurfcut | TRUE if only the surfaces cut by the section line are to appear in the section view, FALSE if not |
| Input: | (long) numExcludedComponents | Number of excluded components in this section view |
| Input: | (LPDISPATCH) pExcludedComponents | Array of components to exclude from section view |
| Output: | (LPVIEW) retval | Pointer the newly created View object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Select the section line or the lines to use as a section line before calling this method.

This method runs silently; the end-user is not prompted for a label.

Use View::GetSection to get the DrSection object, and use DrSection::SetLabel2 to set the name for the label, which provides a warning if the name is a duplicate and the standard does not accept duplicate names.
