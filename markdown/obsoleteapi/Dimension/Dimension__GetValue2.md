---
title: "Dimension::GetValue2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Dimension/Dimension__GetValue2.htm"
---

# Dimension::GetValue2

This method is obsolete and has been superseded by [Dimension::GetValue3](sldworksAPI.chm::/Dimension/Dimension__GetValue3.htm).

Description

This method gets the value of the current dimension in the named configuration.

Syntax (OLE Automation)

retval = Dimension.GetValue2 ( configName )

| Input: | (BSTR) configName | Name of the configuration |
| --- | --- | --- |
| Return: | (double) retval | Value of the dimension in user units |

Syntax (COM)

status = Dimension->GetValue2 ( configName, &retval )

| Input: | (BSTR) configName | Name of the configuration |
| --- | --- | --- |
| Output: | (double) retval | Value of the dimension in user units |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Only use the configName argument if there is more than one configuration.

This method returns a value in user units, which it gets from the document in which the dimension was created.
