---
title: "Set Components and Transforms for Interference Detection Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Components_and_Transforms_for_Interference_Detection_Example_VB.htm"
---

# Set Components and Transforms for Interference Detection Example (VBA)

This example shows how to:

- move an assembly component to an interfering position by replacing its transform.
- detect interference.

This example also shows how to apply absolute transforms to all components in order to multiply by identity transforms, which results in the components remaining in their current positions during interference detection.

```
'------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly exists.
' 2. Copy and paste Main into the main module of your macro.
' 3. Click Insert > Class Module and copy and paste Class1 into that
'    class module.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly.
' 2. Gets the components of the assembly and their transforms.
' 3. Creates a new transform for Part1^AssemInterferenceDetection-2.
' 4. Sets the components and their transforms, using the existing
'    rotation and the translation from the assembly origin.
'    a. Gets the number of interferences.
'    b. Examine the graphics area at the Stop statement to visually
'       verify the interferences, then press F5.
'    c. Programmatically verifies that the number of interferences
'       is as expected.
'    d. Gets whether:
'       * each returned interference is correct.
'       * the components remained in their starting positions during
'         interference detection.
'       * the components are at their starting positions.
' 5. Examine the Immediate window and graphics area.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'-------------------------------------------------------------------------
' Main
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim colStartingPositions As Collection
```

```
Sub main()
```

```
    Dim expectedNumberofInterferences As Long
    expectedNumberofInterferences = 2
```

```
    Dim expectedInterferenceVolumes As Collection
    Set expectedInterferenceVolumes = New Collection
    expectedInterferenceVolumes.Add 0.09
    expectedInterferenceVolumes.Add 0.01
```

```
    Dim expectedNumberOfInterferenceComps As Collection
    Set expectedNumberOfInterferenceComps = New Collection
    expectedNumberOfInterferenceComps.Add 2
    expectedNumberOfInterferenceComps.Add 2
```

```
    Dim bResult As Boolean
    bResult = True
```

```
    Dim swAssem As SldWorks.AssemblyDoc
    Set swAssem = OpenAssembly
```

```
    RecordStartingPositions swAssem
```

```
    SelectAllComponents swAssem
```

```
    Dim swInfrMgr As SldWorks.InterferenceDetectionMgr
    Set swInfrMgr = swAssem.InterferenceDetectionManager
```

```
    swInfrMgr.UseTransform = True
```

```
    Dim swComps(0 To 2) As SldWorks.Component2
    Set swComps(0) = swAssem.GetComponentByName("Part1^AssemInterferenceDetection-1")
    Set swComps(1) = swAssem.GetComponentByName("Part1^AssemInterferenceDetection-2")
    Set swComps(2) = swAssem.GetComponentByName("Part1^AssemInterferenceDetection-3")
```

```
    Dim swXfms(0 To 2) As SldWorks.MathTransform
    Set swXfms(0) = swComps(0).Transform2
    Set swXfms(1) = swComps(1).Transform2
    Set swXfms(2) = swComps(2).Transform2
```

```
    ' Replacement transform for Part1^AssemInterferenceDetection-2
    Dim dXfm(0 To 15) As Double
    ' Use existing rotation
    Dim vXfmCurrent As Variant
    vXfmCurrent = swXfms(1).ArrayData
```

```
    dXfm(0) = vXfmCurrent(0): dXfm(1) = vXfmCurrent(1): dXfm(2) = vXfmCurrent(2)
    dXfm(3) = vXfmCurrent(3): dXfm(4) = vXfmCurrent(4): dXfm(5) = vXfmCurrent(5)
    dXfm(6) = vXfmCurrent(6): dXfm(7) = vXfmCurrent(7): dXfm(8) = vXfmCurrent(8)
    ' Translation from assembly origin
    dXfm(9) = 0.9: dXfm(10) = 0.1: dXfm(11) = 0
    dXfm(12) = 1
    dXfm(13) = 0: dXfm(14) = 0: dXfm(15) = 0: dXfm(1) = 0: dXfm(2) = 0
```

```
    Dim swMath As SldWorks.MathUtility
    Set swMath = swApp.GetMathUtility
```

```
    Set swXfms(1) = swMath.CreateTransform(dXfm)
```

```
    Dim lResult As Long
    lResult = swInfrMgr.SetComponentsAndTransforms(swComps, swXfms)
    Debug.Print "Transforms applied:"
    If lResult = swSetComponentsAndTransformsStatus_e.swSetComponentsAndTransforms_Succeeded Then
        Debug.Print "  True"
    Else
        Debug.Print "  False: " & lResult & " vs. " & swSetComponentsAndTransformsStatus_e.swSetComponentsAndTransforms_Succeeded
        bResult = False
    End If
```

