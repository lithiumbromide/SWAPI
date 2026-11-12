---
title: "CustomSymbol::GetLeaderAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetLeaderAtIndex.htm"
---

# CustomSymbol::GetLeaderAtIndex

This method is obsolete and has been superseded by [Note::GetLeaderAtIndex](sldworksAPI.chm::/Note/Note__GetLineAtIndex.htm).

Description

This method gets information about the specified leader on this symbol.

Syntax (OLE Automation)

retval = CustomSymbol.GetLeaderAtIndex ( index )

| Input: | (long) index | Index of leader |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray (see below) |

Syntax (COM)

status = CustomSymbol->IGetLeaderAtIndex ( index, &PointCount, retval )

| Input: | (long) index | Index of leader |
| --- | --- | --- |
| Output: | (long) PointCount | Number of (x,y,z) points being returned in the array |
| Output: | (double*) retval | Pointer to array of doubles (see below) |
| Return: | (HRESULT) status | S_OK if Successful |

Remarks

The leader line might use 0, 1 or 2 lines. If the CustomSymbol is not attached, there are 0 lines; a straight leaderline is 1 line, and a bent leaderline is 2 lines. You must infer the number of leader lines based on IsAttached() and HasExtraLeader().

IsAttached() == FALSE implies no leaderline and there are therefore no leaderline points (PointCount=0).

HasExtraLeader() == FALSE means that this is a straight leaderline and there will therefore be 1 line (PointCount=2)

HasExtraLeader() == TRUE means that this is a bent leaderline and there will therefore be 2 lines (PointCount=3)

The return value uses the following format:

retval[0] = X-coord of first leader point

retval[1] = Y-coord of first leader point

retval[2] = Z-coord of first leader point

retval[3] = X-coord of second leader point

retval[4] = Y-coord of second leader point

retval[5] = Z-coord of second leader point

retval[6] = X-coord of third leader point

retval[7] = Y-coord of third leader point

retval[8] = Z-coord of third leader point

Use [CustomSymbol::GetLeaderCount](CustomSymbol__GetLeaderCount.htm) to determine how many leaders are on the CustomSymbol object.
