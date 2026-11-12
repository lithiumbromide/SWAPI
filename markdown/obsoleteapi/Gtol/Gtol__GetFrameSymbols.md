---
title: "Gtol::GetFrameSymbols"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Gtol/Gtol__GetFrameSymbols.htm"
---

# Gtol::GetFrameSymbols

This method is obsolete and has been superseded by [Gtol::GetFrameSymbols2](sldworksAPI.chm::/Gtol/Gtol__GetFrameSymbols2.htm) and [Gtol::GetFrameDiameterSymbols](sldworksAPI.chm::/Gtol/Gtol__GetFrameDiameterSymbols.htm).

Description

This method returns an array describing the symbols that appear in the first or second feature control frame of this Gtol.

Syntax (OLE Automation)

retval = Gtol.GetFrameSymbols ( frameNumber)

| Input: | (short) frameNumber | Frame number |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray |

Syntax (COM)

status = Gtol->IGetFrameSymbols ( frameNumber, retval )

| Input: | (short) frameNumber | Frame number |
| --- | --- | --- |
| Output: | (short*) retval | Array of shorts |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Each symbol returned by this method is identified by an integer index that you can use as the symIdx argument with the GetSym* methods.

Format of return information is the following array of short integers:

retval[0] = gcs, Geometric characteristic symbol index

retval[1] = tdia1, Indicates whether the first gtol tolerance has a "diameter" symbol

retval[2] = tmc1, Index of material condition symbol for first tolerance value

retval[3] = tdia2, Indicates whether the second gtol tolerance has a "diameter" symbol

retval[4] = tmc2, Index of material condition symbol for first tolerance value

retval[5] = dmc1, Index of material condition symbol for datum1

retval[6] = dmc2, Index of material condition symbol for datum2

retval[7] = dmc3, Index of material condition symbol for datum3

For valid Geometric Characteristic Symbols (GCS), see swGtolGeomCharSymbol_e.

For valid Material Conditions (tolMC1, tolMC2, datumMC1, and so on), see swGtolMatCondition_e.
