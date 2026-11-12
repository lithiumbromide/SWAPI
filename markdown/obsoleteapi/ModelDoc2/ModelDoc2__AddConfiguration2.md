---
title: "ModelDoc2::AddConfiguration2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__AddConfiguration2.htm"
---

# ModelDoc2::AddConfiguration2

This method is obsolete and has been superseded by [ModelDoc2::AddConfiguration3](sldworksAPI.chm::/ModelDoc2/ModelDoc2__AddConfiguration3.htm).

Description

This method creates a new configuration. Any component added to your assembly inherits these settings if this configuration is the active configuration.

Syntax (OLE Automation)

retval = ModelDoc2.AddConfiguration2 ( name, comment, alternateName, suppressByDefault, hideByDefault, minFeatureManager, inheritProperties, flags)

| Input: | (BSTR) name | Name to be given to this new configuration |
| --- | --- | --- |
| Input: | (BSTR) comment | Comment string for documenting your configuration |
| Input: | (BSTR) alternateName | Alternate name for Bill of Materials |
| Input: | (VARIANT_BOOL) suppressByDefault | TRUE if you want newly added components to be suppressed, FALSE if not |
| Input: | (VARIANT_BOOL) hideByDefault | TRUE if you want newly added components to be hidden, FALSE if not |
| Input: | (VARIANT_BOOL) minFeatureManager | TRUE if you want newly added components to only display their component name in the FeatureManager design tree; FALSE if you want newly added components to display their name and each of their features in the FeatureManager design tree |
| Input: | (VARIANT_BOOL) inheritProperties | TRUE if you want to inherit properties |
| Input: | (ULONG) flags | Additional control |
| Return: | (VARIANT_BOOL) retval | VARIANT_TRUE if created successfully, FALSE If not |

Syntax (COM)

status = ModelDoc2->AddConfiguration2 ( name, comment, alternateName, suppressByDefault, hideByDefault, minFeatureManager, inheritProperties, flags, &retval )

| Input: | (BSTR) name | Name to be given to this new configuration |
| --- | --- | --- |
| Input: | (BSTR) comment | Comment string for documenting your configuration |
| Input: | (BSTR) alternateName | Alternate name for Bill of Materials |
| Input: | (VARIANT_BOOL) suppressByDefault | TRUE if you want newly added components to be suppressed, FALSE if not |
| Input: | (VARIANT_BOOL) hideByDefault | TRUE if you want newly added components to be hidden, FALSE if not |
| Input: | (VARIANT_BOOL) minFeatureManager | TRUE if you want newly added components to only display their component name in the FeatureManager design tree; FALSE if you want newly added components to display their name and each of their features in the FeatureManager design tree |
| Input: | (VARIANT_BOOL) inheritProperties | TRUE if you want to inherit properties |
| Input: | (ULONG) flags | Additional control |
| Output: | (VARIANT_BOOL) retval | VARIANT_TRUE if successfully created, VARIANT_FALSE if not |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method is identical to the earlier version, ModelDoc::AddConfiguration, except that it returns a BOOLEAN to indicate success or failure.

The flags argument allows additional control of the created configuration. It can take the values from the ConfigurationFlags_e:

- CONFIG_USE_ALTERNATENAME - When set indicates that the alternateName specified is used in the Bill of Materials.
- CONFIG_DONT_SHOW_PARTS_IN_BOM - When set, specifies that sub-assemblies show in the Bill of Materials, otherwise the child components are listed in the Bill of Materials.
