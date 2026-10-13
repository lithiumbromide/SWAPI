---
title: "Get Block Information Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Block_Information_Example_VB.htm"
---

# Get Block Information Example (VBA)

This example shows how to get information about blocks in a drawing document. This example also shows how to migrate the now obsolete and not-supported block definition and block instance interfaces (IBlockDefinition and IBlockInstance) to the new block definition and sketch block instance interfaces (ISketchBlockDefinition and ISketchBlockInstance).

```vb
'----------------------------------------------
 ' Preconditions:
 ' 1. Open drawing with block definitions
 '    and instances.
 ' 2. Open the Immediate window.
 '
 ' Postconditions: Examine the Immediate window.
 '----------------------------------------------
Option Explicit
Sub main()
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swDraw                      As SldWorks.DrawingDoc
    Dim vBlockDef                   As Variant
    Dim vBlockInst                  As Variant

    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' OLD BLOCKS: Obsolete and not supported block
    '             interfaces as of SOLIDWORKS 2007
    'Dim swBlockDef                  As SldWorks.BlockDefinition
    'Dim swBlockInst                 As SldWorks.BlockInstance
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' NEW BLOCKS: New block interfaces as of SOLIDWORKS 2007
    Dim swBlockDef                  As SldWorks.SketchBlockDefinition
    Dim swBlockInst                 As SldWorks.SketchBlockInstance
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    Dim vNote                       As Variant
    Dim swNote                      As SldWorks.Note
    Dim vDispDim                    As Variant
    Dim swDispDim                   As SldWorks.DisplayDimension
    Dim swDim                       As SldWorks.Dimension
    Dim i                           As Long
    Dim j                           As Long
    Dim k                           As Long
    Dim bRet                        As Boolean

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' NEW BLOCKS: Additional declaration needed for new blocks
    Dim SwSketchMgr                 As SldWorks.SketchManager
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' NEW BLOCKS: For SketchBlockDefinition
    Set SwSketchMgr = swModel.SketchManager
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    Debug.Print "File = " & swModel.GetPathName

    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' OLD BLOCKS: Obsolete and not supported method to get block
    '             definitions
    'vBlockDef = swDraw.GetBlockDefinitions
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' NEW BLOCKS: New method to get block definitions
    vBlockDef = SwSketchMgr.GetSketchBlockDefinitions
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    If Not IsEmpty(vBlockDef) Then
        For i = 0 To UBound(vBlockDef)
            Set swBlockDef = vBlockDef(i)

            vBlockInst = swBlockDef.GetInstances
            vNote = swBlockDef.GetNotes
            vDispDim = swBlockDef.GetDisplayDimensions

            '''''''''''''''''''''''''''''''''''''''''''''''''''''''
            ' OLD BLOCKS: Obsolete and not supported block-related
            '             methods and properties
            'Debug.Print "  " & swBlockDef.Name
            'Debug.Print "    UseExternalFile = " & swBlockDef.GetUseExternalFile
            'Debug.Print "      ExternalFileName = " & swBlockDef.GetExternalFileName
            ''''''''''''''''''''''''''''''''''''''''''''''''''''''''

            ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
            ' NEW BLOCKS: New block-related properties for external files; no
            ' corresponding block definition Name property
            Debug.Print "      Block definition linked to file? " & swBlockDef.LinkToFile
            Debug.Print "         File name: " & swBlockDef.FileName
            ''''''''''''''''''''''''''''''''''''''''''''''''''''''''

            If Not IsEmpty(vNote) Then
                Debug.Print ""
                Debug.Print "    Notes:"
                For j = 0 To UBound(vNote)
                    Set swNote = vNote(j)

                    Debug.Print "      Tag Name         = " & swNote.TagName
                    Debug.Print "      Text             = " & swNote.GetText
                    Debug.Print ""

                Next j
            End If

            If Not IsEmpty(vDispDim) Then
                Debug.Print ""
                Debug.Print "    Dimensions:"
                For j = 0 To UBound(vDispDim)
                    Set swDispDim = vDispDim(j)
                    Set swDim = swDispDim.GetDimension
                    Debug.Print "      Name             = " & swDim.Name
                    Debug.Print "      FullName         = " & swDim.FullName
                    Debug.Print "      Type             = " & swDim.GetType
                    Debug.Print "      DrivenState      = " & swDim.DrivenState
                    Debug.Print "      ReadOnly         = " & swDim.ReadOnly
                    Debug.Print "      Value            = " & swDim.GetSystemValue2("") * 1000# & " mm"
                    Debug.Print "      TextAll          = " & swDispDim.GetText(swDimensionTextAll)
                    Debug.Print "      TextPrefix       = " & swDispDim.GetText(swDimensionTextPrefix)
                    Debug.Print "      TextSuffix       = " & swDispDim.GetText(swDimensionTextSuffix)
                    Debug.Print "      CalloutAbove     = " & swDispDim.GetText(swDimensionTextCalloutAbove)
                    Debug.Print "      CalloutBelow     = " & swDispDim.GetText(swDimensionTextCalloutBelow)
                    Debug.Print ""
                Next j
            End If

            If Not IsEmpty(vBlockInst) Then
                Debug.Print ""
                For j = 0 To UBound(vBlockInst)
                    Set swBlockInst = vBlockInst(j)
                    vNote = swBlockInst.GetAttributes

                    ''''''''''''''''''''''''''''''''''''''''''''''''''''''
                    ' NEW BLOCKS: Get block instance Name
                    Debug.Print "  Name of block instance: " & swBlockInst.Name
                    ''''''''''''''''''''''''''''''''''''''''''''''''''''''

                    Debug.Print "    Block instance(" & j & "):"
                    ' 1 radian = 180º/p = 57.295779513º or approximately 57.3º
                    Debug.Print "      Angle            = " & swBlockInst.Angle * 57.3 & " deg"
                    Debug.Print "      Scale            = " & swBlockInst.Scale
                    Debug.Print "      TextDisplay      = " & swBlockInst.TextDisplay
                    If Not IsEmpty(vNote) Then
                        Debug.Print "      Notes:"
                        For k = 0 To UBound(vNote)
                            Set swNote = vNote(k)
                            Debug.Print "        Tag Name         = " & swNote.TagName
                            Debug.Print "        Text             = " & swNote.GetText
                            Debug.Print ""
                        Next k
                    End If
                Next j
            End If
            Debug.Print "  ------------------------------------"

        Next i
    End If
End Sub
'------------------------------------
```
