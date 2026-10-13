---
title: "Release Notes"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: ""
member: ""
kind: "topic"
source: "swvisualizeapi/ReleaseNotes.html"
---

# Release Notes

This topic provides you with quick access to the enhancements in SOLIDWORKS Visualize Add-in API 2026.

###### Service Pack 0

###### New interfaces

##### IBitmapImageSource Interface

- [IBitmapImageSource::GetPixels](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IBitmapImageSource~GetPixels.html)
- [IBitmapImageSource::Height](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IBitmapImageSource~Height.html)
- [IBitmapImageSource::Width](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IBitmapImageSource~Width.html)

##### IRenderCallbackHandler Interface

- [IRenderCallbackHandler::OnPreviewRequested](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderCallbackHandler~OnPreviewRequested.html)
- [IRenderCallbackHandler::OnRenderActionRequested](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderCallbackHandler~OnRenderActionRequested.html)

##### IRendererPropertiesStatus2 Interface

- [IRendererPropertiesStatus2::BitmapPreviewImageSource2](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus2~BitmapPreviewImageSource2.html) (obsoletes IRendererPropertiesStatus::BitmapPreveiwImageSource)

##### IRenderNotificationHandler2 Interface (obsoletes IRenderNotificationHandler)

- [IRenderNotificationHandler2::RendererPropertyChangedNotify](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler2~RendererPropertyChangedNotify.html) (obsoletes IRenderNotificationHandler::RendererPropertyChangedNotify)
- [IRenderNotificationHandler2::SetCallbackHandler](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler2~SetCallbackHandler.html)

##### IVisualizeAddin2 Interface

- [IVisualizeAddin2::GetAddinManager2](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddin2~GetAddinManager2.html) (obsoletes IVisualizeAddin::GetAddinManager)

##### IVisualizeAddinManager2 Interface

- [IVisualizeAddinManager2::LaunchVisualize](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2~LaunchVisualize.html)
- [IVisualizeAddinManager2::SaveWithPartGrouping](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2~SaveWithPartGrouping.html) (obsoletes IVisualizeAddinManager::Save)
- [IVisualizeAddinManager2::StartRender2](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2~StartRender2.html) (obsoletes IVisualizeAddinManager::StartRender)

###### Obsoleted interfaces and methods

##### IRendererPropertiesStatus interface

- IRendererPropertiesStatus::BitmapPreviewImageSource (superseded by [IRendererPropertiesStatus2::BitmapPreviewImageSource2](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus2~BitmapPreviewImageSource2.html))

##### IRenderNotificationHandler interface (superseded by IRenderNotificationHandler2 )

- IRenderNotificationHandler::RendererPropertyChangedNotify (superseded by [IRenderNotificationHandler2::RendererPropertyChangedNotify](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler2~RendererPropertyChangedNotify.html))

##### IVisualizeAddin interface

- IVisualizeAddin::GetAddinManager (superseded by [IVisualizeAddin2::GetAddinManager2](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddin2~GetAddinManager2.html))

##### IVisualizeAddinManager interface

- IVisualizeAddinManager::Save (superseded by [IVisualizeAddinManager2::SaveWithPartGrouping](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2~SaveWithPartGrouping.html))
- IVisualizeAddinManager::StartRender (superseded by [IVisualizeAddinManager2::StartRender2](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2~StartRender2.html))
