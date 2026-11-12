---
title: "Gtol::SetFrameSymbols"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Gtol/Gtol__SetFrameSymbols.htm"
---

# Gtol::SetFrameSymbols

This method is obsolete and has been superseded by [Gtol::SetFrameSymbols2](sldworksAPI.chm::/Gtol/Gtol__SetFrameSymbols2.htm).

Description

This method sets all the symbols for a feature control symbol.

Syntax (OLE Automation)

void Gtol.SetFrameSymbols ( frameNumber, GCS, tolDia1, tolMC1, tolDia2, tolMC2, datumMC1, datumMC2, datumMC3)

| Input: | (short) frameNumber | Feature control frame 1 for first |
| --- | --- | --- |
| Input: | (short) GCS | Geometric characteristic symbol |
| Input: | (BOOL) tolDia1 | Diameter symbol exists for tolerance 1 (TRUE or FALSE) |
| Input: | (short) tolMC1 | Material condition for tolerance 1 |
| Input: | (BOOL) tolDia2 | Diameter symbol exists for tolerance 2 (TRUE or FALSE) |
| Input: | (short) tolMC2 | Material condition for tolerance 2 |
| Input: | (short) datumMC1 | Material condition for primary datum |
| Input: | (short) datumMC2 | Material condition for secondary datum |
| Input: | (short) datumMC3 | Material condition for tertiary datum |

Syntax (COM)

status = Gtol->SetFrameSymbols ( frameNumber, GCS, tolDia1, tolMC1, tolDia2, tolMC2, datumMC1, datumMC2, datumMC3 )

| Input: | (short) frameNumber | Feature control frame 1 for first |
| --- | --- | --- |
| Input: | (short) GCS | Geometric characteristic symbol |
| Input: | (VARIANT_BOOL) tolDia1 | Diameter symbol exists for tolerance 1 (TRUE or FALSE) |
| Input: | (short) tolMC1 | Material condition for tolerance 1 |
| Input: | (VARIANT_BOOL) tolDia2 | Diameter symbol exists for tolerance 2 (TRUE or FALSE) |
| Input: | (short) tolMC2 | Material condition for tolerance 2 |
| Input: | (short) datumMC1 | Material condition for primary datum |
| Input: | (short) datumMC2 | Material condition for secondary datum |
| Input: | (short) datumMC3 | Material condition for tertiary datum |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

For valid Geometric Characteristic Symbols (GCS), refer to swGtolGeomCharSymbol_e.

For valid Material Conditions (tolMC1, tolMC2, datumMC1, and so on), refer to swGtolMatCondition_e.
