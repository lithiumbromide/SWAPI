---
title: "Body::ISectionBySheet"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__ISectionBySheet.htm"
---

# Body::ISectionBySheet

This method is obsolete and has been superseded by [Body2::ISectionBySheet](sldworksAPI.chm::/Body2/Body2__ISectionBySheet.htm).

Description

This method sections a body using a sheet.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Body->ISectionBySheet ( Sheet, NumMaxSections, SectionedBodies, &retval )

| Input: | (LPBODY) Sheet | Pointer to the sheet body used to perform the section |
| --- | --- | --- |
| Input: | (long) NumMaxSections | Maximum number of sections created |
| Input: | (LPBODY*) SectionedBodies | Pointer to an array of bodies created during the section operation |
| Output: | (long) retval | Number of bodies created during the operation |
| Return: | (HRESULT)status | S_OK if successful |
