---
title: "Entity::Select"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Entity/Entity__Select.htm"
---

# Entity::Select

This method is obsolete and has been superseded by [Entity::Select2](Entity__Select2.htm).

Description

This method selects the entity and either appends it to the selection list or replaces the entire selection list.

Syntax (OLE Automation)

retval = Entity.Select ( appendFlag )

| Input: | (BOOL) appendFlag | TRUE if the entity is to be appended to the selection list, FALSE if the entity replaces the selection list |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the entity was selected, FALSE if not |

Syntax (COM)

status = Entity->Select ( appendFlag, &retval )

| Input: | (VARIANT_BOOL) appendFlag | TRUE if the entity is to be appended to the selection list, FALSE if the entity replaces the selection list |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the entity was selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can use this method to select features. In VC++, you must first get the entity interface from the Feature object. To select features, you can also use ModelDoc2::SelectByID with the feature name, feature type and 0,0,0 coordinates.

You can use this method only with Entity objects that you get from the active document. For example, if Assembly1 is the active document when you call Entity::Select, then you must get the entity directly from the Assembly1 document. You can do this using items in the selection list (for example, SelectionMgr::GetSelectedObject3) or you can traverse the body of an assembly component (for example, Component2::GetBody and Body2::GetFirstFace). You cannot obtain the entity from the underlying part document (for example, Component2::GetModelDoc, PartDoc::Body, and Body2::GetFirstFace).
