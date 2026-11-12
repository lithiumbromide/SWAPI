---
title: "Sorting Tables"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Sorting_Tables.htm"
---

# Sorting Tables

#### To sort and re-sort a Bill of Materials (BOM) table:

1. Select a BOM table annotation in the graphics area.
2. Call [ISelectionMgr::GetSelectedObject6](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html) to get the selected [ITableAnnotation](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html).
3. Cast the selected [ITableAnnotation](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html) object to an [IBomTableAnnotation](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html).
4. Call [IBomTableAnnotation::GetBomTableSortData](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetBomTableSortData.html) to create an [IBomTableSortData](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.html) object.
5. Set the properties of [IBomTableSortData](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.html) to define the sort.
6. (Optional) Set [IBomTableSortData::SaveCurrentSortParameters](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData~SaveCurrentSortParameters.html) to true to save the sort settings to the BOM table in the document during the sort. This allows you to re-sort the table at a later date. See step 8.
7. Sort the table by calling [IBomTableAnnotation::Sort](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Sort.html), passing the [IBomTableSortData](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.html) object in SortData.
8. To re-sort the table at a later date, you can perform steps 1-7. But if you previously performed steps 6 and 7 to save the sort settings to the BOM table, you can quickly re-sort the table by only performing steps 1-4 and calling [IBomTableAnnotation::ApplySavedSortScheme](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~ApplySavedSortScheme.html), which applies the sort settings saved in the BOM table.

#### To sort a hole table:

1. Select a hole table annotation in the graphics area.
2. Call [ISelectionMgr::GetSelectedObject6](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html) to get the selected [ITableAnnotation](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html).
3. Cast the selected [ITableAnnotation](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html) object to an [IHoleTableAnnotation](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTableAnnotation.html).
4. Because hole tables must be sorted on the Tag column, call [IHoleTableAnnotation::Sort(ColumnIndex, SortAscending)](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTableAnnotation~Sort.html), where ColumnIndex = 0 and SortAscending = true for an ascending sort.

#### To sort a general table:

1. Select a general table annotation in the graphics area.
2. Call [ISelectionMgr::GetSelectedObject6](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html) to get the selected [ITableAnnotation](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html).
3. Cast the selected [ITableAnnotation](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html) object to an [IGeneralTableAnnotation](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableAnnotation.html).
4. Call [IGeneralTableAnnotation::Sort](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableAnnotation~Sort.html).

#### To sort a weldment cut list table:

1. Select a weldment cut list table annotation in the graphics area.
2. Call [ISelectionMgr::GetSelectedObject6](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html) to get the selected [ITableAnnotation](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html).
3. Cast the selected [ITableAnnotation](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html) object to an [IWeldmentCutListAnnotation](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation.html).
4. Because weldment cut list tables must be sorted on any column except Item Number, call [IWeldmentCutListAnnotation::Sort(ColumnIndex, SortAscending)](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~Sort.html), where ColumnIndex > 0 and SortAscending = true for an ascending sort.
