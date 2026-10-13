---
title: "Mate::GetMateDimensionValue"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Mate/Mate__GetMateDimensionValue.htm"
---

# Mate::GetMateDimensionValue

This method is obsolete and has been superseded by [Mate2::DisplayDimension2](sldworksAPI.chm::/Mate2/Mate2__DisplayDimension2.htm).

Description

This method gets the mate dimension value. This value is either a distance in meters or an angle in radians based on the mate type. If this mate does not support a dimensional value, then 0 is returned.

Syntax (OLE Automation)

retval = Mate.GetMateDimensionValue ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray, which is an array of one double containing the dimensional value for this mate; this value is either a distance in meters or an angle in radians based on the mate type |
| --- | --- | --- |

Syntax (COM)

status = Mate->IGetMateDimensionValue ( &dimValue )

| Output: | (double) dimValue | Pointer to a double containing the dimensional value for this mate; this value is either a distance in meters or an angle in radians based on the mate type |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

To determine the mate type, see Mate::GetMateParams.
