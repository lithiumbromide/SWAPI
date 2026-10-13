---
title: "AssemblyDoc::GetPhysicalSimulationComponents"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDoc/AssemblyDoc__GetPhysicalSimulationComponents.htm"
---

# AssemblyDoc::GetPhysicalSimulationComponents

This method is:

- obsolete and has not been superseded.
- nonfunctional in SolidWorks 2008 and later.

  Use the interfaces related to motion studies introduced in SolidWorks 2008 to access animation and simulation.

Description

This method gets the Physical Simulation's components and transforms.

Syntax (OLE Automation)

void = AssemblyDoc.GetPhysicalSimulationComponents ( inDuration, outCount, outComponents, outTransforms, outStepStartTimes, outStepDurations, outTotalPhysSimDuration)

| Input: | (long) inDuration | Total elapsed time for Physical Simulation |
| --- | --- | --- |
| Output: | (long*) outCount | Size for all returned arrays |
| Output: | (VARIANT*) outComponents | VARIANT of type SafeArray of the Component2 objects |
| Output: | (VARIANT*) outTransforms | VARIANT of type SafeArray of the MathTransform objects |
| Output: | (VARIANT*) outStepStartTimes | Array of doubles of size outCount; when each step in the Physical Simulation should happen |
| Output: | (VARIANT*) outStepDurations | Array of doubles of size outCount; how long each step in the Physical Simulation should take |
| Output: | (double*) outTotalPhysSimDuration | Total elapsed time Physical Simulation should have taken |

Syntax (COM)

status = AssemblyDoc->GetPhysicalSimulationComponents ( inDuration, outCount, outComponents, outTransforms, outStepStartTimes, outStepDurations, outTotalPhysSimDuration)

| Input: | (long) inDuration | Total elapsed time for Physical Simulation |
| --- | --- | --- |
| Output: | (long*) outCount | Size for all returned arrays |
| Output: | (VARIANT*) outComponents | VARIANT of type SafeArray of the Component2 objects |
| Output: | (VARIANT*) outTransforms | VARIANT of type SafeArray of the MathTransform objects |
| Output: | (VARIANT*) outStepStartTimes | Array of doubles of size outCount; when each step in the Physical Simulation should happen |
| Output: | (VARIANT*) outStepDurations | Array of doubles of size outCount; when each step in the Physical Simulation should happen |
| Output: | (double*) outTotalPhysSimDuration | Total elapsed time Physical Simulation should have taken |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
