---
title: "AssemblyDoc::AddMate"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDoc/AssemblyDoc__AddMate.htm"
---

# AssemblyDoc::AddMate

This method is obsolete and has been superseded by [AssemblyDoc::AddMate2](AssemblyDoc__AddMate2.htm).

Description

This method adds an assembly component mate relationship.

Syntax (OLE Automation)

void AssemblyDoc.AddMate ( mateType, align, flip, dist, angle)

| Input: | (long) mateType | Type of mate as defined in swMateType_e |
| --- | --- | --- |
| Input: | (long) align | Type of alignment as defined in swMateAlign_e |
| Input: | (BOOL) flip | TRUE to flip the component, FALSE otherwise |
| Input: | (double) dist | Distance value used with swMateDISTANCE mate type |
| Input: | (double) angle | Angle value used with swMateANGLE mate type |

Syntax (COM)

status = AssemblyDoc->AddMate ( mateType, align, flip, dist, angle )

| Input: | (long) mateType | Type of mate as defined in swMateType_e |
| --- | --- | --- |
| Input: | (long) align | Type of alignment as defined in swMateAlign_e |
| Input: | (VARIANT_BOOL) flip | TRUE to flip the component, FALSE otherwise |
| Input: | (double) dist | Distance value used with swMateDISTANCE mate type |
| Input: | (double) angle | Angle value used with swMateANGLE mate type |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method replaces MateAdd, MateAngle, MateOffset, MateSame, and MateOn.

If mateType is swMateDISTANCE or swMateANGLE when the mate is applied to the closest position that meets the mate condition specified by dist or angle, then setting flip to TRUE jumps the assembly to the other possible mate position.
