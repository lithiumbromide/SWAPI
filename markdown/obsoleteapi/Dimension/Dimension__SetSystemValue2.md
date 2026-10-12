---
title: "Dimension::SetSystemValue2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Dimension/Dimension__SetSystemValue2.htm"
---

# Dimension::SetSystemValue2

This method is obsolete and has been superseded by [Dimension::SetSytemValue3](sldworksAPI.chm::/Dimension/Dimension__SetSystemValue3.htm).

Description

This method sets the dimension value in system units (meters) in the specified configurations.

Syntax (OLE Automation)

retval = Dimension.SetSystemValue2 ( newValue, allConfigs )

| Input: | (double) newValue | Dimension value in meters |
| --- | --- | --- |
| Input: | (long) whichConfigs | Configurations in which to set this value as defined in swSetValueInConfiguration_e |
| Return: | (long) retval | Success indicator value as defined in swSetValueReturnStatus_e |

Syntax (COM)

status = Dimension->SetSystemValue2 ( newValue, allConfigs, retval, &retval )

| Input: | (double) newValue | Dimension value in meters |
| --- | --- | --- |
| Input: | (long) whichConfigs | Configurations in which to set this value as defined in swSetValueInConfiguration_e |
| Output: | (long) retval | Success indicator value as defined in swSetValueReturnStatus_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The whichConfigs argument is equivalent to the Change Parameter dialog in the SolidWorks user interface, which gives the user the option of having the value set in all configurations or the current configuration. If there is one configuration in the part, SolidWorks ignores this argument.

This method allows you to change the value of a read-only dimension. You can use Dimension::ReadOnly to determine if a dimension is read-only.
