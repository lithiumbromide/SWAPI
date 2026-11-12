---
title: "Simulation::GetFeature"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Simulation/Simulation__GetFeature.htm"
---

# Simulation::GetFeature

This method is:

- obsolete and has not been superseded.
- nonfunctional in SolidWorks 2008 and later.

  Use the interfaces related to motion studies introduced in SolidWorks 2008 to access animation and simulation.

Description

This method gets the feature that provides you access to the Physical Simulation.

Syntax (OLE Automation)

Retval = Simulation.GetFeature ()

| Output: | (LPFEATURE) Retval | Pointer to the Feature object |
| --- | --- | --- |

Syntax (COM)

status = Simulation->GetFeature ( &Retval)

| Output: | (LPFEATURE) Retval | Pointer to the Feature object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

After using this method to get the feature, use either of the following methods to get the Simulation interface:

- Feature::GetSpecificFeatue2
- AssemblyDoc::GetSimulation
