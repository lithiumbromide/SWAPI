---
title: "PropertyManagerPage2Handler4::OnTabClicked"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnTabClicked.htm"
---

# PropertyManagerPage2Handler4::OnTabClicked

This method is obsolete and has been superseded by [PropertyManagerPage2Handler5::OnTabClicked.](sldworksAPI.chm::/PropertyManagerPage2Handler5/PropertyManagerPage2Handler5__OnTabClicked.htm)

Description

This method is called when a user clicks a tab on a multi-tab PropertyManager page.

Syntax (OLE Automation)

retval = PropertyManagerPage2Handler4.OnTabClicked ( Id)

| Input: | (long) Id | ID of the tab clicked (see Remarks ) |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the tab clicked is processed, FALSE if not |

Syntax (COM)

status = PropertyManagerPage2Handler4->OnTabClicked ( Id, &retval)

| Input: | (long) Id | ID of the tab clicked (see Remarks ) |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the tab clicked is processed, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The value of Id is the ID that was specified when the tab was created by PropertyManagerPage2::AddTab.

When a user clicks a tab, control is passed to the add-in via this method. The add-in is expected to show or hide groups and controls intended to be visible or hidden on that tab.

Your add-in is responsible for showing and hiding the controls on a tab to simulate moving between tabs, making it look like the tab is a container for the controls. However, tabs are not containers for the groups or controls. Tabs are controls that are displayed in a certain way, making them look like control containers.
