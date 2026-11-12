---
title: "DrawingDoc::InsertModelAnnotations2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__InsertModelAnnotations2.htm"
---

# DrawingDoc::InsertModelAnnotations2

This method is obsolete and has been superseded by [DrawingDoc::InsertModelAnnotations3](sldworksAPI.chm::/DrawingDoc/DrawingDoc__InsertModelAnnotations3.htm).

Description

This method inserts model annotations into this drawing document.

Syntax (OLE Automation)

ok = DrawingDoc.InsertModelAnnotations2 ( option, allTypes, types, allViews, duplicateDims, hiddenFeatureDims)

| Input: | (long) option | 0 - All dimensions in the view 1 - All dimensions of the currently selected component (for assembly drawings) 2 - All dimensions of the currently selected feature |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) allTypes | TRUE to insert all types of annotations, FALSE uses the types argument |
| Input: | (long) types | Bitwise OR of annotation types as defined in swInsertAnnotation_e |
| Input: | (VARIANT_BOOL) allViews | TRUE to insert the annotations in all views in the drawing, FALSE to insert annotations only in the selected view |
| Input: | (VARIANT_BOOL) duplicateDims | TRUE to insert duplicate dimensions, FALSE to eliminate duplicate dimensions |
| Input: | (VARIANT_BOOL) hiddenFeatureDims | TRUE to insert dimensions from features that are hidden, FALSE to not insert dimensions from features that are hidden |
| Output: | (VARIANT_BOOL) ok | TRUE if the annotations were added, FALSE if not |

Syntax (COM)

status = DrawingDoc->InsertModelAnnotations2 ( option, allTypes, types, allViews, duplicateDims, hiddenFeatureDims, &ok)

| Input: | (long) option | 0 - All dimensions in the view 1 - All dimensions of the currently selected component (for assembly drawings) 2 - All dimensions of the currently selected feature |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) allTypes | TRUE to insert all types of annotations, FALSE uses the types argument |
| Input: | (long) types | Bitwise OR of annotation types as defined in swInsertAnnotation_e |
| Input: | (VARIANT_BOOL) allViews | TRUE to insert the annotations in all views in the drawing, FALSE to insert annotations only in the selected view |
| Input: | (VARIANT_BOOL) duplicateDims | TRUE to insert duplicate dimensions, FALSE to eliminate duplicate dimensions |
| Input: | (VARIANT_BOOL) hiddenFeatureDims | TRUE to insert dimensions from features that are hidden, FALSE to not insert dimensions from features that are hidden |
| Output: | (VARIANT_BOOL) ok | TRUE if the annotations were added, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
