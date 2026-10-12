---
title: "Component::GetTessNorms"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__GetTessNorms.htm"
---

# Component::GetTessNorms

This method is obsolete and has been superseded by [Component2::GetTessNorms](sldworksAPI.chm::/Component2/Component2__GetTessNorms.htm).

Description

This method returns the normal vector for each of the triangles, which make up the shaded picture tessellation for the component.

Syntax (OLE Automation)

retval = Component.GetTessNorms ( )

| Return: | (VARIANT) retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = Component->IGetTessNorms ( retval )

| Output: | (float*) retval | Pointer to an array of floats |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Tessellation information is available only when the component is loaded as lightweight.

The format of the returned data is:

- float x, y, z first point's unit normal
- float x, y, z second point's unit normal
- float x, y, z third point's unit normal

for the set of triangles for the component.

The total size of the data is [ 9 x sizeof(float) x (number of triangles) ].
