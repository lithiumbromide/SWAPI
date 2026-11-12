---
title: "Get Annotation Object Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Annotation_Object_Example_VBNET.htm"
---

# Get Annotation Object Example (VB.NET)

This example shows how to obtain the annotation object for the selected annotation symbol.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document that contains an annotation symbol.
 ' 2. Select the annotation symbol.
 '
 ' Postconditions: The annotation object for the selected symbol is obtained.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim SelMgr As SelectionMgr
     Dim AnnoObject As Object
     Dim aWeldSymbol As WeldSymbol
     Dim aWeldBead As WeldBead
     Dim aView As View
     Dim aTableAnno As TableAnnotation
     Dim anSFSymbol As SFSymbol
     Dim aRevisionCloud As RevisionCloud
     Dim aNote As Note
     Dim aLeader As MultiJogLeader
     Dim aGtol As Gtol
     Dim aDowelSym As DowelSymbol
     Dim aDispDim As DisplayDimension
     Dim aDatTarSym As DatumTargetSym
     Dim aDatumTag As DatumTag
     Dim aDatumOrigin As DatumOrigin
     Dim aCustomSymbol As CustomSymbol
     Dim aCenterMark As CenterMark
     Dim aCenterLine As CenterLine
     Dim aCThread As CThread
     Dim Anno As Annotation

     Sub main()

         Part = swApp.ActiveDoc
         SelMgr = Part.SelectionManager
         AnnoObject = SelMgr.GetSelectedObject6(1, -1)

         Select Case SelMgr.GetSelectedObjectType3(1, -1)
             Case swSelectType_e.swSelWELDS
                 Debug.Print("Selected annotation is a WeldSymbol.")
                 aWeldSymbol = AnnoObject
                 Anno = aWeldSymbol.GetAnnotation
             Case swSelectType_e.swSelWELDBEADS
                 Debug.Print("Selected annotation is a WeldBead.")
                 aWeldBead = AnnoObject
                 Anno = aWeldBead.GetAnnotation
             Case swSelectType_e.swSelDRAWINGVIEWS
                 Debug.Print("Selected annotation is a View.")
                 aView = AnnoObject
                 Anno = aView.GetAnnotation
             Case swSelectType_e.swSelANNOTATIONTABLES
                 Debug.Print("Selected annotation is a TableAnnotation.")
                 aTableAnno = AnnoObject
                 Anno = aTableAnno.GetAnnotation
             Case swSelectType_e.swSelSFSYMBOLS
                 Debug.Print("Selected annotation is an SFSymbol.")
                 anSFSymbol = AnnoObject
                 Anno = anSFSymbol.GetAnnotation
             Case swSelectType_e.swSelREVISIONCLOUDS
                 Debug.Print("Selected annotation is a RevisionCloud.")
                 aRevisionCloud = AnnoObject
                 Anno = aRevisionCloud.GetAnnotation
             Case swSelectType_e.swSelNOTES
                 Debug.Print("Selected annotation is a Note.")
                 aNote = AnnoObject
                 Anno = aNote.GetAnnotation
             Case swSelectType_e.swSelLEADERS
                 Debug.Print("Selected annotation is a Leader.")
                 aLeader = AnnoObject
                 Anno = aLeader.GetAnnotation
             Case swSelectType_e.swSelGTOLS
                 Debug.Print("Selected annotation is a Gtol.")
                 aGtol = AnnoObject
                 Anno = aGtol.GetAnnotation
             Case swSelectType_e.swSelDOWELSYMS
                 Debug.Print("Selected annotation is a DowelSymbol.")
                 aDowelSym = AnnoObject
                 Anno = aDowelSym.GetAnnotation
             Case swSelectType_e.swSelDIMENSIONS
                 Debug.Print("Selected annotation is a DisplayDimension.")
                 aDispDim = AnnoObject
                 Anno = aDispDim.GetAnnotation
             Case swSelectType_e.swSelDTMTARGS
                 Debug.Print("Selected annotation is a DatumTargetSym.")
                 aDatTarSym = AnnoObject
                 Anno = aDatTarSym.GetAnnotation
             Case swSelectType_e.swSelDATUMTAGS
                 Debug.Print("Selected annotation is a DatumTag.")
                 aDatumTag = AnnoObject
                 Anno = aDatumTag.GetAnnotation
             Case swSelectType_e.swSelDATUMPOINTS
                 Debug.Print("Selected annotation is a DatumOrigin.")
                 aDatumOrigin = AnnoObject
                 Anno = aDatumOrigin.GetAnnotation
             Case swSelectType_e.swSelCUSTOMSYMBOLS
                 Debug.Print("Selected annotation is a CustomSymbol.")
                 aCustomSymbol = AnnoObject
                 Anno = aCustomSymbol.GetAnnotation
             Case swSelectType_e.swSelCTHREADS
                 Debug.Print("Selected annotation is a CThread.")
                 aCThread = AnnoObject
                 Anno = aCThread.GetAnnotation
             Case swSelectType_e.swSelCENTERMARKSYMS
                 Debug.Print("Selected annotation is a CenterMark.")
                 aCenterMark = AnnoObject
                 Anno = aCenterMark.GetAnnotation
             Case swSelectType_e.swSelCENTERLINES
                 Debug.Print("Selected annotation is a CenterLine.")
                 aCenterLine = AnnoObject
                 Anno = aCenterLine.GetAnnotation
         End Select

         Debug.Print("Annotation: " & Anno.GetName)

     End Sub

     Public swApp As SldWorks

 End  Class
```
