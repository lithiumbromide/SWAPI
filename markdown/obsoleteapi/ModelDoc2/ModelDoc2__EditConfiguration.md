---
title: "ModelDoc2::EditConfiguration"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__EditConfiguration.htm"
---

# ModelDoc2::EditConfiguration

This method is obsolete and has been superseded by [ModelDoc2::EditConfiguration2](ModelDoc2__EditConfiguration2.htm).

Description

This method allows you to edit the named configuration. Any component added to your assembly takes on these settings if this configuration is the active configuration. To edit the configuration of an individual component, use AssemblyDoc::CompConfigProperties.

Syntax (OLE Automation)

retval = ModelDoc2.EditConfiguration ( name, newname, comment, alternateName, suppressByDefault, hideByDefault, minFeatureManager, inheritProperties, flags )

| Input: | (BSTR) name | Name of the configuration to edit |
| --- | --- | --- |
| Input: | (BSTR) newname | New name for the configuration or NULL string otherwise |
| Input: | (BSTR) comment | Comment string for documenting your configuration |
| Input: | (BSTR) alternateName | Alternate name for Bill of Materials (see Remarks ) |
| Input: | (BOOL) suppressByDefault | TRUE if you want newly added components to be suppressed, FALSE otherwise |
| Input: | (BOOL) hideByDefault | TRUE if you want newly added components to be hidden, FALSE otherwise |
| Input: | (BOOL) minFeatureManager | TRUE if you want newly added components to only display their component name in the FeatureManager design tree, FALSE if you want newly added components to display their name and each of their features in the FeatureManager design tree |
| Input: | (BOOL) inheritProperties | TRUE if you want to inherit properties, FALSE if not |
| Input: | (ULONG) flags | Additional control (see Remarks ) |
| Return: | (BOOL) retval | TRUE if the configuration is modified, FALSE if not |

Syntax (COM)

status = ModelDoc2->EditConfiguration ( name, newname, comment, alternateName, suppressByDefault, hideByDefault, minFeatureManager, inheritProperties, flags )

| Input: | (BSTR) name | Name of the configuration to edit |
| --- | --- | --- |
| Input: | (BSTR) newname | New name for the configuration or NULL string otherwise |
| Input: | (BSTR) comment | Comment string for documenting your configuration |
| Input: | (BSTR) alternateName | Alternate name for Bill of Materials (see Remarks ) |
| Input: | (VARIANT_BOOL) suppressByDefault | TRUE if you want newly added components to be suppressed, FALSE otherwise |
| Input: | (VARIANT_BOOL) hideByDefault | TRUE if you want newly added components to be hidden, FALSE otherwise |
| Input: | (VARIANT_BOOL) minFeatureManager | TRUE if you want newly added components to only display their component name in the FeatureManager design tree, FALSE if you want newly added components to display their name and each of their features in the FeatureManager design tree |
| Input: | (VARIANT_BOOL) inheritProperties | TRUE if you want to inherit properties, FALSE if not |
| Input: | (ULONG) flags | Additional control (see Remarks ) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The flags argument allows additional control of the created configuration. It can take these values from the ConfigurationFlags_e enumeration swoptions.h:

- CONFIG_USE_ALTERNATENAME - When set ,indicates that the alternateName specified is used in the Bill of Materials.
- CONFIG_DONT_SHOW_PARTS_IN_BOM - When set, specifies that subassemblies show in the Bill of Materials; otherwise, the child components are listed in the Bill of Materials.
