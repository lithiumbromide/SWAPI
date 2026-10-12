---
title: "ModelDocExtension::SelectByID"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDocExtension/ModelDocExtension__SelectByID.htm"
---

# ModelDocExtension::SelectByID

This method is obsolete and has been superseded by [ModelDocExtension::SelectByID2](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__SelectByID2.htm).

Description

This method selects the specified entity.

Syntax (OLE Automation)

retval = ModelDocExtension.SelectByID ( Name, Type, X, Y, Z, Append, Mark, Callout )

| Input: | (BSTR) Name | Name of object to select or an empty string |
| --- | --- | --- |
| Input: | (BSTR) Type | Type of object (uppercase) as defined in swSelectType_e or an empty string |
| Input: | (double) X | X selection location or 0 |
| Input: | (double) Y | Y selection location or 0 |
| Input: | (double) Z | Z selection location or 0 |
| Input: | (VARIANT_BOOL) Append | If... And if entity is... Then... TRUE Not already selected The entity is appended to the current selection list Already selected The entity is removed from the current selection list FALSE Not already selected The current selection list is cleared, and then the entity is put on the list Already selected The current selection list remains the same |
| If... | And if entity is... | Then... |
| TRUE | Not already selected | The entity is appended to the current selection list |
| FALSE | Not already selected | The current selection list is cleared, and then the entity is put on the list |
| Input: | (long) Mark | Value that you want to use as a mark; this value is used by other functions that require ordered selection |
| Input: | (LPCALLOUT) Callout | Pointer to the associated callout |
| Output: | (VARIANT_BOOL) retval | TRUE if item was successfully selected, FALSE if not |

Syntax (COM)

status = ModelDocExtension->SelectByID ( Name, Type, X, Y, Z, Append, Mark, Callout, &retval )

| Input: | (BSTR) Name | Name of object to select or an empty string |
| --- | --- | --- |
| Input: | (BSTR) Type | Type of object (uppercase) as defined in swSelectType_e or an empty string |
| Input: | (double) X | X selection location or 0 |
| Input: | (double) Y | Y selection location or 0 |
| Input: | (double) Z | Z selection location or 0 |
| Input: | (VARIANT_BOOL) Append | If... And if entity is... Then... TRUE Not already selected The entity is appended to the current selection list Already selected The entity is removed from the current selection list FALSE Not already selected The current selection list is cleared, and then the entity is put on the list Already selected The current selection list remains the same |
| If... | And if entity is... | Then... |
| TRUE | Not already selected | The entity is appended to the current selection list |
| FALSE | Not already selected | The current selection list is cleared, and then the entity is put on the list |
| Input: | (long) Mark | Value that you want to use as a mark; this value is used by other functions that require ordered selection |
| Input: | (LPCALLOUT) Callout | Pointer to the associated callout |
| Output: | (VARIANT_BOOL) retval | TRUE if item was successfully selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use this method instead of using the selection methods on the following objects:

- Annotation
- Component2
- Feature
- FeatureManager
- SketchHatch
- SketchPoint
- SketchSegment

The previously listed objects' selection methods do not work well when a PropertyManager page is open or a command is running. This method, ModelDocExtension::SelectByID, handles selection correctly whether or not a command is running.

If your application already has an object handle (for example, Face, SketchSegment, and so on), use the appropriate Select method to select the item directly using its handle.

To filter the objects selected by this method, set the Type argument. If no filtering is required, then pass an empty string for this argument.

For example, to select an object of type swSelDIMENSIONS, use the string that appears in the comment column, "DIMENSION". The objectType might change based on your current state. For example, to select a sketch point that was created in the active sketch, specify the Type "SKETCHPOINT". However, if you do not have an active sketch, or if the point was created in a sketch other than the active sketch, then specify the Type "EXTSKETCHPOINT".

If a type is specified in Type, then this method returns FALSE if it cannot find the matching object type.

The Name argument is not intended for selection of faces, edges, and so on. This is a case-sensitive string for objects that are automatically named by SolidWorks during entity creation, such as dimensions, drawing views, and so on. This method tries to find and select an object whose name matches the Name argument; however, the match needs to be exact for this method to return TRUE.

For example, if a string is passed that matches an object name but whose case does not match exactly, this method might return FALSE. For selection of dimensions, the Name argument needs to be fully qualified. For example, specify "D1@Sketch2@Part1.SLDPRT" rather than simply "D1@Sketch2"; otherwise, this method might return FALSE. If you do not know the object name, or if it is an item that is not automatically named by SolidWorks, you can pass an empty string.

If you are using the Name parameter, then specify the XYZ coordinates in terms of the context where the item was created. For example, if you want to select a sketch point using its name (for example, "Point1") in the Name argument, then specify XYZ in terms of the sketch where the point was created. Even if the sketch is not active, specify the XYZ values in terms of sketch space when you use the Name parameter. In certain situations, you can also pass in the XYZ coordinates as simply ( 0,0,0 ). For example, to select a feature shown in the FeatureManager design tree, you do not need to specify an XYZ coordinates. However, to select objects such as Notes or Faces, or when you need a point location picked, you must specify the XYZ coordinates.

If you are not using the Name parameter as a filter, then specify the XYZ coordinates in terms of model space.

If you do not know the object name or the object type, pass in empty strings for the Name and Type parameters and the selection routine makes the best attempt to select the correct object.

To get Face, Edge or Vertex objects by name, use PartDoc::GetEntityByName.

The ModelDoc object used to call this method must be an open and visible document. For example, you cannot use the ModelDoc object returned from an assembly component (Component2::GetModelDoc) unless that SolidWorks component part or subassembly is an open and visible document. In this case, you can select the item using the fully-qualified name (for example, "Plane4@Part1-1@Assem1").

When selecting Face objects, this method uses the specified point as input to the normal UI selection routines to use the speed of ray tracing. As a result, if the view changes from the original recorded size or orientation, then the same Face might not be selected next time. If your application has a pointer to the Face object to be selected, then you can call the Entity::Select3 method directly. Otherwise, you can call ModelDoc2::SelectByRay. Calling ModelDoc2::SelectByRay allows for tighter control over the starting point and the direction in which to search.
