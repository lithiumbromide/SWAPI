---
title: "Document Properties > Units"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_Units.htm"
---

# Document Properties > Units

HTML PUBLIC "-//W3C//DTD HTML 4.0 Frameset//EN"

(==============================================================)

(Table)=========================================================

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Unit system | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitSystem,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitSystem,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swUnitSystem_e.< Value >) | See swUnitSystem_e for valid options | Specifies type of system unit |
| Basic Units - Length - Unit | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsLinear,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsLinear,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLengthUnit_e.< Value >) | See swLengthUnit_e for valid options | Specifies the type of linear length units |
| Basic Units - Length - Decimals or fractions? | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsLinearDecimalDisplay,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsLinearDecimalDisplay,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swFractionDisplay_e.< Value >) | See swFractionDisplay_e for valid options | Specifies decimal or fraction display for linear units |
| Basic Units - Length - Decimals | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsLinearDecimalPlaces,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsLinearDecimalPlaces,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Integer value (0 - 8) | Specifies the number of decimal places for linear units |
| Basic Units - Length - Fractions | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsLinearFractionDenominator,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsLinearFractionDenominator,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Integer value | Specifies the default denominator for linear fractions |
| Basic Units - Length - More - Convert feet
and inches format | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swUnitsLinearFeetAndInchesFormat,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swUnitsLinearFeetAndInchesFormat,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to change format of linear feet and inches |
| Basic Units - Length - More - Round to nearest fraction | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swUnitsLinearRoundToNearestFraction,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swUnitsLinearRoundToNearestFraction,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to round linear units to the nearest fraction |
| Basic Units - Dual Dimension Length - Unit | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsDualLinear,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsDualLinear,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLengthUnit_e.< Value >) | See swLengthUnit_e for valid options | Specifies type of dual linear length units |
| Basic Units - Dual Dimension Length - Decimals or fractions? | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsDualLinearDecimalDisplay,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsDualLinearDecimalDisplay,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swFractionDisplay_e.< Value >) | See swFractionDisplay_e for valid options | Specifies decimal or fraction display for dual linear units |
| Basic Units - Dual Dimension Length - Decimals | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsDualLinearDecimalPlaces,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsDualLinearDecimalPlaces,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Integer value (0 - 8) | Specifies the number of decimal places for dual linear units |
| Basic Units - Dual Dimension Length - Fractions | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsDualLinearFractionDenominator,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsDualLinearFractionDenominator,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Integer value | Specifies the default denominator for dual linear fractions |
| Basic Units - Dual Dimension Length - More - Round to nearest fraction | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swUnitsDualLinearRoundToNearestFraction,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swUnitsDualLinearRoundToNearestFraction,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to round dual linear units to the nearest fraction |
| Basic Units - Dual Dimension Length - More - Convert feet and inches
format | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swUnitsDualLinearFeetAndInchesFormat,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swUnitsDualLinearFeetAndInchesFormat,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to change format of dual linear feet and inches |
| Basic Units - Angle - Unit | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsAngular,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsAngular,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swAngleUnit_e.< Value >) | See swAngleUnit_e for valid options | Specifies angular units |
| Basic Units - Angle - Decimals | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsAngularDecimalPlaces,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsAngularDecimalPlaces,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Integer value (0 - 8) | Specifies the number of decimal places for angular units |
| Mass/Section Properties - Length - Unit | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsMassPropLength,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsMassPropLength,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLengthUnit_e.< Value >) | See swLengthUnit_e for valid options | Specifies type of length unit to use for mass property units NOTE: You can only set this option when swUnitSystem_e is swUnitSytem_Custom; Otherwise, FALSE is returned |
| Mass/Section Properties - Length - Decimals | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsMassPropDecimalPlaces,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsMassPropDecimalPlaces,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Integer value (0 - 8) | Specifies number of decimal places for mass property units |
| Mass/Section Properties - Mass - Unit | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsMassPropMass,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsMassPropMass,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swUnitsMassPropMass_e.< Value >) | See swUnitsMassPropMass_e for valid options | Specifies type of mass unit to use for mass property units NOTE: You can only set this option when swUnitSystem_e is swUnitSytem_Custom; Otherwise, FALSE is returned |
| Mass/Section Properties - Per Unit Volume - Unit | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsMassPropVolume,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsMassPropVolume,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swUnitsMassPropVolume_e.< Value >) | See swUnitsMassPropVolume_e for valid options | Specifies type of volume unit to use for mass property units NOTE: You can only set this option when swUnitSystem_e is swUnitSytem_Custom; Otherwise, FALSE is returned |
| Motion Analysis - Time - Unit | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsTimeUnits,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsTimeUnits,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swUnitsTimeUnit_e.< Value >) | See swUnitsTimeUnit_e for valid options | Specifies the type of time unit. NOTE: You can only set this option when swUnitSystem_e is swUnitSytem_Custom; Otherwise, FALSE is returned |
| Motion Analysis - Time - Decimals | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsTimeDecimalPlaces,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsTimeDecimalPlaces,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Integer value (0 - 8) | Specifies the number of decimal places for swUnitsTime |
| Motion Analysis - Force - Unit | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsForce,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsForce,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swUnitsForce_e.< Value >) | See swUnitsForce_e for valid options | Specifies the type of force units. NOTE: You can only set this option when swUnitSystem_e is swUnitSytem_Custom; Otherwise, FALSE is returned |
| Motion Analysis - Force - Decimals | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsForceDecimalPlaces,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsForceDecimalPlaces,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Integer value (0 - 8) | Specifies the number of decimal places for swUnitsForce |
| Motion Analysis - Power - Unit | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsPowerUnits,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsPowerUnits,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swUnitsPowerUnit_e.< Value >) | See swUnitsPowerUnit_e for valid options | Specifies type of power unit. NOTE: You can only set this option when swUnitSystem_e is swUnitSytem_Custom; Otherwise, FALSE is returned |
| Motion Analysis - Power - Decimals | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsPowerDecimalPlaces,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsPowerDecimalPlaces,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Integer value (0 - 8) | Specifies the number of decimal places for swUnitsPower |
| Motion Analysis - Energy - Unit | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsEnergyUnits,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsEnergyUnits,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swUnitsEnergyUnit_e.< Value >) | See swUnitsEnergyUnit_e for valid options | Specifies the type of energy units. NOTE: You can only set this option when swUnitSystem_e is swUnitSytem_Custom; Otherwise, FALSE is returned |
| Motion Analysis - Energy - Decimals | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swUnitsEnergyDecimalPlaces,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swUnitsEnergyDecimalPlaces,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Integer value (0 - 8) | Specifies the number of decimal places for swUnitsEnergy |
| Decimal rounding - Round half away from zero Round half towards zero Round half to even Truncate without rounding | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsDecimalRounding,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swUnitsDecimalRounding,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swUnitsDecimalRounding_e.< Value >) | See swUnitsDecimalRounding_e for valid options | Specifies decimal rounding method |
| Only apply rounding method to dimensions | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingNoDimSpecificOptionSpecified,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingNoDimSpecificOptionSpecified,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to apply the
specified decimal rounding method to: any numeric display where
rounding occurs, including dialogs. - or - dimensions on their tolerances, including dimensions whose values are derived from equations. NOTE : Check box is not available if Round half away from zero is selected. |
