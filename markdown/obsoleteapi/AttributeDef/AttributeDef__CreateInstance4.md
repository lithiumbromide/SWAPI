---
title: "AttributeDef::CreateInstance4"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AttributeDef/AttributeDef__CreateInstance4.htm"
---

# AttributeDef::CreateInstance4

This method is obsolete and has been superseded by [AttributeDef::CreateInstance5](sldworksAPI.chm::/AttributeDef/AttributeDef__CreateInstance5.htm).

Description

This method creates an instance of this attribute on a document, component, or an entity object.

Syntax (OLE Automation)

retval = AttributeDef.CreateInstance4 ( ownerDoc, ownerObj, nameIn, options, configurationOption )

| Input: | (LPMODELDOC2) ownerDoc | Document whose FeatureManager design tree to add this attribute |
| --- | --- | --- |
| Input: | (LPDISPATCH) ownerObj | Component or entity to which to add this attribute: ENTITY, which can be a face, loop, edge, vertex, or feature COMPONENT2 MODELDOC2 if NULL |
| Input: | (BSTR) nameIn | Name to be given to this attribute instance (see Remarks ) |
| Input: | (long) options | Creation control options (see Remarks ) |
| Input: | (long) configurationOption | Configuration options as defined in swInConfigurationOpts_e |
| Output: | (LPATTRIBUTE) retval | Pointer to the newly created attribute instance |
| Return: | (HRESULT) status | S_OK if successful |

Syntax (COM)

status = AttributeDef->ICreateInstance4 ( ownerDoc, ownerComp, ownerEntity, nameIn, options, configurationOption, &retval )

| Input: | (LPMODELDOC2) ownerDoc | Document whose FeatureManager design tree this attribute is to be added |
| --- | --- | --- |
| Input: | (LPCOMPONENT2) ownerObj | Component to which to add this attribute: COMPONENT2 MODELDOC2 if NULL |
| Input: | (LPENTITY) ownerEntity | Entity to which to add this attribute: face loop edge vertex feature |
| Input: | (BSTR) nameIn | Name to be given to this attribute instance (see Remarks ) |
| Input: | (long) options | Creation control options (see Remarks ) |
| Input: | (long) configurationOption | Configuration options as defined in swInConfigurationOpts_e |
| Output: | (LPATTRIBUTE) retval | Pointer to the newly created attribute instance |

Remarks

When you add an attribute to a feature, the FeatureManager design tree might not reflect the new state of the model. This discrepancy exists for performance reasons (rebuilding the FeatureManager design tree is very time-consuming). You can request a rebuild after you have added a number of attributes to save time.

The attribute is created as a feature and displayed in the FeatureManager design tree, which means that the name specified in nameIn must be unique in the FeatureManager design tree for the document.

You can create attributes on entity objects such as faces and edges, on features, or on the document itself.

Setting or clearing bits in the options argument controls the creation of the attribute:

| Bit | Value | Meaning |
| --- | --- | --- |
| 1 | 1 | Attribute is created hidden in the FeatureManager design tree (see Feature::SetUIState) |
| 1 | 0 | Attribute is created visible in the FeatureManager design tree |

For example, options = 1 creates an attribute that is hidden in the FeatureManager design tree.

NOTE: By default, SolidWorks adds attributes only to the active configuration. SolidWorks adds the attribute to all other configurations as a suppressed feature. You can unsuppress the attribute by selecting it with ModelDocExtension::SelectByID and calling ModelDoc2::EditUnsuppressDependent2. If you want to add your attributes to a non-active configuration, then the user must edit the properties of that particular configuration and make sure that the Suppress New Features option is disabled.

Attributes are not supported on library features or library feature parts. If you add an attribute to an entity, SolidWorks strips the attribute feature from the entity if the entity is included in your export to a library feature or library feature part. See the SolidWorks Help for more information about library features.
