---
title: "Create Circular Pattern Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Circular_Pattern_Example_VB.htm"
---

# Create Circular Pattern Example (VBA)

This example shows how to create a circular-pattern feature using selected direction axis, pattern seed features, and variable spacing between pattern instances.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open public_documents\samples\tutorial\api\varyinstance.sldprt.
 '
 ' Postconditions: Creates a circular-pattern feature.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
 Dim SwApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim boolstatus As Boolean
 Dim longstatus As Long
 Option Explicit
 Sub main()
    Set SwApp = Application.SldWorks

    SwApp.ActivateDoc3 "varyInstance", False, swUserDecision, longstatus
     Set Part = SwApp.ActiveDoc

    boolstatus = Part.Extension.SelectByID2("Cut-Extrude1", "BODYFEATURE", 8.43730075439453E-03, 3.64341890551145E-03, -3.54416044676498E-02, False, 4, Nothing, 0)
     If boolstatus = False Then ErrorMsg SwApp, "Failed to select a seed feature": GoTo LastLine

    boolstatus = Part.Extension.SelectByID2("", "EDGE", 6.28473027779819E-03, -0.168045059787516, -4.96550391792034E-02, True, 1, Nothing, 0)
     If boolstatus = False Then ErrorMsg SwApp, "Failed to select an edge for direction 1": GoTo LastLine

    boolstatus = Part.Extension.SelectByID2("Fillet1", "BODYFEATURE", 7.82948437176856E-04, 4.55320522434022E-03, -3.50770617062892E-02, True, 4, Nothing, 0)
     If boolstatus = False Then ErrorMsg SwApp, "Failed to select a seed feature": GoTo LastLine

    boolstatus = Part.FeatureManager.InsertVaryInstanceIncrement("D1@Sketch2@varyInstance.SLDPRT", 4, 1, 0, 0.003)
     If boolstatus = False Then ErrorMsg SwApp, "Failed to add an increment value to dimension D1@Sketch2@varyInstance.SLDPRT": GoTo LastLine

    boolstatus = Part.FeatureManager.InsertVaryInstanceIncrement("D1@Cut-Extrude1@varyInstance.SLDPRT", 4, 1, 0, -0.001)
     If boolstatus = False Then ErrorMsg SwApp, "Failed to add an increment value to dimension D1@Cut-Extrude1@varyInstance.SLDPRT": GoTo LastLine

    boolstatus = Part.FeatureManager.InsertVaryInstanceIncrement("D1@Fillet1@varyInstance.SLDPRT", 4, 1, 0, 0.0001)
     If boolstatus = False Then ErrorMsg SwApp, "Failed to add an increment value to dimension D1@Fillet1@varyInstance.SLDPRT": GoTo LastLine

    boolstatus = Part.FeatureManager.InsertVaryInstanceIncrement("Space Increment", 4, 2, 0, 3.49065850398866E-02)
     If boolstatus = False Then ErrorMsg SwApp, "Failed to add an increment value to direction 1 spacing": GoTo LastLine

    boolstatus = Part.FeatureManager.InsertVaryInstanceOverride("D1@Sketch2@varyInstance.SLDPRT", 4, 1, -1, 5, -1, 0.05)
     If boolstatus = False Then ErrorMsg SwApp, "Failed to override value of dimension D1@Sketch2@varyInstance.SLDPRT at instance (5, 0)": GoTo LastLine

    boolstatus = Part.FeatureManager.InsertVaryInstanceOverride("D1@Sketch2@varyInstance.SLDPRT", 4, 1, -1, 3, -1, 0.06)
     If boolstatus = False Then ErrorMsg SwApp, "Failed to override value of dimension D1@Sketch2@varyInstance.SLDPRT at instance (3, 0)": GoTo LastLine

    boolstatus = Part.FeatureManager.InsertVaryInstanceOverride("D1@Cut-Extrude1@varyInstance.SLDPRT", 4, 1, -1, 5, -1, 0.005)
     If boolstatus = False Then ErrorMsg SwApp, "Failed to override value of dimension D1@Cut-Extrude1@varyInstance.SLDPRT at instance (5, 0)": GoTo LastLine

    boolstatus = Part.FeatureManager.InsertVaryInstanceOverride("D1@Fillet1@varyInstance.SLDPRT", 4, 1, -1, 5, -1, 0.006)
     If boolstatus = False Then ErrorMsg SwApp, "Failed to override value of dimension D1@Fillet1@varyInstance.SLDPRT at instance (5, 0)": GoTo LastLine

    boolstatus = Part.FeatureManager.InsertVaryInstanceOverride("D1@Fillet1@varyInstance.SLDPRT", 4, 1, -1, 3, -1, 0.004)
     If boolstatus = False Then ErrorMsg SwApp, "Failed to override value of dimension D1@Fillet1@varyInstance.SLDPRT at instance (3, 0)": GoTo LastLine

    boolstatus = Part.FeatureManager.InsertVaryInstanceOverride("Space Increment", 4, 2, 0, 5, -1, 1.30899693899575)
     If boolstatus = False Then ErrorMsg SwApp, "Failed to override value of direction 1 spacing increment at instance (3, 0)": GoTo LastLine

    Dim myFeature As SldWorks.Feature
     Set myFeature = Part.FeatureManager.FeatureCircularPattern4(6, 0.174532925199434, True, "NULL", False, False, True)
     If myFeature Is Nothing Then ErrorMsg SwApp, "Failed to create a vary instance circular pattern": GoTo LastLine

LastLine:

End Sub
Function ErrorMsg(SwApp As Object, Message As String)
     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
 End Function
```
