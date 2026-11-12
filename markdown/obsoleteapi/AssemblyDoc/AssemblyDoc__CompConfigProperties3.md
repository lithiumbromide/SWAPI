---
title: "AssemblyDoc::CompConfigProperties3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDoc/AssemblyDoc__CompConfigProperties3.htm"
---

# AssemblyDoc::CompConfigProperties3

This method is obsolete and has been superseded by [AssemblyDoc::CompConfigProperties4](sldworksAPI.chm::/AssemblyDoc/AssemblyDoc__CompConfigProperties4.htm).

Description

This method sets the configuration properties for the selected component.

Syntax (OLE Automation)

retval = AssemblyDoc.CompConfigProperties3 ( suppression, solving, visibility, featureDetails )

| Input: | (long) suppression | Suppression state of this component instance as defined in swComponentSuppressionState_e |
| --- | --- | --- |
| Input: | (long) solving | Solving state of the component as defined in swComponentSolvingOption_e |
| Input: | (BOOL) visibility | TRUE if you want to show the selected component in the graphics display area, if not If the selected component is a... Then... Part setting this option to TRUE or FALSE also sets the featureDetails parameter Sub-assembly You can hide the component in the graphics area and still show its details in the FeatureManager design tree |
| If the selected component is a... | Then... |  |
| Part | setting this option to TRUE or FALSE also sets the featureDetails parameter |  |
| Sub-assembly | You can hide the component in the graphics area and still show its details in the FeatureManager design tree |  |
| Input: | (BOOL) featureDetails | TRUE if you want the feature details for this component to be displayed in the FeatureManager design tree, FALSE if you want to see only the component name in the FeatureManager design tree If the selected component is a... Then... Part setting this option to TRUE or FALSE also sets the visibility parameter Sub-assembly You can hide the feature details in the FeatureManager design tree and still show the component in the graphics area |
| If the selected component is a... | Then... |  |
| Part | setting this option to TRUE or FALSE also sets the visibility parameter |  |
| Sub-assembly | You can hide the feature details in the FeatureManager design tree and still show the component in the graphics area |  |
| Return: | (BOOL) retval | TRUE if successful, FALSE if not |

Syntax (COM)

status = AssemblyDoc->CompConfigProperties3 ( suppression, solving, visibility, featureDetails, &retval )

| Input: | (long) suppression | Suppression state of this component instance as defined in swComponentSuppressionState_e. |
| --- | --- | --- |
| Input: | (long) solving | Solving state of the component as defined in swComponentSolvingOption_e. |
| Input: | (VARIANT_BOOL) visibility | TRUE if you want to show the selected component in the graphics display area, if not If the selected component is a... Then... Part setting this option to TRUE or FALSE also sets the featureDetails parameter Sub-assembly You can hide the component in the graphics area and still show its details in the FeatureManager design tree |
| If the selected component is a... | Then... |  |
| Part | setting this option to TRUE or FALSE also sets the featureDetails parameter |  |
| Sub-assembly | You can hide the component in the graphics area and still show its details in the FeatureManager design tree |  |
| Input: | (VARIANT_BOOL) featureDetails | TRUE if you want the feature details for this component to be displayed in the FeatureManager design tree, FALSE if you want to see only the component name in the FeatureManager design tree If the selected component is a... Then... Part setting this option to TRUE or FALSE also sets the visibility parameter Sub-assembly You can hide the feature details in the FeatureManager design tree and still show the component in the graphics area |
| If the selected component is a... | Then... |  |
| Part | setting this option to TRUE or FALSE also sets the visibility parameter |  |
| Sub-assembly | You can hide the feature details in the FeatureManager design tree and still show the component in the graphics area |  |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can use configurations to save certain display characteristics with each of the assembly components and retrieve that configuration in the future. SolidWorks applies the settings that you specify with this method to the active configuration.

You cannot set a component to LightWeight (that is, m_suppressed = swComponentLightweight is not valid).

Known reasons for failure of this method include:

- Invalid suppression state specified
- Not preselecting a component
