---
title: "Gtol::GetLeaderAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Gtol/Gtol__GetLeaderAtIndex.htm"
---

# Gtol::GetLeaderAtIndex

This method is obsolete and has been superseded by [Gtol::GetLeaderAtIndex2](sldworksAPI.chm::/Gtol/Gtol__GetLeaderAtIndex2.htm).

Description

This method gets information about the specified leader on this Gtol.

Syntax (OLE Automation)

retval = Gtol.GetLeaderAtIndex ( index )

| Input: | (long) index | Index of the leader |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray (see Remarks ) |

Syntax (COM)

status = Gtol->IGetLeaderAtIndex ( index, &PointCount, retval )

| Input: | (long) index | Index of the leader |
| --- | --- | --- |
| Output: | (long) PointCount | Number of (x,y,z) points returned in the array |
| Output: | (double*) retval | Pointer to array of doubles (see Remarks ) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

There can be 0, 1 or 2 lines with the leader line. If the Gtol is not attached, then there are 0 lines. Otherwise, the gtol can have a straight leaderline (1 line) or a bent leaderline (2 lines). The caller must infer the number of leader lines based on Gtol::IsAttached and Gtol::HasExtraLeader.

- IsAttached() == FALSE implies no leaderline and there are therefore no leaderline points (PointCount=0).
- HasExtraLeader() == FALSE means that this is a straight leaderline and there will therefore be 1 line (PointCount=2).
- HasExtraLeader() == TRUE means that this is a bent leaderline and there will therefore be 2 lines (PointCount=3).

The format of return information is the following array of doubles:

- retval[0] = X-coordinate of first leader point
- retval[1] = Y-coordinate of first leader point
- retval[2] = Z-coordinate of first leader point
- retval[3] = X-coordinate of second leader point
- retval[4] = Y-coordinate of second leader point
- retval[5] = Z-coordinate of second leader point
- retval[6] = X-coordinate of third leader point
- retval[7] = Y-coordinate of third leader point
- retval[8] = Z-coordinate of third leader point

Use Gtol::GetLeaderCount to see how many leaders are on the Gtol object.
