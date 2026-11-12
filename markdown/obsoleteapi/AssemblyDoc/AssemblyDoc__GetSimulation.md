---
title: "AssemblyDoc::GetSimulation"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDoc/AssemblyDoc__GetSimulation.htm"
---

# AssemblyDoc::GetSimulation

This method is:

- obsolete and has not been superseded.
- nonfunctional in SolidWorks 2008 and later.

  Use the interfaces related to motion studies introduced in SolidWorks 2008 to access animation and simulation.

Description

This method gets the Simulation folder.

Syntax (OLE Automation)

retval = AssemblyDoc.GetSimulation ()

| Output: | (LPSIMULATION) retval | Pointer to the Simulation object |
| --- | --- | --- |

Syntax (COM)

status = AssemblyDoc->GetSimulation ( &retval)

| Output: | (LPSIMULATION) retval | Pointer to the Simulation object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The Simulation interface for the Simulation folder is returned even if the folder does not yet exist or does not currently appear in the FeatureManager design tree.
