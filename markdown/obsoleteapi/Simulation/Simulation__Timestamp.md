---
title: "Simulation::Timestamp"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Simulation/Simulation__Timestamp.htm"
---

# Simulation::Timestamp

This property is:

- obsolete and has not been superseded.
- nonfunctional in SolidWorks 2008 and later.

  Use the interfaces related to motion studies introduced in SolidWorks 2008 to access animation and simulation.

Description

This property gets the unique time stamp for this Physical Simulation.

Syntax (OLE Automation)

Retval = Simulation.Timestamp (VB Get property)

Retval = Simulation.GetTimestamp ( ) (C++ Get property)

| Output: | (long) Retval | Time stamp for this Physical Simulation (see Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = Simulation->get_Timestamp ( &Retval )

| Output: | (long) Retval | Time stamp for this Physical Simulation (see Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

| If a... | Then... |
| --- | --- |
| New Physical Simulation is calculated | The time stamp (Retval) changes |
| Physical Simulation does not exist or it was deleted | 0 is returned |
| Physical Simulation was created using SolidWorks 2005 or earlier | -1 is returned |
