---
title: "IDimension Interface Members"
project: "SOLIDWORKS API Help"
interface: "IDimension_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html"
---

# IDimension Interface Members

The following tables list the members exposed by [IDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | DimensionLineDirection | Gets or sets the direction of this dimension line. |
| Property | DrivenState | Gets or sets the driven state of a dimension. |
| Property | ExtensionLineDirection | Gets or sets the direction of the extension line. |
| Property | FullName | Gets the full name of a dimension including the feature and the model. |
| Property | Name | Gets or sets the name of a dimension. |
| Property | ReadOnly | Gets or sets the read-only state of a dimension. |
| Property | ReferencePoints | Gets or sets the reference points for this dimension. |
| Property | SystemValue | Obsolete. Superseded by IDimension::GetSystemValue3 , IDimension::IGetSystemValue3 , IDimension::SetSystemValue3 , and IDimension::ISetSystemValue3 . |
| Property | Tolerance | Gets the IDimensionTolerance object. |
| Property | Value | Obsolete. Superseded by IDimension::GetValue3 , IDimension::IGetValue3 , IDimension::ISetValue3 , and IDimension::SetValue3 . |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetArcEndCondition | Gets the end conditions for linear dimensions that end on an arc. |
| Method | GetFeatureOwner | Gets the feature for this dimension. |
| Method | GetNameForSelection | Gets the name of the selected dimension needed by IModelDocExtension::SelectByID2 . |
| Method | GetReferencePointsCount | Gets the number of reference points for this dimension. |
| Method | GetSystemChamferValues | Gets the chamfer dimension values in system units. |
| Method | GetSystemValue2 | Obsolete. See IDimension::GetSystemValue3 and IDimension::IGetSystemValue3 . |
| Method | GetSystemValue3 | Gets the value of the current dimension in system units in the named configuration. |
| Method | GetToleranceFitValues | Obsolete. Superseded by IDimensionTolerance::GetHoleFitValue and IDimensionTolerance::GetShaftFitValue . |
| Method | GetToleranceFontInfo | Obsolete. Superseded by IDimensionTolerance::GetFontUseDimension , IDimensionTolerance::GetFontUseScale , IDimensionTolerance::GetFontScale , and IDimensionTolerance::GetFontHeight . |
| Method | GetToleranceType | Obsolete. Superseded by IDimensionTolerance::Type . |
| Method | GetToleranceValues | Obsolete. Superseded by IDimensionTolerance::GetMaxValue and IDimensionTolerance::GetMinValue . |
| Method | GetType | Gets the type of dimension. |
| Method | GetUserValueIn | Gets the value of this dimension in the units of the specified document. |
| Method | GetValue2 | Obsolete. Superseded by IDimension::GetValue3 and IDimension::IGetValue3 . |
| Method | GetValue3 | Gets the values of the dimensions in the specified configurations. |
| Method | IGetReferencePoints | Gets the reference points for this dimension. |
| Method | IGetSystemValue3 | Gets the value of the current dimension in system units in the named configuration. |
| Method | IGetToleranceFontInfo | Obsolete. Superseded by IDimensionTolerance::GetFontUseDimension , IDimensionTolerance::GetFontUseScale , IDimensionTolerance::GetFontScale , and IDimensionTolerance::GetFontHeight . |
| Method | IGetToleranceValues | Obsolete. Superseded by IDimensionTolerance::GetMaxValue and IDimensionTolerance::GetMinValue . |
| Method | IGetUserValueIn | Obsolete. Superseded by IDimension::IGetUserValueIn2 . |
| Method | IGetUserValueIn2 | Gets the value of this dimension in the units of the specified document. |
| Method | IGetValue3 | Gets the values of the dimensions in the specified configurations. |
| Method | IsAppliedToAllConfigurations | Gets whether a dimension is currently applied to all configurations of the model or to just the current configuration. |
| Method | IsDesignTableDimension | Gets whether this dimension is driven by a design table. |
| Method | ISetReferencePoints | Sets the reference points for this dimension. |
| Method | ISetSystemValue3 | Sets the value of this dimension in system units (meters) in the specified configuration. |
| Method | ISetUserValueIn | Obsolete. Superseded by IDimension::ISetUserValueIn3 . |
| Method | ISetUserValueIn2 | Obsolete. Superseded by IDimension::ISetUserValueIn3 . |
| Method | ISetUserValueIn3 | Sets the value of this dimension in the units of the specified document. |
| Method | ISetValue3 | Sets the values of the dimensions in the specified configurations. |
| Method | IsReference | Gets whether the dimension is a reference dimension. |
| Method | SetArcEndCondition | Sets the end conditions for linear dimensions that end on an arc. |
| Method | SetSystemValue2 | Obsolete. Superseded by IDimension::SetSystemValue3 . |
| Method | SetSystemValue3 | Sets the value of this dimension in system units (meters) in the specified configuration. |
| Method | SetToleranceFitValues | Obsolete. Superseded by IDimensionTolerance::SetFitValues . |
| Method | SetToleranceFontInfo | Obsolete. Superseded by IDimensionTolerance::SetFont . |
| Method | SetToleranceType | Obsolete. Superseded by IDimensionTolerance::Type . |
| Method | SetToleranceValues | Obsolete. Superseded by IDimensionTolerance::SetValues . |
| Method | SetUserValueIn | Obsolete. Superseded by IDimension::SetUserValueIn2 . |
| Method | SetUserValueIn2 | Sets the value of this dimension in the units of the specified document. |
| Method | SetValue2 | Obsolete. Superseded by IDimension::SetValue3 . |
| Method | SetValue3 | Sets the values of the dimensions in the specified configurations. |

[Top](#topBookmark)

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.html)
