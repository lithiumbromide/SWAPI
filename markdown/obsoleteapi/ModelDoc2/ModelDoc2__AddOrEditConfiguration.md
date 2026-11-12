---
title: "ModelDoc2::AddOrEditConfiguration"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__AddOrEditConfiguration.htm"
---

# ModelDoc2::AddOrEditConfiguration

This method is obsolete and has been superseded by [Configuration::GetParameters](sldworksAPI.chm::/Configuration/Configuration__GetParameters.htm) and [Configuration::SetParameters](sldworksAPI.chm::/Configuration/Configuration__SetParameters.htm).

Description

This method adds or edits a configuration in the model document.

Syntax (OLE Automation)

retval = ModelDoc2.AddOrEditConfiguration ( ConfigName, paramNames, paramValues )

| Input: | (BSTR) ConfigName | Name of the configuration |
| --- | --- | --- |
| Input: | (VARIANT) paramNames | Array of parameters (see Remarks ) |
| Input: | (VARIANT) paramValues | Array of values (see Remarks ) |
| Output: | (long) retval | Indicates success or failure |

Syntax (COM)

status = ModelDoc2->IAddOrEditConfiguration ( ConfigName, paramCount, paramNames, paramValues, &retval )

| Input: | (BSTR) ConfigName | Name of the configuration |
| --- | --- | --- |
| Input: | (long) paramCount | Number of parameters |
| Input: | (BSTR*) paramNames | Array of parameters of size paramCount (see Remarks ) |
| Input: | (BSTR) *paramValues | Array of values of size paramCount (see Remarks ) |
| Output: | (long) retval | Indicates success or failure |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can control the following items in a part document:

- Dimension values. Specify the dimension name in paramNames (for example, D1@Sketch1) and the value in paramValues (for example, 60.0mm).
- Suppression state of features. Specify the feature name in paramNames (for example, $STATE@Extrude2) and the suppression state in paramValues (S=suppressed or U=Unsuppressed) .
