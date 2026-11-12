---
title: "Simulation::Status"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Simulation/Simulation__Status.htm"
---

# Simulation::Status

This property is:

- obsolete and has not been superseded.
- nonfunctional in SolidWorks 2008 and later.

  Use the interfaces related to motion studies introduced in SolidWorks 2008 to access animation and simulation.

Description

This property gets the status of the Physical Simulation.

Syntax (OLE Automation)

Retval = Simulation.Status (VB Get property)

Retval = Simulation.GetStatus ( ) (C++ Get property)

| Output: | (VARIANT_BOOL) Retval | TRUE if the Physical Simulation has been calculated, FALSE if it has not or if the calculation was unsuccessful |
| --- | --- | --- |

Syntax (COM)

status = Simulation->get_Status ( &Retval )

| Output: | (VARIANT_BOOL) Retval | TRUE if the Physical Simulation has been calculated, FALSE if it has not or if the calculation was unsuccessful |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
