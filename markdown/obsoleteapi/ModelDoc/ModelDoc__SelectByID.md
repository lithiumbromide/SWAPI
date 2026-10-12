---
title: "ModelDoc::SelectByID"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SelectByID.htm"
---

# ModelDoc::SelectByID

This method is obsolete and has been superseded by [ModelDoc2::SelectByID](../ModelDoc2/ModelDoc2__SelectByID.htm).

Description

This is a generic function for all selections in the system. With appropriate input, it selects features, faces, edges, sketch items, and so on, at the location specified.

Syntax (OLE Automation)

retval = ModelDoc.SelectByID ( objectName, objectType, x, y, z)

| Input: | (BSTR) objectName | Name of object to select or an empty string |
| --- | --- | --- |
| Input: | (BSTR) objectType | Type of object or an empty string (uppercase) |
| Input: | (double) x | X Selection location or 0 |
| Input: | (double) y | Y Selection location or 0 |
| Input: | (double) z | Z Selection location or 0 |
| Return: | (BOOL) retval | TRUE if item was successfully selected, FALSE otherwise |

Syntax (COM)

status = ModelDoc->SelectByID ( objectName, objectType, x, y, z, &retval )

| Input: | (BSTR) objectName | Name of object to select or an empty string |
| --- | --- | --- |
| Input: | (BSTR) objectType | Type of object or an empty string (uppercase) |
| Input: | (double) x | X Selection location,or 0 |
| Input: | (double) y | Y Selection location or 0 |
| Input: | (double) z | Z Selection location or 0 |
| Output: | (VARIANT_BOOL) retval | TRUE if item was successfully selected, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method resets the list of selected objects to contain only objects that match the specified criteria. To append selections to the current selection set, see ModelDoc::AndSelectByID.

If your application already has an object handle (for example, Face Object, SketchSegment Object, and so on), use the appropriate Select method to select the item directly using its handle.

To filter the objects that get selected by the ModelDoc::SelectByID method, set the objectType argument as desired. This must be in uppercase. If no specific type of object is required, then an empty string can be passed in objectType; otherwise, this argument can take any of the values defined in the comments of the enumeration swSelectType_e.

For example, to select an object of type swSelDIMENSIONS, you should use the string that appears in the comment column, "DIMENSION". Be aware that the objectType can change based on your current state. For example, if you wish to select a sketch point that was created in the active sketch, then you should specify the objectType as "SKETCHPOINT". However, if you do not have an active sketch or if the point was created in a sketch other than the active sketch, then you should specify the objectType as "EXTSKETCHPOINT".

If a type is specified in objectType, then this method returns FALSE if it cannot find the matching object type.

The objectName argument is not intended for selection of faces, edges, and so on. This is a case-sensitive string that is intended for objects that are automatically named by SolidWorks during entity creation, such as dimensions, drawing views, and so on. This method attempts to find and select an object whose name matches the objectName string; however, the match must be exact for it to return a value of TRUE.

For example, if a string is passed that matches an object name but whose case does not match exactly, this mehtod may return FALSE. For selection of dimensions, the objectName argument needs to be fully qualified. For example you must specify "D1@Sketch2@Part1.SLDPRT" rather than simply "D1@Sketch2"; otherwise, this method may return FALSE. If you do not know the object name or if it is an item that is not automatically named by SolidWorks, you can pass an empty string.

If you are using the objectName parameter, then the XYZ coordinates should be in terms of the context where the item was created. For example, if you want to select a sketch point and you enter its name (for exmaple, "Point1") in the objectName parameter, then you should give XYZ in terms of the sketch where the point was created. Even if the sketch is not active, the XYZ values should be in terms of sketch space if you are using the objectName parameter. In certain situations, you can also pass in the XYZ coordinates as 0,0,0. For example, to select an feature shown in the FeatureManager design tree, you do not need to give an XYZ pick location. However, to select objects such as notes or faces, or when you need a point location picked, you must specify the XYZ coordinates.

If you are not using the objectName parameter as a filter, then the XYZ coordinates should be in terms of model space.

If you do not know the object name or the object type, pass in an empty string to the objectName and the objectType parameters and the selection routine will make its best attempt to select the correct object.

To get Face, Edge or Vertex objects by name, use the PartDoc::GetEntityByName method.

The ModelDoc object being used to call this method must be an open and visible document. For example, you cannot use the ModelDoc object returned from an assembly component (Component::GetModelDoc) unless that actual SolidWorks component part or subassembly is an open and visible document. In this case, you could select the item using the fully qualified name (for examp,e "Plane4@Part1-1@Assem1").

When selecting Face objects, the supplied point is used as input to the user-interface selection routines to use the speed of ray tracing. As a result, if the view changes from the original recorded size or orientation or both, then the same face cannot be selected upon replay. If your application has a pointer to the Face object to be selected, then you can call the Entity::Select method directly. Otherwise, you can call ModelDoc::SelectByRay. Calling SelectByRay allows for tighter control over the starting point and the direction in which to search.