```
    Dim actualNumberOfInterferences As Long
    actualNumberOfInterferences = swInfrMgr.GetInterferenceCount
    Debug.Print "Number of interferences: "
    Debug.Print "  " & actualNumberOfInterferences
```

```
    Stop
    ' Examine the graphics area to verify
    ' the interferences, then press F5
```

```
    Dim bCorrectNumberofInterferences As Boolean
    bCorrectNumberofInterferences = expectedNumberofInterferences = actualNumberOfInterferences
    Debug.Print "Correct number of interferences:"
    If bCorrectNumberofInterferences Then
        Debug.Print "  True"
    Else
        Debug.Print "  False: " & actualNumberOfInterferences & " vs. " & expectedNumberofInterferences
        bResult = False
    End If
```

```
    Dim bCorrectInterferences As Boolean
    bCorrectInterferences = VerifyInterferencesAgainstExpectation(swInfrMgr.GetInterferences, expectedInterferenceVolumes, expectedNumberOfInterferenceComps)
    Debug.Print "Correct interferences:"
    If bCorrectInterferences Then
        Debug.Print "  True"
    Else
        Debug.Print "  False"
        bResult = False
    End If
```

```
    swInfrMgr.Done
```

```
    Dim bBackToStartingPositions As Boolean
    bBackToStartingPositions = VerifyFinishingPositions
    Debug.Print "Components back at starting positions:"
    If bBackToStartingPositions Then
        Debug.Print "  True"
    Else
        Debug.Print "  False"
        bResult = False
    End If
```

```
End Sub
```

```
Public Function OpenAssembly() As SldWorks.AssemblyDoc
    If swApp Is Nothing Then
        Set swApp = Application.SldWorks
    End If
```

```
    swApp.CloseAllDocuments True
```

```
    Dim docspec As SldWorks.DocumentSpecification
    Dim assemblyFile As String
    assemblyFile = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\AssemInterferenceDetection.sldasm"
    Set docspec = swApp.GetOpenDocSpec(assemblyFile)
```

```
    Dim swModel As SldWorks.ModelDoc2
    Set swModel = swApp.ActiveDoc
    Set swModel = swApp.OpenDoc7(docspec)
```

```
    Set OpenAssembly = swModel
End Function
```

```
Public Function EqualWithinTolerance(ByVal A As Double, ByVal B As Double) As Boolean
    Const tolerance As Double = 0.00001
    Dim difference As Double
    difference = Abs(A - B)
    EqualWithinTolerance = difference < tolerance
End Function
```

```
Public Sub RecordStartingPositions(swAssem As AssemblyDoc)
    Set colStartingPositions = New Collection
```

```
    Dim vComponents As Variant
    vComponents = swAssem.GetComponents(True)
```

```
    If Not IsEmpty(vComponents) Then
        Dim vComp As Variant
        For Each vComp In vComponents
            Dim swComp As Component2
            Set swComp = vComp
            Dim position As Class1
            Set position = New Class1
            position.RecordReferencePosition swComp
```

```
            colStartingPositions.Add position
        Next
    End If
End Sub
```

```
Public Function VerifyFinishingPositions() As Boolean
    Dim bResult As Boolean
    bResult = True
```

```
    Dim position As Class1
    Debug.Print "Position of: "
    For Each position In colStartingPositions
        If position.IsAtReferencePosition() Then
            Debug.Print "  " & position.Name & " has not moved"
        Else
            Debug.Print "  " & position.Name & " has moved"
            bResult = False
        End If
    Next
```

```
    VerifyFinishingPositions = bResult
End Function
```

```
Public Function VerifyInterferencesAgainstExpectation(vInterferences As Variant, expectedVolumes As Collection, expectedCompCounts As Collection) As Boolean
    Dim bResult As Boolean
    bResult = True
    If IsEmpty(vInterferences) Then
        Debug.Print "IInterferenceDetectionMgr::GetInterferences returned:"
        If expectedVolumes.Count = 0 Then
            Debug.Print "  Nothing as expected"
        Else
            Debug.Print "  Nothing unexpectedly"
            bResult = False
        End If
    Else
        Dim numInterferences As Long
        numInterferences = UBound(vInterferences) - LBound(vInterferences) + 1
        If numInterferences <> expectedVolumes.Count Then
            Debug.Print "IInterferenceDetectionMgr::GetInterferences returned unexpected number of interferences: " & numInterferences & " vs. " & expectedVolumes.Count
            bResult = False
        End If
```

```
        ' Cannot assume the same order
        ' Try to find matches for each returned interference
        Dim i As Long

        Debug.Print "Match found for calculated interference:"
        For i = LBound(vInterferences) To UBound(vInterferences)
            Dim swInterference As Interference
            Set swInterference = vInterferences(i)
```

