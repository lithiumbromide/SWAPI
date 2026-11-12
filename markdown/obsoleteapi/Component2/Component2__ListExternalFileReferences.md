---
title: "Component2::ListExternalFileReferences"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component2/Component2__ListExternalFileReferences.htm"
---

# Component2::ListExternalFileReferences

This method is obsolete and has been superseded by [Component2::ListExternalReferences2](sldworksAPI.chm::/Component2/Component2__ListExternalFileReferences2.htm).

Description

This method gets the names and status of the external file references on this model.

Syntax (OLE Automation)

void = Component2.ListExternalFileReferences ( modelPathName, componentPathName, feature, dataType, Status, refEntity, featCom )

| Output: | (VARIANT) *modelPathName | Array of external models referenced |
| --- | --- | --- |
| Output: | (VARIANT) *componentPathName | Array of external components referenced |
| Output: | (VARIANT) *feature | Array of external features referenced |
| Output: | (VARIANT) *dataType | Array of types of data used to create the items |
| Output: | (VARIANT) *Status | Status of external reference as defined in swExternalReferenceStatus_e |
| Output: | (VARIANT) *refEntity | Array of external entity references |
| Output: | (VARIANT) *featCom | Array of the names of the components |

Syntax (COM)

status = Component2->IListExternalFileReferences ( numRefs, modelPathName, compPathName, feature, dataType, Status, refEntity, featComp )

| Input: | (long) numRefs | Number of external references |
| --- | --- | --- |
| Output: | (BSTR*) modelPathName | Array of external model references of size numRefs |
| Output: | (BSTR*) compPathName | Array of external component references of size numRefs |
| Output: | (BSTR*) feature | Array of external feature references of size numRefs |
| Output: | (BSTR*) dataType | Array of types of data used to create the items of size numRefs |
| Output: | (long*) Status | Status of external reference as defined in swExternalReferenceStatus_e |
| Output: | (BSTR*) refEntity | Array of external entity references of size numRefs |
| Output: | (BSTR*) featComp | Array of the names of the components of size numRefs |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
