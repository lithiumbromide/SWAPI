---
title: "DrSection::SetLabel"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrSection/DrSection__SetLabel.htm"
---

# DrSection::SetLabel

This method is obsolete and has been superseded by [DrSection::SetLabel2](sldworksAPI.chm::/DrSection/DrSection__SetLabel2.htm).

Description

This method sets the label for this section cut.

Syntax (OLE Automation)

labelSet = DrSection.SetLabel ( label )

| Input: | ( BSTR ) label | Label for this section cut |
| --- | --- | --- |
| Return: | (BOOL) labelSet | TRUE if label was successfully set, FALSE if not |

Syntax (COM)

status = DrSection->SetLabel ( label, &labelSet )

| Input: | (BSTR ) label | Label for this section cut |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) labelSet | TRUE if label was successfully set, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
