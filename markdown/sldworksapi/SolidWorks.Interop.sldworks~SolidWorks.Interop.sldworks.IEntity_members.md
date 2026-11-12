---
title: "IEntity Interface Members"
project: "SOLIDWORKS API Help"
interface: "IEntity_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity_members.html"
---

# IEntity Interface Members

The following tables list the members exposed by [IEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | IsSafe | Gets whether this IEntity object survived a rebuild. |
| Property | ModelName | Gets or sets the standard Parasolid name attribute of the entity. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | FindAttribute | Finds an attribute on an entity. |
| Method | GetComponent | Gets the owning component for this entity. |
| Method | GetDistance | Gets the minimum or maximum distance between this entity and the given face or edge entity (see Remarks ). |
| Method | GetDrawingComponent | Gets the drawing component that owns this entity, if the entity is in a drawing view. |
| Method | GetSafeEntity | Gets a safe entity. |
| Method | GetType | Gets the type of the entity. |
| Method | IFindAttribute | Finds an attribute on an entity. |
| Method | IGetComponent | Obsolete. Superseded by IEntity::IGetComponent2 . |
| Method | IGetComponent2 | Gets the owning component for this entity. |
| Method | IGetDistance | Gets the minimum or maximum distance between this entity and the given face or edge entity (see Remarks ). |
| Method | Select | Obsolete. Superseded by IEntity::Select4 . |
| Method | Select2 | Obsolete. Superseded by IEntity::Select4 . |
| Method | Select3 | Obsolete. Superseded by IEntity::Select4 . |
| Method | Select4 | Selects an entity and marks it. |

[Top](#topBookmark)

## See Also

[IEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
