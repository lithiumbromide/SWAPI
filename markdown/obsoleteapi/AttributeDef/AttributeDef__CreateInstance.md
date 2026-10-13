---
title: "AttributeDef::CreateInstance"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AttributeDef/AttributeDef__CreateInstance.htm"
---

# AttributeDef::CreateInstance

This method is obsolete and has been superseded by [AttributeDef::CreateInstance2](AttributeDef__CreateInstance2.htm).

Description

This method creates an Attribute defined by this AttributeDef on the specified entity. After an Attribute is added to an entity, the attribute and its information is stored with the document upon saving.

Syntax (OLE Automation)

retval = AttributeDef.CreateInstance ( ownerDoc, ownerEntity, nameIn)

| Input: | (LPDISPATCH) ownerDoc | Document whose FeatureManager design tree this attribute is to be added |
| --- | --- | --- |
| Input: | (LPDISPATCH) ownerEntity | Entity to which the attribute will be applied or NULL for the document |
| Input: | (BSTR) nameIn | Name to be given to this attribute instance (see Remarks ) |
| Return: | (LPDISPATCH) retval | Pointer to a dispatch object, the newly created attribute instance |

Syntax (COM)

status = AttributeDef->ICreateInstance ( ownerDoc, ownerEntity, nameIn, &retval )

| Input: | (LPMODELDOC) ownerDoc | Document whose FeatureManager design tree this attribute is to be added |
| --- | --- | --- |
| Input: | (LPENTITY) ownerEntity | Entity to which the attribute will be applied or NULL for the document |
| Input: | (BSTR) nameIn | Name to be given to this attribute instance (see Remarks ) |
| Output: | (LPATTRIBUTE) retval | Pointer to the newly created attribute instance |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The attribute is created as a feature and displayed in the FeatureManager design tree, which means that the name specified in nameIn must be unique in the FeatureManager design tree for the document.

You can create attributes on entity objects such as faces and edges, on features, or on the document itself.

NOTE: By default, SolidWorks adds attributes only to the active configuration. SolidWorks adds the attribute to all other configurations as a suppressed feature. You can unsuppress the attribute by selecting it with ModelDoc2::SelectById and calling ModelDoc2::EditUnsuppressDependent2. If you want to add your attributes to a non-active configuration, then the use must edit the properties of that particular configuration and make sure that the Suppress New Features option is disabled.
