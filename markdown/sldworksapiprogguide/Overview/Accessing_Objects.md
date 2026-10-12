---
title: "Accessing SOLIDWORKS Objects"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Accessing_Objects.htm"
---

# Accessing SOLIDWORKS Objects

To call any of the SOLIDWORKS API's methods or properties, you first need to obtain the object. For example, to use the IFace2::GetArea method you need to have a IFace2 object.

There are various ways to access objects within the SOLIDWORKS API. To obtain the Face2 object, you could use one of the following accessors:

- Obtain the IBody2 object using IPartDoc::GetBodies2 or IPartDoc::EnumBodies3, and then traverse the faces on the body using the IBody2::GetFirstFace and IFace2::GetNextFace methods.

  - or -
- Get the IFace2 object from the current set of selected items using ISelectionMgr::GetSelectedObject6.

  - or -
- Get the IFace2 object by its name using IPartDoc::GetEntityByName.

When you have the IFace2 object, you can access the properties and methods found in the Face2 class. For example, you could get the number of edges on the face using the IFace2::GetEdgeCount method, or you could get the normal vector for the face using the IFace2::Normal property.

NOTE: Some methods and properties, such as IFeatureManager::InsertMateReference, also require one or more selected items. The items can be selected in one of two ways:

- The end-user can interactively select the items.

  - or -
- You can programmatically select the items using IModelDocExtension::SelectByID2.

See [Accessing SOLIDWORKS Add-in Objects](Accessing_Add-ins.htm).
