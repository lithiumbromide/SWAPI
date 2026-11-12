---
title: "ICWRemoteLoad Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html"
---

# ICWRemoteLoad Interface Members

The following tables list the members exposed by [ICWRemoteLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AllowDistributedCoupling | Obsolete. Superseded by ICWRemoteLoad::AllowDistributedCoupling2 . |
| Property | AllowDistributedCoupling2 | Gets whether distributed coupling is allowed for the current study. |
| Property | ConnectionType | Sets the connection type of this remote load. |
| Property | ForceOrTranslationUnit | Sets the units of force or translation for this remote load. |
| Property | ForceUnit | Sets the units of force for this remote load. |
| Property | LoadType | Gets or sets the type of remote load. |
| Property | LocationUnit | Gets or sets the units of remote location. |
| Property | MassUnit | Gets or sets the unit system for remote mass. |
| Property | MomentOrRotationUnit | Sets the units of moment or rotation for this remote load. |
| Property | MomentUnit | Sets the units of moment for this remote load. |
| Property | RotationUnit | Sets the units of rotation for this remote load. |
| Property | TranslationUnit | Sets the units of translation for this remote load. |
| Property | WeightingFactor | Sets the weighting factor for the distributed coupling of this remote load. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetForceOrTranslationValues | Obsolete. Superseded by ICWRemoteLoad::GetForceOrTranslationValues2 . |
| Method | GetForceOrTranslationValues2 | Gets the components of force or translation for this remote load. |
| Method | GetLocationValues | Gets the coordinates of the point of application of this remote load. |
| Method | GetMassValues | Obsolete. Superseded by ICWRemoteLoad::GetMassValues2 . |
| Method | GetMassValues2 | Gets the components of mass in this remote load. |
| Method | GetMomentOrRotationValues | Obsolete. Superseded by ICWRemoteLoad::GetMomentOrRotationValues2 . |
| Method | GetMomentOrRotationValues2 | Gets the components of moment or rotation for this remote load. |
| Method | GetReferenceCoordinateSystem |  |
| Method | GetReferenceCoordinateSystem2 |  |
| Method | GetTimeOrFrequencyCurve | Gets the variation with time or frequency of this remote load. |
| Method | InsertEntity | Adds a face, edge, or vertex to the collection of entities to which this remote load is applied. |
| Method | RemoteLoadBeginEdit | Starts editing remote load. |
| Method | RemoteLoadEndEdit | Stops editing remote load. |
| Method | RemoveEntity | Removes a face, edge, or vertex from the collection of entities to which this remote load is applied. |
| Method | SetForceOrTranslationValues | Obsolete. Superseded by ICWRemoteLoad::SetForceOrTranslationValues2 . |
| Method | SetForceOrTranslationValues2 | Sets the components of force or translation for this remote load. |
| Method | SetForceOrTranslationValuesEx | Obsolete. Superseded by ICWRemoteLoad::SetForceOrTranslationValuesEx2 . |
| Method | SetForceOrTranslationValuesEx2 | Sets the components of force or translation for this remote load of a linear static, topology, or nonlinear static study. |
| Method | SetLocationValues | Sets the coordinates of the point of application of this remote load. |
| Method | SetMassValues | Obsolete. Superseded by ICWRemoteLoad::SetMassValues2 . |
| Method | SetMassValues2 | Sets the components of mass in this remote load. |
| Method | SetMomentOrRotationValues | Obsolete. Superseded by ICWRemoteLoad::SetMomentOrRotationValues2 . |
| Method | SetMomentOrRotationValues2 | Sets the components of moment or rotation for this remote load. |
| Method | SetMomentOrRotationValuesEx | Obsolete. Superseded by ICWRemoteLoad::SetMomentOrRotationValuesEx2 . |
| Method | SetMomentOrRotationValuesEx2 | Sets the components of moment or rotation for this remote load of a linear static, topology, or nonlinear static study. |
| Method | SetReferenceCoordinateSystem | Obsolete. Superseded by ICWRemoteLoad::SetReferenceCoordinateSystem2 . |
| Method | SetReferenceCoordinateSystem2 | Sets the coordinate system used for interpreting the location and direction of the remote load, mass, or displacement. |
| Method | SetTimeOrFrequencyCurve | Obsolete. Superseded by ICWRemoteLoad::SetTimeOrFrequencyCurve2 . |
| Method | SetTimeOrFrequencyCurve2 | Sets the variation with time or frequency of this remote load. |

[Top](#topBookmark)

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
