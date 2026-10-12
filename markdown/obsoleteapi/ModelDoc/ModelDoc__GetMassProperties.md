---
title: "ModelDoc::GetMassProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetMassProperties.htm"
---

# ModelDoc::GetMassProperties

This method is obsolete and has be superseded by [ModelDoc::GetMassProperties2](ModelDoc__GetMassProperties2.htm).

Description

This method returns the mass properties of the current part or assembly.

Syntax (OLE Automation)

retval = ModelDoc.GetMassProperties ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IGetMassProperties ( mPropsData, &retval )

| Input: | (double) mPropsData | Pointer to an array of doubles . |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if not |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The return value is a 0-based array of doubles as follows:

[ CenterOfMassX, CenterOfMassY, CenterOfMassZ, Volume, Area, Mass, MomXX, MomYY, MomZZ, MomXY, MomZX, MomYZ ]

To obtain the density currently used by the SolidWorks part, call SldWorks::GetUserPreferencDoubleValue. If the user did not explicitly set the density, then a value of 1.0 is used. You can also derive the density of the body using the following calculation:

Density = ( Mass / Volume )

Consistent with all other API functions, units returned will be metric unless explicitly specified.

If this ModelDoc object is an assembly, then any suppressed components are not included in the mass property analysis. Use Component::GetSuppression to determine the state for each of the assembly's components.

NOTE: The calculated origin for the returned values is based on the default coordinate systems of the ModelDoc. It is not not based on the a selected coordinate system.
