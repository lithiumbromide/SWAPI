---
title: "Create a Mate Controller Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Mate_Controller_Example_VBNET.htm"
---

# Create a Mate Controller Example (VB.NET)

This example shows how to create a Mate Controller in an assembly.

'======================================================================================

' Preconditions: Open an assembly document that contains a mechanical slot feature

' with a slot mate that has one of these constraints:

' - Distance Along Slot

' - Percent Along Slot

'

' Postconditions:

' 1. Mate Controller (Position 3) is added to the FeatureManager design tree.

' 2. Inspect the graphics area.

'
' NOTE: Because the model is used elsewhere, do not save changes.
'---------------------------------------------------------------------------

Imports SolidWorks.Interop.sldworks

Imports SolidWorks.Interop.swconst

Imports System.Runtime.InteropServices

Imports System

Partial Class SolidWorksMacro

Dim Part As ModelDoc2

Dim Assem As AssemblyDoc

Dim featMgr As FeatureManager

Dim boolstatus As Boolean

Dim myModelView As Object

Dim var As Object

Dim mateControllerObj As MateControllerFeatureData

Dim mcObj2 As MateControllerFeatureData

Dim mateContFeat As Feature

Dim position2ValArr(0) As Double

Dim position3ValArr(0) As Double

Dim var1 As Object

Dim position2ValArr2(0) As Double

Dim position3ValArr2(0) As Double

Function ObjectArrayToDispatchWrapperArray(ByVal Objects As Object()) As DispatchWrapper()

Dim ArraySize As Integer

ArraySize = Objects.GetUpperBound(0)

Dim d(ArraySize) As DispatchWrapper

Dim ArrayIndex As Integer

For ArrayIndex = 0 To ArraySize

d(ArrayIndex) = New DispatchWrapper(Objects(ArrayIndex))

Next

Return d

End Function

Sub main()

Part = swApp.ActiveDoc

Assem = Part

myModelView = Part.ActiveView

myModelView.FrameState = swWindowState_e.swWindowMaximized

Part.ClearSelection2(True)

boolstatus = Assem.**IsSupportedMatesAvailable**

var = Assem.**CollectAllSupportiveMates**

featMgr = Part.FeatureManager

mateControllerObj = featMgr.**CreateDefinition**(swFeatureNameID_e.swFmMateController)

Dim dArray() As DispatchWrapper

dArray = ObjectArrayToDispatchWrapperArray(var)

Call mateControllerObj.**Initialize**(dArray)

mateControllerObj.**AddNewPosition**("Position1")

mateControllerObj.**AddNewPosition**("Position2")

mateControllerObj.**AddNewPosition**("Position3")

position2ValArr(0) = 0.0375

Call mateControllerObj.**SetValues**("Position2", position2ValArr)

position3ValArr(0) = 0.0625

Call mateControllerObj.**SetValues**("Position3", position3ValArr)

mateContFeat = featMgr.**CreateFeature**(mateControllerObj)

mcObj2 = mateContFeat.**GetDefinition**()

var1 = mcObj2.**Mates**

position2ValArr2(0) = 0.015

Call mcObj2.**SetValues**("Position2", position2ValArr2)

position3ValArr2(0) = 0.085

Call mcObj2.**SetValues**("Position3", position3ValArr2)

mateContFeat.**ModifyDefinition**(mcObj2, Part, Nothing)

End Sub

''' <summary>

''' The SldWorks swApp variable is pre-assigned for you.

''' </summary>

Public swApp As SldWorks

End Class
