---
title: "Controls on Multipage PropertyManager Page"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Controls_on_Multipage_PropertyManager_Page.htm"
---

# Controls on Multipage PropertyManager Page

All of the controls for a multipage PropertyManager page must be contained on a single page.

Your add-in must simulate the appearance of multipage controls by showing and hiding the appropriate controls (the add-in must know which controls to show on each page) as the user moves from page to page. This means that your implementation of [IPropertyManagerPage2Handler8](swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8.html) must know which page is currently in use and act accordingly within the [IPropertyManagerPage2Handler8::OnNextPage](swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8~OnNextPage.html) and [IPropertyManagerPage2Handler8::OnPreviousPage](swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8~OnPreviousPage.html) callbacks.

Your add-in must not respond to the next page handler by trying to show a second page because:

- The first page will close.
- When the next page handler returns control to the SOLIDWORKS Design application and your code, the first page is gone and a memory error occurs.
