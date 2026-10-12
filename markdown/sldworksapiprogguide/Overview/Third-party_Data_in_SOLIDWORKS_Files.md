---
title: "Third-party Data in SOLIDWORKS Files"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Third-party_Data_in_SOLIDWORKS_Files.htm"
---

# Third-party Data in SOLIDWORKS Files

Starting with SOLIDWORKS 2015, third-party data stored in SOLIDWORKS files cannot be externally read or written by standard structured storage or compound file techniques.

To read or write third-party data, use the methods and events in the SOLIDWORKS API or SOLIDWORKS Document Manager API.

SOLIDWORKS API:

- [IModelDoc2::IGet3rdPartyStorage](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IModelDoc2~IGet3rdPartyStorage.html)
- [IModelDoc2::IRelease3rdPartyStorage](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IModelDoc2~IRelease3rdPartyStorage.html)
- [IModelDocExtension::IGet3rdPartyStorageStore](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IModelDocExtension~IGet3rdPartyStorageStore.html)
- [IModelDocExtension::IRelease3rdPartyStorageStore](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IModelDocExtension~IRelease3rdPartyStorageStore.html)
- [DAssemblyDocEvents::AutoSaveToStorageNotifyEventHandler Delegate](sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_AutoSaveToStorageNotifyEventHandler.html)
- [DAssemblyDocEvents::AutoSaveToStorageStoreNotifyEventHandler Delegate](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.DAssemblyDocEvents_AutoSaveToStorageStoreNotifyEventHandler.html)
- [DAssemblyDocEvents::LoadFromStorageNotifyEventHandler Delegate](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.DAssemblyDocEvents_LoadFromStorageNotifyEventHandler.html)
- [DAssemblyDocEvents::LoadFromStorageStoreNotifyEventHandler Delegate](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.DAssemblyDocEvents_LoadFromStorageStoreNotifyEventHandler.html)
- [DAssemblyDocEvents::SaveToStorageNotifyEventHandler Delegate](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.DAssemblyDocEvents_SaveToStorageNotifyEventHandler.html)
- [DAssemblyDocEvents::SaveToStorageStoreNotifyEventHandler Delegate](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.DAssemblyDocEvents_SaveToStorageStoreNotifyEventHandler.html)
- [DDrawingDocEvents::AutoSaveToStorageNotifyEventHandler Delegate](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.DDrawingDocEvents_AutoSaveToStorageNotifyEventHandler.html)
- [DDrawingDocEvents::AutoSaveToStorageStoreNotifyEventHandler Delegate](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.DDrawingDocEvents_AutoSaveToStorageStoreNotifyEventHandler.html)
- [DDrawingDocEvents::LoadFromStorageNotifyEventHandler Delegate](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.DDrawingDocEvents_LoadFromStorageNotifyEventHandler.html)
- [DDrawingDocEvents::LoadFromStorageStoreNotifyEventHandler Delegate](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.DDrawingDocEvents_LoadFromStorageStoreNotifyEventHandler.html)
- [DDrawingDocEvents::SaveToStorageNotifyEventHandler Delegate](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.DDrawingDocEvents_SaveToStorageNotifyEventHandler.html)
- [DDrawingDocEvents::SaveToStorageStoreNotifyEventHandler Delegate](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.DDrawingDocEvents_SaveToStorageStoreNotifyEventHandler.html)
- [DPartDocEvents::AutoSaveToStorageNotifyEventHandler Delegate](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.DPartDocEvents_AutoSaveToStorageNotifyEventHandler.html)
- [DPartDocEvents::AutoSaveToStorageStoreNotifyEventHandler Delegate](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.DPartDocEvents_AutoSaveToStorageStoreNotifyEventHandler.html)
- [DPartDocEvents::LoadFromStorageNotifyEventHandler Delegate](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.DPartDocEvents_LoadFromStorageNotifyEventHandler.html)
- [DPartDocEvents::LoadFromStorageStoreNotifyEventHandler Delegate](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.DPartDocEvents_LoadFromStorageStoreNotifyEventHandler.html)
- [DPartDocEvents::SaveToStorageNotifyEventHandler Delegate](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.DPartDocEvents_SaveToStorageNotifyEventHandler.html)
- [DPartDocEvents::SaveToStorageStoreNotifyEventHandler Delegate](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.DPartDocEvents_SaveToStorageStoreNotifyEventHandler.html)

**SOLIDWORKS Document Manager API:**

- [ISwDMDocument20::Delete3rdPartyStorage](swdocmgrapi.chm::/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20~Delete3rdPartyStorage.html)
- [ISwDMDocument20::Delete3rdPartyStorageStore](swdocmgrapi.chm::/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20~Delete3rdPartyStorageStore.html)
- [ISwDMDocument19::Get3rdPartyStorage](swdocmgrapi.chm::/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Get3rdPartyStorage.html)
- [ISwDMDocument19::Get3rdPartyStorageStore](swdocmgrapi.chm::/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Get3rdPartyStorageStore.html)
- [ISwDMDocument19::Release3rdPartyStorage](swdocmgrapi.chm::/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Release3rdPartyStorage.html)
- [ISwDMDocument19::Release3rdPartyStorageStore](swdocmgrapi.chm::/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Release3rdPartyStorageStore.html)
