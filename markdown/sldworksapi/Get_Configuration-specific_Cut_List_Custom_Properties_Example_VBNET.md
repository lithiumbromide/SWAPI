---
title: "Get Configuration-specific Cut List Custom Properties Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Configuration-specific_Cut_List_Custom_Properties_Example_VBNET.htm"
---

# Get Configuration-specific Cut List Custom Properties Example (VB.NET)

This example shows how to get configuration-specific cut list custom properties.

'================================================================

'Preconditions:

' 1. Open a part that has one or more configuration-specific cut lists with custom properties.

' (Or ask SOLIDWORKS API Support to send you the models that work with this ICutListItem sample code.)

' 2. Open an Immediate/Output window.

'Postconditions: Inspect all the configurations' cut lists' custom properties in the Immediate/Output window.

'=============================================================

Imports SolidWorks.Interop.sldworks

Imports SolidWorks.Interop.swconst

Imports System.Runtime.InteropServices

Imports System

Partial Class SolidWorksMacro

Dim swModel As ModelDoc2

Dim vConfigNameArr() As Object

Dim vConfigName As String

Dim vcutlistItems() As Object

Dim vcutlistItem As CutListItem

Dim cutlistItem As CutListItem

Dim cusPropMgr As CustomPropertyManager

Dim config As Configuration

Dim lRetVal As Integer

Dim vPropNames() As String

Dim vPropTypes() As Integer

Dim vPropValues() As String

Dim resolved() As Integer

Dim linkProp() As Integer

Dim i As Integer

Dim j As Integer

Dim propName As String

Public Sub main()

swModel = swApp.**ActiveDoc**

vConfigNameArr = swModel.**GetConfigurationNames**()

For Each vConfigName In vConfigNameArr

Debug.Print("Configuration: " & vConfigName)

config = swModel.**GetConfigurationByName**(vConfigName)

vcutlistItems = config.**GetCutListItems**()

i = 1

For Each vcutlistItem In vcutlistItems

Debug.Print("Cut list item #" & i & " custom properties:")

cutlistItem = vcutlistItem

cusPropMgr = cutlistItem.**CustomPropertyManager**()

lRetVal = cusPropMgr.**GetAll3**(vPropNames, vPropTypes, vPropValues, resolved, linkProp)

j = 0

For Each propName In vPropNames

Debug.Print(" " & propName & " " & vPropValues(j))

j = j + 1

Next

i = i + 1

Next

Next

End Sub

''' <summary>

''' The SldWorks swApp variable is pre-assigned for you.

''' </summary>

Public swApp As SldWorks

End Class
