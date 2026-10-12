---
title: "ModelDoc2::ListExternalFileReferences2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__ListExternalFileReferences2.htm"
---

# ModelDoc2::ListExternalFileReferences2

This method is obsolete and has been superseded by [ModelDocExtension::ListExternalFileReferences](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__ListExternalFileReferences.htm).

Description

This method gets the names and statuses of the external file references on this model.

Syntax (OLE Automation)

void = ModelDoc2.ListExternalFileReferences2 ( modelPathName, componentPathName, feature, dataType, Status, refEntity, featCom )

| Output: | (VARIANT) *modelPathName | Array of external parts' or assemblies' paths and names |
| --- | --- | --- |
| Output: | (VARIANT) *componentPathName | Array of configurations of the referenced components to use for derived parts |
| Output: | (VARIANT) *feature | Array of in-context items (sketches, features, and so on) in the selected part |
| Output: | (VARIANT) *dataType | Array of data used to create the items (converted edge or face, converted or offset sketch entity, body, and so on) |
| Output: | (VARIANT) *Status | Status of external reference as defined in swExternalReferenceStatus_e |
| Output: | (VARIANT) *refEntity | Array of actual items being used and the names of the documents that contain the items |
| Output: | (VARIANT) *featCom | Array of the names of the components in which the affected features exist; this information is only displayed when one or more refEntity is in a different component in an assembly; this does not apply to derived parts |

Syntax (COM)

status = ModelDoc2->IListExternalFileReferences2 ( numRefs, modelPathName, compPathName, feature, dataType, Status, refEntity, featComp )

| Input: | (long) numRefs | Number of external references |
| --- | --- | --- |
| Output: | (BSTR*) modelPathName | Array of external parts' or assemblies' paths and names of size numRefs |
| Output: | (BSTR*) compPathName | Array of configurations of the referenced components to use for derived parts of size numRefs |
| Output: | (BSTR*) feature | Array of in-context items (sketches, features, and so on) in the selected part of size numRefs |
| Output: | (BSTR*) dataType | Array of data used to create the items (converted edge or face, converted or offset sketch entity, body, and so on) of size numRefs |
| Output: | (long*) Status | Status of external reference as defined in swExternalReferenceStatus_e |
| Output: | (BSTR*) refEntity | Array of actual items being used and the names of the documents that contain the items of size numRefs |
| Output: | (BSTR*) featComp | Array of the names of the components in which the affected features exist of size numRefs; this information is only displayed when one or more refEntity is in a different component in an assembly; this does not apply to derived parts |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Call ModelDoc2::ListExternalFileReferencesCount2 before calling the COM version of this method to determine the size of the array required.
