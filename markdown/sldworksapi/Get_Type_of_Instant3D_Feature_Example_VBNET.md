---
title: "Get Type of Instant3D Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Type_of_Instant3D_Feature_Example_VBNET.htm"
---

# Get Type of Instant3D Feature Example (VB.NET)

This example shows how to get the types and persistent IDs of underlying features of Instant3D features.

'-----------------------------------------------------
' Preconditions:
' 1. Verify that the specified part exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part and traverses the FeatureManager
' design tree.
' 2. Gets the types of features, including the types
' of underlying features and the persistent
' IDs of Instant3D features.
' 3. Examine the Immediate window.
'-----------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

Public Sub Main()

Dim swModel As ModelDoc2
Dim swFeature As Feature
Dim fileName As String
Dim errors As Integer
Dim warnings As Integer

fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block.sldprt"
swModel = swApp.**OpenDoc6**(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

swFeature = swModel.**FirstFeature**

Call SelectFeat(swFeature)

End Sub

Public Function SelectFeat(ByVal featureTemp As Feature) As Boolean

While Not featureTemp Is Nothing

Dim featureName As String
featureName = featureTemp.**GetTypeName2**

Debug.Print(featureName)

' Instant3D features are ICE features
If featureName = "ICE" Then
Debug.Print(" Type: " & featureTemp.**GetTypeName**)
Debug.Print(" ID: " & featureTemp.**GetID**)
End If

featureTemp = featureTemp.**GetNextFeature**

End While

End Function

''' <summary>
''' The SldWorks swApp variable is pre-assigned for you.
''' </summary>
Public swApp As SldWorks

End Class
