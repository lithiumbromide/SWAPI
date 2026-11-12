---
title: "Persistent Reference IDs"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Persistent_Reference_IDs.htm"
---

# Persistent Reference IDs

Selectable objects in a SOLIDWORKS model document are assigned unique reference IDs. The reference IDs persist for the objects in the model document across SOLIDWORKS sessions. Other applications can use persistent reference IDs to locate objects at runtime.

Some methods that support the retrieval of persistent reference IDs are:

- [IModelDocExtension::GetPersistReferenceCount3](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IModelDocExtension~GetPersistReferenceCount3.html): returns the size of the persistent reference ID for the selected object. Call this method before calling [IModelDocExtension::IGetPersistReference3](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IModelDocExtension~IGetPersistReference3.html).

NOTE: See [swSelectType_e](swconst.chm::/SolidWorks.interop.swconst~SolidWorks.interop.swconst.swSelectType_e.html) for a list of selectable objects. You can select the objects via the user interface or programmatically by using [IModelDocExtension::SelectByID2](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IModelDocExtension~SelectByID2.html).

- [IModelDocExtension::GetPersistReference3](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IModelDocExtension~GetPersistReference3.html): returns the persistent reference ID for the selected object. Call this method before calling [IModelDocExtension::GetObjectByPersistReference3](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IModelDocExtension~GetObjectByPersistReference3.html).
- [IModelDocExtension::GetObjectByPersistReference3](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IModelDocExtension~GetObjectByPersistReference3.html): returns the object by its persistent reference ID.
