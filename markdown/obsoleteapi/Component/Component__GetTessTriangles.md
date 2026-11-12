---
title: "Component::GetTessTriangles"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__GetTessTriangles.htm"
---

# Component::GetTessTriangles

This method is obsolete and has been superseded by [Component2::GetTessTriangles](sldworksAPI.chm::/Component2/Component2__GetTessTriangles.htm).

Description

This method returns the triangles that make up the shaded picture tessellation for this component.

Syntax (OLE Automation)

retval = Component.GetTessTriangles ( noConversion )

| Input: | (BOOL) noConversion | TRUE prohibits conversion to user units from system units, FALSE does not |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray (see Remarks ) |

Syntax (COM)

status = Component->IGetTessTriangles ( noConversion, retval )

| Input: | (VARIANT_BOOL) noConversion | TRUE prohibits conversion to user units from system units, FALSE does not |
| --- | --- | --- |
| Output: | (float*) retval | Pointer to array of floats (see Remarks ) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Tessellation information is available only when the component is loaded as lightweight.

These triangles are intended for graphical display purposes and do not represent a tessellation that an be used, for example, by a machining application. If you need the type of accuracy associated with a machining product, we recommend that you traverse the body faces and extract the topology and geometry data to create your own faceting.

The format of the returned data is:

- float x, y, z first point in meters
- float x, y, z second point in meters
- float x, y, z third point in meters

for the set of triangles for the component.

The total size of the data is [ 9 x sizeof(float) x (number of triangles) ].
