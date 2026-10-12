---
title: "Get Annotation Object Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Annotation_Object_Example_VB.htm"
---

# Get Annotation Object Example (VBA)

This example shows how to obtain the annotation object for the selected annotation symbol.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document that contains an annotation symbol.
 ' 2. Select the annotation symbol.
 '
 ' Postconditions: The annotation object for the selected symbol is obtained.
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim SelMgr As SldWorks.SelectionMgr
 Dim AnnoObject As Object
 Dim aWeldSymbol As SldWorks.WeldSymbol
 Dim aWeldBead As SldWorks.WeldBead
 Dim aView As SldWorks.View
 Dim aTableAnno As SldWorks.TableAnnotation
 Dim anSFSymbol As SldWorks.SFSymbol
 Dim aRevisionCloud As SldWorks.RevisionCloud
 Dim aNote As SldWorks.Note
 Dim aLeader As SldWorks.MultiJogLeader
 Dim aGtol As SldWorks.Gtol
 Dim aDowelSym As SldWorks.DowelSymbol
 Dim aDispDim As SldWorks.DisplayDimension
 Dim aDatTarSym As SldWorks.DatumTargetSym
 Dim aDatumTag As SldWorks.DatumTag
 Dim aDatumOrigin As SldWorks.DatumOrigin
 Dim aCustomSymbol As SldWorks.CustomSymbol
 Dim aCenterMark As SldWorks.CenterMark
 Dim aCenterLine As SldWorks.CenterLine
 Dim aCThread as SldWorks.CThread
 Dim Anno As SldWorks.Annotation
Option Explicit
 Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc
     Set SelMgr = Part.SelectionManager
     Set AnnoObject = SelMgr.GetSelectedObject6(1, -1)

    Select Case SelMgr.GetSelectedObjectType3(1, -1)
         Case swSelWELDS:
             Debug.Print "Selected annotation is a WeldSymbol."
             Set aWeldSymbol = AnnoObject
             Set Anno = aWeldSymbol.GetAnnotation
         Case swSelWELDBEADS:
             Debug.Print "Selected annotation is a WeldBead."
             Set aWeldBead = AnnoObject
             Set Anno = aWeldBead.GetAnnotation
         Case swSelDRAWINGVIEWS:
             Debug.Print "Selected annotation is a View."
             Set aView = AnnoObject
             Set Anno = aView.GetAnnotation
         Case swSelANNOTATIONTABLES
             Debug.Print "Selected annotation is a TableAnnotation."
             Set aTableAnno = AnnoObject
             Set Anno = aTableAnno.GetAnnotation
         Case swSelSFSYMBOLS
             Debug.Print "Selected annotation is an SFSymbol."
             Set anSFSymbol = AnnoObject
             Set Anno = anSFSymbol.GetAnnotation
         Case swSelREVISIONCLOUDS
             Debug.Print "Selected annotation is a RevisionCloud."
             Set aRevisionCloud = AnnoObject
             Set Anno = aRevisionCloud.GetAnnotation
         Case swSelNOTES
             Debug.Print "Selected annotation is a Note."
             Set aNote = AnnoObject
             Set Anno = aNote.GetAnnotation
         Case swSelLEADERS
             Debug.Print "Selected annotation is a Leader."
             Set aLeader = AnnoObject
             Set Anno = aLeader.GetAnnotation
         Case swSelGTOLS
             Debug.Print "Selected annotation is a Gtol."
             Set aGtol = AnnoObject
             Set Anno = aGtol.GetAnnotation
         Case swSelDOWELSYMS
             Debug.Print "Selected annotation is a DowelSymbol."
             Set aDowelSym = AnnoObject
             Set Anno = aDowelSym.GetAnnotation
         Case swSelDIMENSIONS
             Debug.Print "Selected annotation is a DisplayDimension."
             Set aDispDim = AnnoObject
             Set Anno = aDispDim.GetAnnotation
         Case swSelDTMTARGS
             Debug.Print "Selected annotation is a DatumTargetSym."
             Set aDatTarSym = AnnoObject
             Set Anno = aDatTarSym.GetAnnotation
         Case swSelDATUMTAGS
             Debug.Print "Selected annotation is a DatumTag."
             Set aDatumTag = AnnoObject
             Set Anno = aDatumTag.GetAnnotation
         Case swSelDATUMPOINTS
             Debug.Print "Selected annotation is a DatumOrigin."
             Set aDatumOrigin = AnnoObject
             Set Anno = aDatumOrigin.GetAnnotation
         Case swSelCUSTOMSYMBOLS
             Debug.Print "Selected annotation is a CustomSymbol."
             Set aCustomSymbol = AnnoObject
             Set Anno = aCustomSymbol.GetAnnotation
         Case swSelCTHREADS
             Debug.Print "Selected annotation is a CThread."
             Set aCThread = AnnoObject
             Set Anno = aCThread.GetAnnotation
         Case swSelCENTERMARKSYMS
             Debug.Print "Selected annotation is a CenterMark."
             Set aCenterMark = AnnoObject
             Set Anno = aCenterMark.GetAnnotation
         Case swSelCENTERLINES
             Debug.Print "Selected annotation is a CenterLine."
             Set aCenterLine = AnnoObject
             Set Anno = aCenterLine.GetAnnotation
     End Select

    Debug.Print "Annotation: " & Anno.GetName

End Sub
```
