---
title: "AssemblyDoc::CompConfigProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDoc/AssemblyDoc__CompConfigProperties.htm"
---

# AssemblyDoc::CompConfigProperties

This method is obsolete and has been superseded by [AssemblyDoc::CompConfigProperties2](AssemblyDoc__CompConfigProperties2.htm).

Description

This method sets the configuration properties for the selected component.

Syntax (OLE Automation)

void AssemblyDoc.CompConfigProperties ( m_suppressed, m_show_component, m_fdetail)

| Input: | (BOOL) m_suppressed | TRUE if you want the selected component suppressed, FALSE if not; if set to TRUE, the component is not used in any regeneration of the document |
| --- | --- | --- |
| Input: | (BOOL) m_show_component | TRUE if you want to show the selected component in the graphics display area, if not If the selected component is a... Then... Part Setting this option also sets the m_fdetail option Sub-assembly You can hide the component in the graphics area and still show its details in the FeatureManager design tree |
| If the selected component is a... | Then... |  |
| Part | Setting this option also sets the m_fdetail option |  |
| Sub-assembly | You can hide the component in the graphics area and still show its details in the FeatureManager design tree |  |
| Input: | (BOOL) m_fdetail | TRUE if you want the feature details for this component to be displayed in the FeatureManager design tree, FALSE if you want to see only the component name in the FeatureManager design tree. If the selected component is a... Then... Part Setting this option also sets the m_show_component option Sub-assembly You can hide the feature details in the FeatureManager design tree and still show the component in the graphics area |
| If the selected component is a... | Then... |  |
| Part | Setting this option also sets the m_show_component option |  |
| Sub-assembly | You can hide the feature details in the FeatureManager design tree and still show the component in the graphics area |  |

Syntax (COM)

status = AssemblyDoc->CompConfigProperties ( m_suppressed, m_show_component, m_fdetail )

| Input: | (VARIANT_BOOL) m_suppressed | TRUE if you want the selected component suppressed, FALSE if not; if set to TRUE, the component is not used in any regeneration of the document |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) m_show_component | TRUE if you want to show the selected component in the graphics display area, if not If the selected component is a... Then... Part Setting this option also sets the m_fdetail option Sub-assembly You can hide the component in the graphics area and still show its details in the FeatureManager design tree |
| If the selected component is a... | Then... |  |
| Part | Setting this option also sets the m_fdetail option |  |
| Sub-assembly | You can hide the component in the graphics area and still show its details in the FeatureManager design tree |  |
| Input: | (VARIANT_BOOL) m_fdetail | TRUE if you want the feature details for this component to be displayed in the FeatureManager design tree, FALSE if you want to see only the component name in the FeatureManager design tree. If the selected component is a... Then... Part Setting this option also sets the m_show_component option Sub-assembly You can hide the feature details in the FeatureManager design tree and still show the component in the graphics area |
| If the selected component is a... | Then... |  |
| Part | Setting this option also sets the m_show_component option |  |
| Sub-assembly | You can hide the feature details in the FeatureManager design tree and still show the component in the graphics area |  |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Configurations allow you to save certain display characteristics with each of the assembly components and retrieve that configuration in the future. SolidWorks uses the settings that you specify with this method and saves them to the active configuration.
