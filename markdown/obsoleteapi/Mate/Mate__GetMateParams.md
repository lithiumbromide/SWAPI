---
title: "Mate::GetMateParams"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Mate/Mate__GetMateParams.htm"
---

# Mate::GetMateParams

This method is obsolete and has not been superseded.

Description

This method gets the assembly mate parameters.

Syntax (OLE Automation)

retval = Mate.GetMateParams ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray containing three longs:mateType, alignFlag, and canBeFlipped (see Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = Mate->IGetMateParams ( &mateType, &alignFlag, &canBeFlipped )

| Output: | (long) mateType | The type of the mate |
| --- | --- | --- |
| Output: | (long) alignFlag | TRUE or FALSE (see Remarks ) |
| Output: | (long) canBeFlipped | TRUE or FALSE (see Remarks ) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

- alignFlag - 1 if the mated entities are aligned, 2 if the mated entities are anti-aligned.
- canBeFlipped - 2 if the mated entities can be flipped, 1 otherwise. This is only useful for mating conditions with dimensional values.
