---
title: "Component::GetBox"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__GetBox.htm"
---

# Component::GetBox

This method is obsolete and has been superseded by [Component2::GetBox](sldworksAPI.chm::/Component2/Component2__GetBox.htm).

Description

This method gets the bounding box for this component object.

Syntax (OLE Automation)

retval = Component.GetBox ( includeRefPlanes, includeSketches)

| Input: | (BOOL) includeRefPlanes | TRUE if you want the bounding box returned to include reference planes, FALSE if not |
| --- | --- | --- |
| Input: | (BOOL) includeSketches | TRUE if you want the bounding box returned to include sketches, FALSE if not |
| Return: | (VARIANT) retval | VARIANT containing the two diagonal points that bound the component; the format of the VARIANT is a SafeArray of 6 doubles |

Syntax (COM)

status = Component->IGetBox ( includeRefPlanes, includeSketches, retval )

| Input: | (VARIANT_BOOL)includeRefPlanes | TRUE if you want the bounding box returned to include reference planes, FALSE if not |
| --- | --- | --- |
| Input: | (VARIANT_BOOL)includeSketches | TRUE if you want the bounding box returned to include sketches, FALSE if not |
| Output: | (double*) retval | Two diagonal points that bound the component in the form of a pointer to an array of 6 doubles |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The X, Y, Z points that this method returns are the lower- and upper-diagonal corners that bound the component with the box sides parallel to the X, Y, and Z axes. These box dimensions enclose the component and are typically, but not always, close to the minimum possible size.

The return value is an array of doubles as follows:

```vb
[ XCorner1, YCorner1, ZCorner1, XCorner2, YCorner2, ZCorner2 ]
```

It is possible for this method to return S_FALSE for COM applications or a NULL VARIANT for Dispatch applications. This occurs if your application calls Component::GetBox with a component that represents a subassembly and that subassembly is not loaded in SolidWorks. After the subassembly is loaded, the correct bounds are returned and Component::IGetBox returns S_OK.

The user interface behavior is the same. When the user selects a subassembly that has not been loaded, there is no selection box around the subassembly. However, after the subassembly loads, there is a selection box.
