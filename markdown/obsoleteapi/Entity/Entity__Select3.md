---
title: "Entity::Select3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Entity/Entity__Select3.htm"
---

# Entity::Select3

This method is obsolete and has been superseded by [Entity::Select4](sldworksAPI.chm::/Entity/Entity__Select4.htm).

Description

This method selects this entity and marks it.

Syntax (OLE Automation)

retval = Entity.Select3 ( Append, Mark, Callout )

| Input: | (BOOL) Append | TRUE appends the entity to the selection list, FALSE replaces the current selection list |
| --- | --- | --- |
| Input: | (long) Mark | Value that you want to use as a selection mark |
| Input: | (LPCALLOUT) Callout | Pointer to the associated callout |
| Output: | (VARIANT_BOOL) retval | TRUE if the entity was selected, FALSE if not |

Syntax (COM)

status = Entity->Select3 ( Append, Mark, Callout, &retval )

| Input: | (VARIANT_BOOL) Append | TRUE appends the entity to the selection list, FALSE replaces the current selection list |
| --- | --- | --- |
| Input: | (long) Mark | Value that you want to use as a selection mark |
| Input: | (LPCALLOUT) Callout | Pointer to the associated callout |
| Output: | (VARIANT_BOOL) retval | TRUE if the entity was selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

When you use this method, selection behaves differently depending on the command

state of SolidWorks. One case is when SolidWorks is running a command that has a

dialog box associated with a selection list box (for example, a feature creation

command such as InsertFillet). The selection behavior in this case is:

- Selecting a new entity appends it to the selection list.
  - or -
- Selecting an entity that is already selected deselects the entity.

SolidWorks ignores the Append argument because the selection is always appended to

the selection list.

The second case is when there is no command running, which is the default state of

SolidWorks. The original Entity::Select worked this way:

- Selecting a new entity replaces or appends the selection list depending on the Append argument.
  - or -
- Selecting an entity that is already selected has no effect.

The mark value of a selection is used by some functions that require multiple selections

(for example, the Insert Draft command uses selection marks). The mark value indicates

which selection belongs to which selection box, so the Mark argument applies only

to certain situations within the first case. If the Mark argument is not used, pass 0 for this argument.

You can use this method only with entity objects that you get from the active document.

In other words, if Assembly1 is the active document when you call Entity::Select3,

then you must get the entity directly from the Assembly1 document. You can do this

using items in the selection list (for example, SelectionMGr::GetSelectedObject3) or you can traverse the body of an assembly component (for example, Component2::GetBody and Body2::GetFirstFace). You cannot obtain the entity from the underlying part document (for example, Component2::GetModelDoc, PartDoc::Body, or Body2::GetFirstFace).
