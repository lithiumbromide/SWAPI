---
title: "Eliminating 32-bit only API use"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Eliminating_32-Bit_Only_API_Use.htm"
---

# Eliminating 32-bit only API use

Several older SOLIDWORKS APIs were implemented to pass 32-bit pointers and handles. These APIs can no longer be used safely with 64-bit editions of SOLIDWORKS. Since SOLIDWORKS has only been available as a 64-bit application since SOLODWORKS 2016, **any use of these APIs in current applications is inherently unsafe**.

Since these APIs are passing 64-bit pointers and handles as 32-bit integers, there is a risk that the pointer/handle will be truncated silently. This may not cause an immediate exception, however, an exception may occur unexpectedly sometime later when the truncated pointer/handle is used. Such exceptions are notoriously difficult to reproduce and diagnose.

**All application authors should review their source code to replace calls to the following 32-bit only APIs with their 64-bit safe counterparts.**

### Obsolete 32-bit only APIs and their 64-bit safe counterparts

| Obsolete 32-bit API | 64-bit safe API |
| --- | --- |
| IFeatMgrView::GetFeatMgrViewWnd | IFeatMgrView::GetFeatMgrViewWndx64 |
| IFrame::GetHWnd | IFrame::GetHWndx64 |
| IFrame::GetMenu | IFrame::GetMenux64 |
| IModelDoc2::InsertSketchPictureData | IModelDoc2::InsertSketchPictureDatax64 |
| IModelDoc/IModelDoc2::ActivateFeatureMgrView | IModelDocExtension::ActivateFeatureMgrViewx64 |
| IModelDoc/IModelDoc2::AddFeatureMgrView IModelDoc/IModelDoc2::AddFeatureMgrView2 IModelDoc/IModelDoc2::AddFeatureMgrView3 | IModelDocExtension::AddFeatureMgrView3 |
| IModelDoc/IModelDoc2::DeActivateFeatureMgrView | IModelDocExtension::DeActivateFeatureMgrViewx64 |
| IModelDoc/IModelDoc2::DeleteFeatureMgrView | IModelDocExtension::DeleteFeatureMgrViewx64 |
| IModelDoc2::GetSceneBkgDIB | IModelDocExtension::GetSceneBkgDIBx64 |
| IModelDoc2::SetSceneBkgDIB | IModelDocExtension::SetSceneBkgDIBx64 |
| IModelView::GetViewDIB | IModelView::GetViewDIBx64 |
| IModelView::GetViewHWnd | IModelView::GetViewHWndx64 |
| IModelViewManager::CreateFeatureMgrWindowFromHandle | IModelViewManager::CreateFeatureMgrWindowFromHandlex64 |
| IModelViewManager::DisplayWindowFromHandle | IModelViewManager::DisplayWindowFromHandlex64 |
| IModelViewManager::GetFeatureMgrViewHWnd | IModelViewManager::GetFeatureMgrViewHWndx64 |
| IModelWindow::HWnd | IModelWindow::HWndx64 |
| IPropertyManagerPage2::SetTitleBitmap | IPropertyManagerPage2::SetTitleBitmapx64 |
| IPropertyManagerPageBitmapButton::SetBitmaps | IPropertyManagerPageBitmapButton::SetBitmapsx64 |
| IPropertyManagerPageWindowFromHandle::SetWindowHandle | IPropertyManagerPageWindowFromHandle::SetWindowHandlex64 |
| ISldWorks::PostMessageToApplication | ISldWorks::PostMessageToApplicationx64 |
| ISldWorks::PreviewDoc | ISldWorks::PreviewDocx64 |
| ISWPropertySheet::AddPage | ISWPropertySheet::AddPage |
| ITaskPaneView::DisplayWindowFromHandle | ITaskPaneView::DisplayWindowFromHandle |
