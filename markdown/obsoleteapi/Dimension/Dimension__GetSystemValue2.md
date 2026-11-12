---
title: "Dimension::GetSystemValue2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Dimension/Dimension__GetSystemValue2.htm"
---

# Dimension::GetSystemValue2

This method is obsolete and has been superseded by [Dimension::GetSystemValue3](sldworksAPI.chm::/Dimension/Dimension__GetSystemValue3.htm).

Description

This method gets the dimension value of the current dimension in system units in the named configuration.

Syntax (OLE Automation)

retval = Dimension.GetSystemValue2 ( configName )

| Input: | (BSTR) configName | Name of the configuration |
| --- | --- | --- |
| Return: | (double) retval | Value of the dimension in system units |

Syntax (COM)

status = Dimension->GetSystemValue2 ( configName, &retval )

| Input: | (BSTR) configName | Name of the configuration |
| --- | --- | --- |
| Output: | (double) retval | Value of the dimension in system units |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
