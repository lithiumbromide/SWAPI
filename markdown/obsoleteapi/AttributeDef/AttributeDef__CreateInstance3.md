---
title: "AttributeDef::CreateInstance3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AttributeDef/AttributeDef__CreateInstance3.htm"
---

# AttributeDef::CreateInstance3

This method is obsolete and has been superseded by [AttributeDef::CreateInstance4](AttributeDef__CreateInstance4.htm).

Description

This method creates an instance of this attribute on a document, component or an entity object.

Syntax (OLE Automation)

retval = AttributeDef.CreateInstance3 ( ownerDoc, ownerComp, ownerEntity, nameIn, options, configurationOption )

| Input: | (LPDISPATCH) ownerDoc | Document whose FeatureManager design tree this attribute is to be added |
| --- | --- | --- |
| Input: | (LPDISPATCH) ownerComp | Component that this attribute is to be added or NULL if not applicable |
| Input: | (LPDISPATCH) ownerEntity | Entity to which the Attribute will be applied or NULL If not applicable |
| Input: | (BSTR) nameIn | Name to be given to this Attribute instance (see Remarks ) |
| Input: | (long) options | Creation control options (see Remarks ) |
| Input | (long) configurationOption | Configuration option as defined in swInConfigurationOpts_e |
| Return: | (LPDISPATCH) retval | Pointer to a dispatch object, the newly created attribute instance |

Syntax (COM)

status = AttributeDef ->ICreateInstance3 ( &ownerDoc, ownerComp, &ownerEntity, nameIn, options, configurationOption, &retval)

| Input: | (ImodelDoc) ownerDoc | Document whose FeatureManager design tree this attribute is to be added |
| --- | --- | --- |
| Input: | (LPCOMPONENT) ownerComp | Component that this attribute is to be added or NULL if not applicable |
| Input: | (IEntity) ownerEntity | Entity to which the Attribute will be applied or NULL If not applicable |
| Input: | (BSTR) nameIn | Name to be given to this Attribute instance (see Remarks ) |
| Input: | (long) options | Creation control options (see Remarks ) |
| Input | (long) configurationOption | Configuration option as defined in swInConfigurationOpts_e |
| Output: | (LPATTRIBUTE) retval | Pointer to the newly created attribute instance |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

When you add an attribute to a feature, the FeatureManager tree might not reflect the new state of the model. This discrepancy exists for performance reasons (rebuilding the FeatureManager tree is very time-consuming). You can request a rebuild after you have added a number of attributes to save time.

The attribute is created as a feature and displayed in the FeatureManager design tree, which means that the name specified in nameIn must be unique in the FeatureManager design tree for the document.

You can create attributes on entity objects such as faces and edges), on Features, or on the document itself.

Setting or clearing bits in the options argument controls the creation of the attribute:

| Bit | Value | Meaning |
| --- | --- | --- |
| 1 | 1 | Attribute is created hidden in the FeatureManager (see Feature::SetUIState) |
| 1 | 0 | Attribute is created visible in the FeatureManager |

For example, options = 1 creates an attribute that is hidden in the FeatureManager view.

NOTE: By default, SolidWorks adds attributes only to the active configuration. SolidWorks adds the attribute to all other configurations as a suppressed feature. You can unsuppress the attribute by selecting it with ModelDoc2::SelectById and calling ModelDoc2::EditUnsuppressDependent2. If you want to add your attributes to a non-active configuration, then the user needs to edit the properties of that particular configuration and make sure that the Suppress New Features option is disabled.

Attributes are not supported on library features or library feature parts. If you add an attribute to an entity, SolidWorks strips the attribute feature from the entity if the entity is included in your export to a library feature or library feature part. See SolidWorks Help for more information about library features.
