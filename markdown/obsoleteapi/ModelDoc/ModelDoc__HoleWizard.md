---
title: "ModelDoc::HoleWizard"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__HoleWizard.htm"
---

# ModelDoc::HoleWizard

This method is obsolete and has been superseded by [ModelDoc2::HoleWizard](../ModelDoc2/ModelDoc2__HoleWizard.htm).

Description

This method invokes the hole wizard to create a new hole.

Syntax (OLE Automation)

void ModelDoc.HoleWizard ( depth, endType, flip, dir, hType, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12)

| Input: | (double) depth | Depth in meters |
| --- | --- | --- |
| Input: | (short) endType | Termination type |
| Input: | (BOOL) flip | TRUE to flip cut, FALSE to not |
| Input: | (BOOL) dir | TRUE to flip direction of extrusion, FALSE to not |
| Input: | (long) hType | Hole type |
| Input: | (double) d1...d12 | Dimension values |

Syntax (COM)

status = ModelDoc->HoleWizard ( depth, endType, flip, dir, hType, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12 )

| Input: | (double) depth | Depth in meters |
| --- | --- | --- |
| Input: | (short) endType | Termination type |
| Input: | (BOOL) flip | TRUE to flip cut, FALSE if not |
| Input: | (BOOL) dir | TRUE to flip direction of extrusion, FALSE if not |
| Input: | (long) hType | Hole type |
| Input: | (double) d1...d12 | Dimension values |
| Input: | (double) d12 | Dimension value |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The hType argument controls the type of hole that is created:

0 Simple

1 Tapered

2 Counter Bore

3 Counter Sunk

4 Counter Drilled

5 Simple Drilled

6 Tapered Drilled

7 C-Bored Drilled

8 C-Sunk Drilled

9 C-Drilled Drilled

For a complete and up-to-date list of available hole types, see HoleWzd.idx located in the ./lang/<language> folder of your SolidWorks installation.

Termination type may be any of the values in swEndConditions_e.
