---
title: "Configuration::Select"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Configuration/Configuration__Select.htm"
---

# Configuration::Select

This method is obsolete and has been superseded by [Configuration::Select2](sldworksAPI.chm::/Configuration/Configuration__Select2.htm).

Description

This method selects the configuration.

Syntax (OLE Automation)

retval = Configuration.Select ( appendFlag)

| Input: | (VARIANT_BOOL) appendFlag | TRUE appends the configuration to the selection list, FALSE replaces the selection list with the configuration |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the configuration is selected, FALSE if not |

Syntax (COM)

status = Configuration->Select ( appendFlag, &retval)

| Input: | (VARIANT_BOOL) appendFlag | TRUE appends the configuration to the selection list, FALSE replaces the selection list with the configuration |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the configuration is selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
