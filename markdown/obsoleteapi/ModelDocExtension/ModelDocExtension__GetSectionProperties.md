---
title: "ModelDocExtension::GetSectionProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDocExtension/ModelDocExtension__GetSectionProperties.htm"
---

# ModelDocExtension::GetSectionProperties

This method is obsolete and has been superseded by [ModelDocExtension::GetSectionProperties2](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__GetSectionProperties2.htm).

Description

This method gets the section properties for the following types of selected items:

- Planar model face in any document
- Face on a section plane
- Crosshatch section face in a section view in a drawing a sketch
- Sketch

Syntax (OLE Automation)

retval = ModelDocExtension.GetSectionProperties ( sections )

| Input: | (VARIANT) sections | Array of sections |
| --- | --- | --- |
| Output: | (VARIANT) * retval | SafeArray of section properties for the selected items |

Syntax (COM)

status = ModelDocExtension->IGetSectionProperties ( count, sections, retval )

| Input: | (long) count | Number of sections |
| --- | --- | --- |
| Input: | (LPUNKNOWN) *sections | Array of sections of size count |
| Output: | (double) * retval | Array of size 15 of the section properties for the selected items (see Remarks ) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method clears the selection set.

| If... | Then... |
| --- | --- |
| The user selected a set of either parallel planes or parallel faces | You can pass an empty sections array |
| The user selected any items and you pass a sections array | The properties of the user-selected items and the sections array are combined in retval |
| You pass a sections array and you do not want this array combined with the properties of any user-selected items | Clear any user-selected items |

The objects in the sections parameter are added to the current selection set. If the objects are already in the current selection set, an error is generated; that is, status code will be equal to 1, which means invalid input.

The format of retval is an array of size 15:

| retval[0] | status of request: 0 = success 1 = invalid input 2 = selected faces are not in the same or parallel planes 3 = unable to compute section properties |
| --- | --- |
| retval[1] | area |
| retval[2] | centroid x |
| retval[3] | centroid y |
| retval[4] | centroid z |
| retval[5] | moment of inertia XX |
| reval[6] | moment of inertia YY |
| retval[7] | moment of inertia ZZ |
| retval[8] | moment of inertia -XY |
| retval[9] | moment of inertia -ZX |
| retval[10] | moment of inertia -YZ |
| retval[11] | polar moment of inertia of an area at the centroid |
| retval[12] | angle between principal axis and part axis |
| retval[13] | principal moment of inertia of an area at the centroid, 1x |
| retval[14] | principal moment of inertia of an area at the centroid, 1y |

This method returns metric units unless explicitly specified otherwise.
