---
title: "Simulation::ResetComponents"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Simulation/Simulation__ResetComponents.htm"
---

# Simulation::ResetComponents

This method is:

- obsolete and has not been superseded.
- nonfunctional in SolidWorks 2008 and later.

  Use the interfaces related to motion studies introduced in SolidWorks 2008 to access animation and simulation.

Description

This method resets the components to the positions and orientations they were in prior to creating the Physical Simulation.

Syntax (OLE Automation)

Retval = Simulation.ResetComponents ()

| Output: | (VARIANT_BOOL) Retval | TRUE if the components' positions and orientations are reset, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = Simulation->ResetComponents ( &Retval)

| Output: | (VARIANT_BOOL) Retval | TRUE if the components' positions and orientations are reset, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
