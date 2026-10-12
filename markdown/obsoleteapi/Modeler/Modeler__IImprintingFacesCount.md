---
title: "Modeler::IImprintingFacesCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Modeler/Modeler__IImprintingFacesCount.htm"
---

# Modeler::IImprintingFacesCount

This method is obsolete and has been superceded by [Modeler::IImprintingFacesCount2](sldworksAPI.chm::/Modeler/Modeler__IImprintingFacesCount2.htm).

Description

This method returns the number of imprinted edges and vertices

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Modeler->IImprintingFacesCount ( nTargetFaces, *targetFaceArray, nToolFaces, *toolFaceArray, options, *nTargetEdges, *ntoolEdges, *ntargetVertices, *toolVertices, *retval )

| Input: | (long) nTargetFaces | Number of faces in the target body |
| --- | --- | --- |
| Input: | (LPFACE) *targetFaceArray | List of the faces that describe the target body |
| Input: | (long) nToolFaces | Number of faces in the tool body |
| Input: | (LPFACE) *toolFaceArray | List of the faces that describe the tool body |
| Input: | (long) options | Options for this operation as defined in swImprintingFacesOpts_e |
| Output: | (long) *nTargetEdges | Number of edges returned from this operation |
| Output: | (long) *ntoolEdges | Number of tool edges returned from this operation |
| Output: | (long) *ntargetVertices | Number of target vertices returned from this operation |
| Output: | (long) *toolVertices | Number of tool vertices returned from this operation |
| Output: | (VARIANT_BOOL) *retval | TRUE if the operation is successful, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
