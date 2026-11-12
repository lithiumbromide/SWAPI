---
title: "Suppress Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Suppress_Feature_Example_VB.htm"
---

# Suppress Feature Example (VBA)

This example shows how to suppress the selected feature.

```vb
'------------------------------------------
'
' Preconditions:
'       (1) Part or assembly is open.
'       (2) At least one entity is selected.
'
' Postconditions: All features associated with the selected
'       entities are suppressed.
'
' NOTE: Features are only suppressed if
'       the owning feature exists for that entity.
'       This typically occurs for edges.
'
'-------------------------------------------
Option Explicit
Public Enum swSelectType_e
    swSelNOTHING = 0
    swSelEDGES = 1              '  "EDGE"
    swSelFACES = 2              '  "FACE"
    swSelVERTICES = 3           '  "VERTEX"
    swSelDATUMPLANES = 4        '  "PLANE"
    swSelDATUMAXES = 5          '  "AXIS"
    swSelDATUMPOINTS = 6        '  "DATUMPOINT"
    swSelOLEITEMS = 7           '  "OLEITEM"
    swSelATTRIBUTES = 8         '  "ATTRIBUTE"
    swSelSKETCHES = 9           '  "SKETCH"
    swSelSKETCHSEGS = 10        '  "SKETCHSEGMENT"
    swSelSKETCHPOINTS = 11      '  "SKETCHPOINT"
    swSelDRAWINGVIEWS = 12      '  "DRAWINGVIEW"
    swSelGTOLS = 13             '  "GTOL"
    swSelDIMENSIONS = 14        '  "DIMENSION"
    swSelNOTES = 15             '  "NOTE"
    swSelSECTIONLINES = 16      '  "SECTIONLINE"
    swSelDETAILCIRCLES = 17     '  "DETAILCIRCLE"
    swSelSECTIONTEXT = 18       '  "SECTIONTEXT"
    swSelSHEETS = 19            '  "SHEET"
    swSelCOMPONENTS = 20        '  "COMPONENT"
    swSelMATES = 21             '  "MATE"
    swSelBODYFEATURES = 22      '  "BODYFEATURE"
    swSelREFCURVES = 23         '  "REFCURVE"
    swSelEXTSKETCHSEGS = 24     '  "EXTSKETCHSEGMENT"
    swSelEXTSKETCHPOINTS = 25   '  "EXTSKETCHPOINT"
    swSelHELIX = 26             '  "HELIX" (is this wrong?)
    swSelREFERENCECURVES = 26   '  "REFERENCECURVES"
    swSelREFSURFACES = 27       '  "REFSURFACE"
    swSelCENTERMARKS = 28       '  "CENTERMARKS"
    swSelINCONTEXTFEAT = 29     '  "INCONTEXTFEAT"
    swSelMATEGROUP = 30         '  "MATEGROUP"
    swSelBREAKLINES = 31        '  "BREAKLINE"
    swSelINCONTEXTFEATS = 32    '  "INCONTEXTFEATS"
    swSelMATEGROUPS = 33        '  "MATEGROUPS"
    swSelSKETCHTEXT = 34        '  "SKETCHTEXT"
    swSelSFSYMBOLS = 35         '  "SFSYMBOL"
    swSelDATUMTAGS = 36         '  "DATUMTAG"
    swSelCOMPPATTERN = 37       '  "COMPPATTERN"
    swSelWELDS = 38             '  "WELD"
    swSelCTHREADS = 39          '  "CTHREAD"
    swSelDTMTARGS = 40          '  "DTMTARG"
    swSelPOINTREFS = 41         '  "POINTREF"
    swSelDCABINETS = 42         '  "DCABINET"
    swSelEXPLVIEWS = 43         '  "EXPLODEDVIEWS"
    swSelEXPLSTEPS = 44         '  "EXPLODESTEPS"
    swSelEXPLLINES = 45         '  "EXPLODELINES"
    swSelSILHOUETTES = 46       '  "SILHOUETTE"
    swSelCONFIGURATIONS = 47    '  "CONFIGURATIONS"
    swSelOBJHANDLES = 48
    swSelARROWS = 49            '  "VIEWARROW"
    swSelZONES = 50             '  "ZONES"
    swSelREFEDGES = 51          '  "REFERENCE-EDGE"
    swSelREFFACES = 52
    swSelREFSILHOUETTE = 53
    swSelBOMS = 54              '  "BOM"
    swSelEQNFOLDER = 55         '  "EQNFOLDER"
    swSelSKETCHHATCH = 56       '  "SKETCHHATCH"
    swSelIMPORTFOLDER = 57      '  "IMPORTFOLDER"
    swSelVIEWERHYPERLINK = 58   '  "HYPERLINK"
    swSelMIDPOINTS = 59
    swSelCUSTOMSYMBOLS = 60     '  "CUSTOMSYMBOL"
    swSelCOORDSYS = 61          '  "COORDSYS"
    swSelDATUMLINES = 62        '  "REFLINE"
    swSelROUTECURVES = 63
    swSelBOMTEMPS = 64          '  "BOMTEMP"
    swSelROUTEPOINTS = 65       '  "ROUTEPOINT"
    swSelCONNECTIONPOINTS = 66  '  "CONNECTIONPOINT"
    swSelROUTESWEEPS = 67
    swSelPOSGROUP = 68          '  "POSGROUP"
    swSelBROWSERITEM = 69       '  "BROWSERITEM"
    swSelFABRICATEDROUTE = 70   '  "ROUTEFABRICATED"
    swSelSKETCHPOINTFEAT = 71   '  "SKETCHPOINTFEAT"
    swSelEMPTYSPACE = 72        '  (is this wrong?)
    swSelCOMPSDONTOVERRIDE = 72
    swSelLIGHTS = 73            '  "LIGHTS"
    swSelWIREBODIES = 74
    swSelSURFACEBODIES = 75     '  "SURFACEBODY"
    swSelSOLIDBODIES = 76       '  "SOLIDBODY"
    swSelFRAMEPOINT = 77        '  "FRAMEPOINT"
    swSelSURFBODIESFIRST = 78
    swSelMANIPULATORS = 79      '  "MANIPULATOR"
    swSelPICTUREBODIES = 80     '  "PICTURE BODY"
    swSelSOLIDBODIESFIRST = 81
    swSelDOWELSYMS = 86         '  "DOWELSYM"
    swSelEXTSKETCHTEXT = 88     '  "EXTSKETCHTEXT"
    swSelBLOCKINST = 93         '  "BLOCKINST"
    swSelFTRFOLDER = 94         '  "FTRFOLDER"
    swSelSKETCHREGION = 95      '  "SKETCHREGION"
    swSelSKETCHCONTOUR = 96     '  "SKETCHCONTOUR"
    swSelBOMFEATURES = 97       '  "BOMFEATURE"
    swSelANNOTATIONTABLES = 98  '  "ANNOTATIONTABLES"
    swSelBLOCKDEF = 99          '  "BLOCKDEF"
    swSelCENTERMARKSYMS = 100   '  "CENTERMARKSYMS"
    swSelCENTERLINES = 103      '  "CENTERLINE"
    swSelHOLETABLEFEATS = 104   '  "HOLETABLE"
    swSelHOLETABLEAXES = 105    '  "HOLETABLEAXIS"
    swSelWELDMENT = 106         '  "WELDMENT"
    swSelSUBWELDFOLDER = 107    '  "SUBWELDMENT"
    swSelEXCLUDEMANIPULATORS = 111
    swSelREVISIONTABLE = 113    '  "REVISIONTABLE"
    swSelBODYFOLDER = 118       '  "BDYFOLDER"
    swSelREVISIONTABLEFEAT = 119
    swSelEVERYTHING = -3
    swSelLOCATIONS = -2
    swSelUNSUPPORTED = -1
'   swSelEVERYTHING = 4294967293
'   swSelLOCATIONS = 4294967294
'   swSelUNSUPPORTED = 4294967295
End Enum
Sub main()
    Dim swApp               As SldWorks.SldWorks
    Dim swModel             As SldWorks.ModelDoc2
    Dim swSelMgr            As SldWorks.SelectionMgr
    Dim swFeat              As SldWorks.Feature
    Dim i                   As Long
    Dim bRet                As Boolean

    On Error Resume Next

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager

    Debug.Print "File = " & swModel.GetPathName

    ' Information about selected entities
    For i = 1 To swSelMgr.GetSelectedObjectCount
        Set swFeat = swSelMgr.GetSelectedObject5(i)

        Debug.Print "  SelType(" & i & ") = " & swSelMgr.GetSelectedObjectType(i)
        If Not swFeat Is Nothing Then
            Debug.Print "    " & swFeat.Name & " <" & swFeat.GetTypeName & ">"
        End If
    Next i
    Debug.Print ""

    ' Suppress what has been selected
    bRet = swModel.EditSuppress2: Debug.Assert bRet
End Sub
'------------------------------------------
```
