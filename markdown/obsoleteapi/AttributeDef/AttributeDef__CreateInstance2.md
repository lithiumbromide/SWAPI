---
title: "AttributeDef::CreateInstance2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AttributeDef/AttributeDef__CreateInstance2.htm"
---

# AttributeDef::CreateInstance2

This method is obsolete and has been superseded by [AttributeDef::CreateInstance3](AttributeDef__CreateInstance3.htm)

Description

This method creates an Attribute defined by this AttributeDef on the specified entity. After an Attribute is added to an entity, the attribute and its information is stored with the document upon saving.

Syntax (OLE Automation)

retval = AttributeDef.CreateInstance2 ( ownerDoc, ownerEntity, nameIn, options)

| Input: | (LPDISPATCH) ownerDoc | Document whose FeatureManager design tree this attribute is to be added. |
| --- | --- | --- |
| Input: | (LPDISPATCH) ownerEntity | Entity to which the Attribute will be applied or NULL for the document |
| Input: | (BSTR) nameIn | Name to be given to this Attribute instance |
| Input: | (long) options | Creation control options |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created attribute instance |

Syntax (COM)

status = AttributeDef->ICreateInstance2 ( ownerDoc, ownerEntity, nameIn, options, &retval )

| Input: | (LPMODELDOC) ownerDoc | Document whose FeatureManager design tree this attribute is to be added |
| --- | --- | --- |
| Input: | (LPENTITY) ownerEntity | Entity to which the Attribute will be applied or NULL for the document |
| Input: | (BSTR) nameIn | Name to be given to this Attribute instance |
| Input: | (long) options | Creation control options |
| Output: | (LPATTRIBUTE) retval | Pointer to the newly created attribute instance |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The attribute is created as a feature and displayed in the FeatureManager, which means that the name specified in nameIn must be unique in the FeatureManager for the document.

You can create attributes on Entity objects (such as Faces and Edges), on Features, or on the document itself.

Setting or clearing bits in the options argument controls the creation of the attribute:

| Bit | Value | Meaning |
| --- | --- | --- |
| 1 | 1 | Attribute is created hidden in the FeatureManager (see Feature::SetUIState) |
|  | 0 | Attribute is created visible in the FeatureManager |

For example, Options = 1 creates an attribute that is hidden in the FeatureManager view.

NOTE: By default, SolidWorks adds attributes only to the active configuration. SolidWorks adds the attribute to all other configurations as a suppressed feature. You can unsuppress the attribute by selecting it with ModelDoc2::SelectById and calling ModelDoc2::EditUnsuppressDependent2. If you want to add your attributes to a non-active configuration, then the user needs to edit the properties of that particular configuration and make sure that the Suppress New Features option is disabled.

Attributes are not supported on Library Features or Library Feature Parts. If you add an attribute to an entity, SolidWorks strips the Attribute feature from the entity if the entity is included in your export to a Library Feature or Library Feature Part.
