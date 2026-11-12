---
title: "ICWMaterial Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html"
---

# ICWMaterial Interface Members

The following tables list the members exposed by [ICWMaterial](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Category | Gets or sets the category of the material. |
| Property | Count | Gets the number of properties defined for this material. |
| Property | Description | Gets or sets the description for the material. |
| Property | IncludeCreep | Obsolete. Superseded by ICWMaterial::IncludeCreep2 . |
| Property | IncludeCreep2 | Gets or sets whether to include creep effect for the material model in nonlinear studies only. |
| Property | MaterialName | Gets or sets the name of the material name. |
| Property | MaterialUnits | Gets or sets the units for the material. |
| Property | ModelType | Gets or sets the material model. |
| Property | MooneyRivlinConstants | Gets or sets the Mooney Rivlin constants for the MooneyRivlin material model used in nonlinear studies only. |
| Property | NoOfBulkModuli | Gets or sets the number of bulk moduli for the viscoelastic material model used in nonlinear studies only. |
| Property | NoOfShearModuli | Gets or sets the number of shear moduli for the viscoelastic material model used in nonlinear studies only. |
| Property | OgdenConstants | Gets or sets the Ogden constants used for the Ogden material model used for nonlinear studies only. |
| Property | SNCurveEstimateConstants | Gets or sets whether to specify the Basquin Equation constants, B and slope (m), or let the program calculate them from the S-N curve. |
| Property | SNCurveEstimateCutoff | Gets or sets the cut-off point for estimating Basquin Eqation constants, B and slope (m). |
| Property | SNCurveSlopeM | Gets or sets the slope (m) of the S-N curve. |
| Property | SNCurveSource | Gets or sets the source for the material S-N curve used in fatigue studies. |
| Property | SNCurveSpecificConstantB | Gets or sets the B constant of the Basquin Equation. |
| Property | SNCurveSpecificConstantBUnit | Gets or sets the units of the Basquin Equation constants. |
| Property | Source | Returns the source of the material. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetAustenticSteelCurve | Gets the austentic steel curve data. |
| Method | GetCarbonSteelCurve | Gets the carbon steel curve data. |
| Method | GetFatigueSNCurve | Gets the fatigue S-N curve data for user-defined curve sources. |
| Method | GetMaterialDataCurve | Obsolete. Superseded by ICWMaterial::GetMaterialDataCurve3 . |
| Method | GetMaterialDataCurve3 | Gets the material data curve. |
| Method | GetPropertyByName | Obsolete. Superseded by er ICWMaterial::GetPropertyByName2 . |
| Method | GetPropertyByName2 | Gets the value of the material property by the property name. |
| Method | GetReferencePlaneName | Gets the name of the reference plane or reference axis used to specify material properties for orthotropic materials. |
| Method | GetStressStrainCurve | Gets the stress strain curve data. |
| Method | GetTemperatureCurveForProperty | Gets the temperature curve data for the material property. |
| Method | SetFatigueSNCurve | Sets the fatigue S-N curve data for user-defined curve sources. |
| Method | SetMaterialDataCurve | Obsolete. Superseded by ICWMaterial::SetMaterialDataCurve3 . |
| Method | SetMaterialDataCurve3 | Sets the material data curve. |
| Method | SetPropertyByName | Obsolete. Superseded by ICWMaterial::SetPropertyByName2 . |
| Method | SetPropertyByName2 | Sets the value of the specified material property. |
| Method | SetReferencePlane | Sets the name of the reference plane or reference axis used to specify material properties for orthotropic materials. |
| Method | SetStressStrainCurve | Sets the stress-strain curve data. |
| Method | SetTemperatureCurveForProperty | Sets the temperature curve data for the material property. |

[Top](#topBookmark)

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWSolidBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody.html)
[ICWBeamBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html)
