---
title: "ICWBoltConnector Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html"
---

# ICWBoltConnector Interface Members

The following tables list the members exposed by [ICWBoltConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AllowDistributedCoupling | Obsolete. Superseded by ICWBoltConnector::AllowDistributedCoupling2 . |
| Property | AllowDistributedCoupling2 | Gets whether distributed coupling is allowed. |
| Property | BoltShankDiameterUnit | Gets or sets the units for the bolt shank diameter. |
| Property | BoltShankDiameterValue | Gets or sets the bolt shank diameter. |
| Property | BoltType | Gets or sets the bolt type. |
| Property | BoltUnit | Gets or sets the bolt unit. |
| Property | ConnectionType | Sets the connection type. |
| Property | FrictionValue | Gets or sets the friction factor used to calculate the axial force from a given torque. |
| Property | HeadDiameterUnit | Gets or sets the unit for the diameter of the bolt's head. |
| Property | HeadDiameterValue | Gets or sets the diameter of the bolt's head. |
| Property | IncludeBoltSeries | Gets or sets whether to bolt more than two components together. |
| Property | IncludeKnownTensileStressArea | Gets or sets whether to include known tensile stress area. |
| Property | IncludeMass | Gets whether to include the mass of this bolt connector. |
| Property | IncludeStrengthData | Gets or sets whether to include strength data. |
| Property | IncludeSymmetricalBolt | Gets or sets whether to define a symmetric bolt if one or two planes of symmetry cut through the bolt. |
| Property | IncludeTightFit | Gets or sets whether to include tight fit if the radius of the shank is equal to the radius of the cylindrical faces associated with at least one of the components. |
| Property | MassValue | Gets or sets the value of mass. |
| Property | MaterialSource | Gets or sets the material source. |
| Property | MaterialType | Gets or sets the material type. |
| Property | MaterialUnit | Gets or sets the material unit. |
| Property | NutDiameterUnit | Gets or sets the unit for the nut's diameter. |
| Property | NutDiameterValue | Gets or sets the diameter of the bolt's nut. |
| Property | PinBoltStrengthUnit | Gets or sets the strength of the bolt. |
| Property | PoissonsRatio | Gets or sets Poisson's ratio for the custom material. |
| Property | PreLoadForceType | Gets or sets the type of preload force. |
| Property | PreLoadForceValue | Gets or set the value of the pre-load force. |
| Property | SameHeadAndNutDiameter | Gets or sets whether the head and nut of the bolt are the same diameter. |
| Property | SymmetricalBoltType | Gets or sets the type of symmetric bolt. |
| Property | TensileStressAreaUnit | Gets or sets the unit of the tensile stress area. |
| Property | ThermalCoefficient | Gets or sets the thermal expansion coefficient for the custom material. |
| Property | ThreadsPerLengthUnit | Gets or sets the threads/length unit. |
| Property | YoungModulus | Gets or sets the Young modulus for the custom material. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | BoltConnectorBeginEdit | Starts editing a bolt connector. |
| Method | BoltConnectorEndEdit | Ends editing a bolt connector. |
| Method | GetBoltSeriesEntityCount | Gets the number of bolt series for this bolt connector. |
| Method | GetLibraryMaterial | Gets the material for this bolt connector. |
| Method | GetSourceEntityCount | Gets the number of source entities for this bolt connector. |
| Method | GetStrengthData | Gets the strength data for this bolt connector. |
| Method | GetTargetEntityCount | Gets the number of target entities for this bolt connector. |
| Method | InsertBoltSeriesEntity | Inserts an entity (cylindrical face from the middle components) in the bolt series. |
| Method | InsertEntityAtFirstLocation | Inserts a source entity at the first location. |
| Method | InsertEntityAtSecondLocation | Inserts a target entity at the second location. |
| Method | InsertReferenceGeometry | Inserts the entity (plane or planar face of symmetry) for symmetrical bolts. |
| Method | InsertTightFitEntity | Inserts the entity (shank contact face) for a tight fit. |
| Method | RemoveBoltSeriesEntity | Removes the entity at the specified index from a bolt series. |
| Method | RemoveEntityAtFirstLocation | Removes the source entity at the specified index at the first location. |
| Method | RemoveEntityAtSecondLocation | Removes the target entity at the specified index at the second location. |
| Method | RemoveTightFitEntity | Removes the entity at the specified index from a tight fit. |
| Method | SetLibraryMaterial | Sets the material for this bolt connector. |
| Method | SetStrengthData | Sets the strength data for this bolt connector. |

[Top](#topBookmark)

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
