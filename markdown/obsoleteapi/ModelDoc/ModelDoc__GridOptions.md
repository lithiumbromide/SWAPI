---
title: "ModelDoc::GridOptions"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GridOptions.htm"
---

# ModelDoc::GridOptions

This method is obsolete and has been superseded by [ModelDoc2::GridOptions](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GridOptions.htm).

Description

This method sets the options for the grid.

Syntax (OLE Automation)

void ModelDoc.GridOptions ( dispGrid, gridSpacing, snap, dotStyle, nMajor, nMinor, align2edge, angleSnap, angleUnit, minorAuto)

| Input: | (BOOL) dispGrid | TRUE to display the grid, FALSE otherwise |
| --- | --- | --- |
| Input: | (double) gridSpacing | Snap distance |
| Input: | (BOOL) snap | TRUE to snap to grid, FALSE otherwise |
| Input: | (BOOL) dotStyle | TRUE for dotted grids, FALSE otherwise |
| Input: | (short) nMajor | Number of minors in major |
| Input: | (short) nMinor | Number of snaps in minor |
| Input: | (BOOL) align2edge | TRUE if to be aligned to an edge, FALSE otherwise |
| Input: | (BOOL) angleSnap | TRUE to snap to angle, FALSE otherwise |
| Input: | (double) angleUnit | Value of angle to which to snap |
| Input: | (BOOL) minorAuto | TRUE if the minor grids are to be set automatically, FALSE otherwise |

Syntax (COM)

status = ModelDoc->GridOptions ( dispGrid, gridSpacing, snap, dotStyle, nMajor, nMinor, align2edge, angleSnap, angleUnit, minorAuto )

| Input: | (VARIANT_BOOL) dispGrid | TRUE to display the grid, FALSE otherwise |
| --- | --- | --- |
| Input: | (double) gridSpacing | Snap distance |
| Input: | (VARIANT_BOOL) snap | TRUE to snap to grid, FALSE otherwise |
| Input: | (VARIANT_BOOL) dotStyle | TRUE for dotted grids, FALSE otherwise |
| Input: | (short) nMajor | Number of minors in major |
| Input: | (short) nMinor | Number of snaps in minor |
| Input: | (VARIANT_BOOL) align2edge | TRUE if to be aligned to an edge, FALSE otherwise |
| Input: | (VARIANT_BOOL) angleSnap | TRUE to snap to angle, FALSE otherwise |
| Input: | (double) angleUnit | Value of angle to which to snap |
| Input: | (VARIANT_BOOL) minorAuto | TRUE if the minor grids are to be set automatically, FALSE otherwise |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The align2edge parameter aligns the grid with the currently selected edge. If align2edge is set to TRUE, then you must have an edge selected.