```
            Dim volume As Double
            volume = swInterference.volume
```

```
            Dim compCount As Long
            compCount = swInterference.GetComponentCount
```

```
            Dim bFoundMatch As Boolean
            bFoundMatch = False
```

```
            Dim j As Long
            For j = 1 To expectedVolumes.Count
                If EqualWithinTolerance(expectedVolumes(j), volume) And (expectedCompCounts(j) = compCount) Then
                    bFoundMatch = True
                    expectedVolumes.Remove j
                    expectedCompCounts.Remove j
                    Exit For
                End If
            Next
```

```
            If bFoundMatch Then
                Debug.Print "  " & i & ": Volume = " & Format(volume, "0.000000") & " & Component count = " & compCount
            Else
                Debug.Print "  " & i & ": Volume = " & Format(volume, "0.000000") & " & Component count = " & compCount
                bResult = False
            End If
        Next
```

```
        Dim k as Long
	If expectedVolumes.Count > 0 Then
            For k = 1 To expectedVolumes.Count
                Debug.Print "No match found for expected interference: Volume = " & Format(expectedVolumes(k), "0.000000") & " & Component count = " & expectedCompCounts(k)
            Next
        End If
    End If
```

```
    VerifyInterferencesAgainstExpectation = bResult
End Function
```

```
Public Sub SelectAllComponents(swAssem As AssemblyDoc)
    Dim swModel As ModelDoc2
    Set swModel = swAssem
    swModel.ClearSelection2 True
```

```
    Dim vComponents As Variant
    vComponents = swAssem.GetComponents(True)
```

```
    If Not IsEmpty(vComponents) Then
        Dim vComp As Variant
        For Each vComp In vComponents
            Dim swComp As Component2
            Set swComp = vComp
            swComp.Select4 True, Nothing, False
        Next
    End If
End Sub
```

```
Back to top
```

'Class1

```
Option Explicit
```

```
Private swComp As Component2
Private swReferenceTransform As MathTransform
```

```
Public Sub RecordReferencePosition(swComponent As Component2)
    Set swComp = swComponent
    Set swReferenceTransform = swComp.Transform2
End Sub
```

```
Public Function IsAtReferencePosition() As Boolean
    Dim swCurrentTransform As MathTransform
    Set swCurrentTransform = swComp.Transform2
```

```
    Dim swProduct As MathTransform
    Set swProduct = swReferenceTransform.Multiply(swCurrentTransform.Inverse)
```

```
    Dim vProduct As Variant
    vProduct = swProduct.ArrayData
```

```
    ' Require identity transform
    Dim bResult As Boolean
    bResult = EqualWithinTolerance(vProduct(0), 1)
    bResult = EqualWithinTolerance(vProduct(1), 0) And bResult
    bResult = EqualWithinTolerance(vProduct(2), 0) And bResult
```

```
    bResult = EqualWithinTolerance(vProduct(3), 0) And bResult
    bResult = EqualWithinTolerance(vProduct(4), 1) And bResult
    bResult = EqualWithinTolerance(vProduct(5), 0) And bResult
```

```
    bResult = EqualWithinTolerance(vProduct(6), 0) And bResult
    bResult = EqualWithinTolerance(vProduct(7), 0) And bResult
    bResult = EqualWithinTolerance(vProduct(8), 1) And bResult
```

```
    bResult = EqualWithinTolerance(vProduct(9), 0) And bResult
    bResult = EqualWithinTolerance(vProduct(10), 0) And bResult
    bResult = EqualWithinTolerance(vProduct(11), 0) And bResult
```

```
    bResult = EqualWithinTolerance(vProduct(12), 1) And bResult
```

```
    If Not bResult Then
        Debug.Print Name & ":"
        Debug.Print Format(vProduct(0), "0.000000") & vbTab & Format(vProduct(1), "0.000000") & vbTab & Format(vProduct(2), "0.000000")
        Debug.Print Format(vProduct(3), "0.000000") & vbTab & Format(vProduct(4), "0.000000") & vbTab & Format(vProduct(5), "0.000000")
        Debug.Print Format(vProduct(6), "0.000000") & vbTab & Format(vProduct(7), "0.000000") & vbTab & Format(vProduct(8), "0.000000")
        Debug.Print Format(vProduct(9), "0.000000") & vbTab & Format(vProduct(10), "0.000000") & vbTab & Format(vProduct(11), "0.000000")
        Debug.Print Format(vProduct(12), "0.000000")
    End If
```

```
    IsAtReferencePosition = bResult
End Function
```

```
Public Property Get Name() As String
    Name = swComp.Name2
End Property
```

```
Back to top
```
