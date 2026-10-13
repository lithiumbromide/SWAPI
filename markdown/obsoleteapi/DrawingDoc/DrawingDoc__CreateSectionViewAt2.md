---
title: "DrawingDoc::CreateSectionViewAt2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateSectionViewAt2.htm"
---

# DrawingDoc::CreateSectionViewAt2

This method is obsolete and has been superseded by [DrawingDoc::CreateSectionViewAt3](DrawingDoc__CreateSectionViewAt3.htm).

Description

This method creates a new section view at a given location on the drawing.

Syntax (OLE Automation)

retval = DrawingDoc.CreateSectionViewAt2 ( x, y, z, notAligned, isOffsetSection, label, chgdirection, scwithmodel, partial, dispsurfcut )

| Input: | (double) x | X position on the drawing sheet for the center of the drawing view |
| --- | --- | --- |
| Input: | (double) y | Y position on the drawing sheet for the center of the drawing view |
| Input: | (double) z | Z position on the drawing sheet for the center of the drawing view |
| Input: | (BOOL) notAligned | TRUE breaks the alignment from the parent view, FALSE snaps into alignment with the parent view |
| Input: | (BOOL) isOffsetSection | TRUE creates an aligned section (two lines at an angle), FALSE creates a normal projection section view |
| Input: | (BSTR) label | String value containing the label name of this section view |
| Input: | (BOOL) chgdirection | TRUE changes the direction of this section view, FALSE does not |
| Input: | (BOOL) switchmodel | TRUE scales the section view with the model, FALSE does not |
| Input: | (BOOL) partial | TRUE displays a partial section view, FALSE does not |
| Input: | (BOOL) dispsurfcut | TRUE displays only the surface cut, FALSE does not |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created View object |

Syntax (COM)

status = DrawingDoc->ICreateSectionViewAt2 ( x, y, z, notAligned, isOffsetSection, label, chgdirection, scwithmodel, partial, dispsurfcut, &retval )

| Input: | (double) x | X position on the drawing sheet for the center of the drawing view |
| --- | --- | --- |
| Input: | (double) y | Y position on the drawing sheet for the center of the drawing view |
| Input: | (double) z | Z position on the drawing sheet for the center of the drawing view |
| Input: | (VARIANT_BOOL) notAligned | TRUE breaks the alignment from the parent view, FALSE snaps into alignment with the parent view |
| Input: | (VARIANT_BOOL) isOffsetSection | TRUE creates an aligned section (two lines at an angle), FALSE creates a normal projection section view |
| Input: | (BSTR) label | String value containing the label name of this section view |
| Input: | (VARIANT_BOOL) chgdirection | TRUE changes the direction of this section view, FALSE does not |
| Input: | (VARIANT_BOOL) switchmodel | TRUE scales the section view with the model, FALSE does not |
| Input: | (VARIANT_BOOL) partial | TRUE displays a partial section view, FALSE does not |
| Input: | (VARIANT_BOOL) dispsurfcut | TRUE displays only the surface cut, FALSE does not |
| Output: | (LPVIEW) retval | Point to the newly View object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method runs silently; the end-user is not prompted for label. Then use View::GetSection to get the DrSection object, and use DrSection::SetLabel2 to set the label, which provides a warning if the name is a duplicate and the standard does not accept duplicate names.
