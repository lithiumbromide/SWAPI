---
title: "Modeler::CreateBodiesFromSheets"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Modeler/Modeler__CreateBodiesFromSheets.htm"
---

# Modeler::CreateBodiesFromSheets

This method is obsolete and has been superseded by [Modeler::CreateBodiesFromSheets2](sldworksAPI.chm::/Modeler/Modeler__CreateBodiesFromSheets2.htm).

Description

This method sews sheets to make a sheet body or solid body.

Syntax (OLE Automation)

results = Modeler.CreateBodiesFromSheets ( sheets, options, error)

| Input: | (VARIANT) sheets | VARIANT of type SafeArray containing the sheets |
| --- | --- | --- |
| Input: | (long) options | Type of body to create as defined by swSheetSewingOption_e |
| Property: | (long) error | Error as defined by swSheetSewingError_e |
| Output: | (VARIANT) results | VARIANT of type SafeArray of the results |

Syntax (COM)

status = Modeler->ICreateBodiesFromSheets ( nSheets, sheets, options, nResults, results, &error)

| Input: | (long) nSheets | Number of sheets |
| --- | --- | --- |
| Input: | (LPUNKNOWN) sheets | Pointer to the sheets |
| Input: | (long) options | Type of body to create as defined by swSheetSewingOption_e |
| Property: | (long) nResults | Number of results |
| Property: | (LPUNKNOWN) results | Pointer to the results |
| Output: | (long) error | Error as defined by swSheetSewingError_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
