---
title: "ModelDoc2::GetMassProperties2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__GetMassProperties2.htm"
---

# ModelDoc2::GetMassProperties2

This method is obsolete and has been superseded by [ModelDocExtension::GetMassProperties](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__GetMassProperties.htm).

Description

This method returns the mass properties of the current part or assembly.

Syntax (OLE Automation)

retval = ModelDoc2.GetMassProperties2 ( &status )

| Output: | (long) status | Status of the mass property results as defined in swMassPropertiesStatus_e |
| --- | --- | --- |
| Return: | (VARIANT) retval | a VARIANT of type SafeArray of doubles |

Syntax (COM)

status = ModelDoc2->IGetMassProperties2 ( &status, &mPropsData )

| Output: | (long) status | Status of the mass property results as defined in swMassPropertiesStatus_e |
| --- | --- | --- |
| Input: | (double) mPropsData | Pointer to an array of doubles |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value is a zero-based array of doubles as follows:

[ CenterOfMassX, CenterOfMassY, CenterOfMassZ, Volume, Area, Mass, MomXX, MomYY, MomZZ, MomXY, MomZX, MomYZ ]

Yu can obtain the density currently used by the SolidWorks part by using SldWorks::GetUserPreferencDoubleValue. If the density has not been explicitly set by the end-user, then a value of 1.0 is used. You can also derive the density of the body using the following calculation:

```vb
    Density = ( Mass / Volume )
```

Consistent with all other API functions, units returned are metric unless explicitly specified otherwise/

| If this object is... | Then... |
| --- | --- |
| An assembly | SolidWorks does not include any suppressed components in the mass property analysis. See Component2::GetSuppression to determine the state of each assembly component. This method returns the moments of inertia (MOI) about the assembly center-of-gravity coordinate system aligned with the assembly axes. |
| A part | The calculated origin for the returned values are based on the default coordinate systems of the model document. They are not based on the selected coordinate system. |
