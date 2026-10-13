---
title: "SldWorks::LoadFile3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__LoadFile3.htm"
---

# SldWorks::LoadFile3

This method is obsolete and has been superseded by [SldWorks::LoadFile4](sldworksAPI.chm::/SldWorks/SldWorks__LoadFile4.htm).

Description

This method loads a non-native SolidWorks file (for example, *.igs, *.dxf, and so on).

Syntax (OLE Automation)

Retval = SldWorks.LoadFile3 ( FileName, ArgString, ImportData)

| Input: | (BSTR) FileName | Full path and filename of the non-native SolidWorks file to import |
| --- | --- | --- |
| Input: | (BSTR) ArgString | Space-separated string that allows optional arguments to be specified when opening a foreign file (see Remarks ) |
| Input: | (LPDISPATCH) ImportData | Pointer to ImportIgesData object (currently only IGES data are supported) |
| Output: | (VARIANT_BOOL) Retval | TRUE if the file type is understood, FALSE if the file type is not known NOTE : This return value does not indicate that the file import is successful; instead, it means that the filename extension is recognized |

Syntax (COM)

status = SldWorks->LoadFile3 ( FileName, ArgString, ImportData, &Retval)

| Input: | (BSTR) FileName | Full path and filename of the non-native SolidWorks file to import |
| --- | --- | --- |
| Input: | (BSTR) ArgString | Space-separated string that allows optional arguments to be specified when opening a foreign file (see Remarks ) |
| Input: | (LPDISPATCH) ImportData | Pointer to ImportIgesData object (currently only IGES data are supported) |
| Output: | (VARIANT_BOOL) Retval | TRUE if the file type is understood, FALSE if the file type is not known NOTE : This return value does not indicate that the file import is successful; instead, it means that the filename extension is recognized |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The general form of ArgString is BOOLEAN and enumerator arguments, which should be passed as a string.

| If importing a... | Then set ArgString to... |
| --- | --- |
| DXF/DWG file | a space-separated list: < PaperSize > specifies the sheet size: -1 = Translator attempts to figure out the sheet size using the foreign file; this is the default if you do not specify any values 0 = A (Horizontal) 1 = A (Vertical) 2 = B 3 = C 4 = D 5 = E 6 = A4 7 = A4 (Vertical) 8 = A3 9 = A2 10 = A1 11 = A0 < LengthUnit > specifies the default length units : -1 = Translator attempts to figure out the default length unit using the foreign file; this is the default if you do not specify any values 0 = MM 1 = CM 2 = METER 3 = INCHES 4 = FEET 5 = FEETINCHES < MoveEntities > = Not used. Specify 0, if necessary. < ImportToSheetFormat > 0 = Import entities to the drawing sheet; this is the default value if you do not specify a value 1 = Import entities to the sheet format Examples To import a DXF/DWG file named Draw1.DXF with a sheet size of A3 and default length units in millimeters: swApp.LoadFile3 "C:\temp\Draw1.DXF", "8 0", Nothing To only specify to use default length units in millimeters in < LengthUnit >, you must also specify -1 for < PaperSize >: swApp.LoadFile3 "C:\temp\Draw1.DXF", "-1 0", NOthing To only specify to import to the sheet format in < ImportToSheetFormat >, you must also specify -1 for both < PaperSize > and < LengthUnit >, and 0 for < MoveEntities >: swApp.LoadFile3 "C:\temp\Draw1.DXF", "-1 -1 0 1" , Nothing |
| Pro/E file | To import features, use R To import geometry, use: B – Direct geometry import with knitting C – Direct geometry import without knitting D – Geometry import with knitting E – Geometry import without knitting S – Surface geometry import with knitting These arguments are case sensitive. Specifying one of these options suppresses dialog. |
| Non DXF/DWG and Pro/E files | To import the foreign file into a new SolidWorks document, use r To insert the foreign file into an existing SolidWorks part document, use i For example, to import an IGES file named measuring_cup.igs into a new SolidWorks document: swApp.LoadFile3 "D:\Samples\measuring_cup.IGS", "r", importData NOTES: Whether or not the result is a surface or solid depends on the import options. See Import and Export File Options for details. If ArgString is set to an empty string , then dialogs may be presented to the end-user during translation. |

See ImportIgesData for details about importing IGES data.
