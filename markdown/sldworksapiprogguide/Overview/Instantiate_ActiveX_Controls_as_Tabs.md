---
title: "Instantiate ActiveX Controls as Tabs"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Instantiate_ActiveX_Controls_as_Tabs.htm"
---

# Instantiate ActiveX Controls as Tabs

Adding a custom tab to the FeatureManager design tree and model view were previously only available to MFC-extension DLL add-ins and required a strong knowledge of MFC, Windows messaging, and Windows SDK. Problems were difficult to diagnose and fix. Additionally the SOLIDWORKS methods for adding a tab to the FeatureManager design tree and model view were highly MFC-specific and, as such, were not COM-compliant.

SOLIDWORKS now has the ability to instantiate any arbitrary ActiveX control as a tab in the FeatureManager design tree and model view. The new methods are fully COM-compliant and reduce the knowledge required for adding a tab.

Using VBA, VB.NET, C#, or any development environment capable of creating an ActiveX control, you can easily develop a SOLIDWORKS-specific ActiveX control.

See:

- [IModelViewManager::CreateFeatureMgrControl2](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IModelViewManager~CreateFeatureMgrControl2.html)
- [IModelViewManager::AddControl](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IModelViewManager~AddControl.html)
