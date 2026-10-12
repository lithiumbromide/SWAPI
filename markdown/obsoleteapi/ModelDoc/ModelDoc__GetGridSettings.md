---
title: "ModelDoc::GetGridSettings"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetGridSettings.htm"
---

# ModelDoc::GetGridSettings

This method is obsolete and has been superseded by [ModelDoc2::GetGridSettings](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetGridSettings.htm).

Description

This method gets the current grid settings.

Syntax (OLE Automation)

retval = ModelDoc.GetGridSettings ()

| Return: | (VARIANT) retval | Current grid settings |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetGridSettings ( &retval )

| Output: | (VARIANT) retval | Ccurrent grid settings |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return format is the following array of doubles:

[ dispGrid, gridSpacing, snap, dotStyle, nMajor, nMinor, angleSnap, angleUnit, minorAuto ]

where:

dispGrid - TRUE if grid displayed, FALSE if not

gridSpacing - snap distance

snap - TRUE if snap to grid is on, FALSE if not

dotStyle - TRUE if dotted grids, FALSE if not

nMajor - number of minors in major

nMinor - number of snaps in minor

angleSnap - TRUE if snap to angle is on, FALSE if not

angleUnit - value of angle to which to snap

minorAuto - TRUE if the minor grids are set automatically, FALSE if not
