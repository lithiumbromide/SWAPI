---
title: "ModelDoc2::GetMassProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__GetMassProperties.htm"
---

# ModelDoc2::GetMassProperties

This method is obsolete and has be superseded by [ModelDoc2::GetMassProperties2](ModelDoc2__GetMassProperties2.htm),

Description

This method returns the mass properties of the current part or assembly.

Syntax (OLE Automation)

retval = ModelDoc2.GetMassProperties ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray of doubles |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->IGetMassProperties ( mPropsData, &retval )

| Input: | (double) mPropsData | Pointer to an array of doubles |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value is a 0-based array of doubles as follows:

[ CenterOfMassX, CenterOfMassY, CenterOfMassZ, Volume, Area, Mass, MomXX, MomYY, MomZZ, MomXY, MomZX, MomYZ ]

You can obtain the density currently used by the SolidWorks part by using SldWorks::GetUserPreferencDoubleValue. If the density has not been explicitly set by the end-user, then a value of 1.0 is used. You can also derive the density of the body using the following calculation:

Density = ( Mass / Volume )

Consistent with all other API functions, units returned are metric unless explicitly specified otherwise.

If this ModelDoc2 object is an assembly, then any suppressed components are not included in the mass property analysis. See Component2::GetSuppression to determine the state for each of the assembly's components.

NOTE: The Calculated origin for the returned values are based on the default coordinate systems of the ModelDoc2. They are not based on the a selected coordinate system
