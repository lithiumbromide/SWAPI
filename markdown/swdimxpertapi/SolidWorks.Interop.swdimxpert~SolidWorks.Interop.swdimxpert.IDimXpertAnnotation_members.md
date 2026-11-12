---
title: "IDimXpertAnnotation Interface Members"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAnnotation_members"
member: ""
kind: "members"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation_members.html"
---

# IDimXpertAnnotation Interface Members

The following tables list the members exposed by [IDimXpertAnnotation](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Feature | Gets the DimXpert feature to which this DimXpert annotation is applied. |
| Property | Name | Gets the name of this DimXpert annotation. |
| Property | Type | Gets the type of this DimXpert annotation. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetAppliedAnnotationCount | Gets the number of annotations applied to this DimXpert annotation. |
| Method | GetAppliedAnnotations | Gets all of the annotations that reference this DimXpert annotation (datum). |
| Method | GetDisplayEntity | Gets the SOLIDWORKS annotation representing this DimXpert annotation. |
| Method | GetModelFeature | Gets the underlying DimXpert model feature that corresponds to this geometric, dimensioning, and tolerancing annotation. |
| Method | IGetAppliedAnnotations | Gets all of the annotations applied to this DimXpert annotation. |
| Method | IsFreeState | Gets whether this annotation is in a free state. |
| Method | IsStatistical | Gets whether this annotation is statistical. |
| Method | IsSuppressed | Gets whether the annotation is suppressed from view on the DimXpertManager tab of the Management Panel. |
| Method | IsToBeInspected | Gets whether this annotation is to be inspected. |

[Top](#topBookmark)

## See Also

[IDimXpertAnnotation Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation.html)
[SolidWorks.Interop.swdimxpert Namespace](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert_namespace.html)
