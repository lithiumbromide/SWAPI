---
title: "ModelDoc::GetMassProperties2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetMassProperties2.htm"
---

# ModelDoc::GetMassProperties2

This method is obsolete and has been superseded by [ModelDoc2::GetMassProperties2](../ModelDoc2/ModelDoc2__GetMassProperties2.htm).

Description

This method returns the mass properties of the current part or assembly.

Syntax (OLE Automation)

retval = ModelDoc.GetMassProperties2 ( &status )

| Output: | (long) status | Status of the mass property results as defined in swMassPropertiesStatus_e |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray |

Syntax (COM)

status = ModelDoc->GetMassProperties2 ( &status, &mPropsData )

| Output: | (long) status | Status of the mass property results as defined in swMassPropertiesStatus_e |
| --- | --- | --- |
| Input: | (double) mPropsData | Pointer to an array of doubles |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value is a 0-based array of doubles as follows:

[ CenterOfMassX, CenterOfMassY, CenterOfMassZ, Volume, Area, Mass, MomXX, MomYY, MomZZ, MomXY, MomZX, MomYZ ]

To obtain the density currently being used by the SolidWorks part, call SldWorks::GetUserPreferencDoubleValue. If the user has not explicitly set the density, then a value of 1.0 will be used. You can also derive the density of the body using the following calculation:

Density = ( Mass / Volume )

Consistent with all other API functions, units returned will be metric unless explicitly specified.

If this ModelDoc object is an assembly, then any suppressed components are not included in the mass property analysis. Use Component::GetSuppression to determine the state for each of the assembly's components.

NOTE: The calculated origin for the returned values is based on the default coordinate systems of the ModelDoc. It is not based on the a selected coordinate system.
