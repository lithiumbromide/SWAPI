---
title: "Export BOMs to XML Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Export_BOMs_to_XML_Example_VBNET.htm"
---

# Export BOMs to XML Example (VB.NET)

SOLIDWORKS Design manages Bills of Materials (BOM) and controls the information within them. You can extract this information for use in downstream systems such as ERP or other business systems.

In SOLIDWORKS 2004 and later, BOMs are now features and appear during a traversal of the FeatureManager design tree. This example shows how to get to each BOM in a drawing document and save the BOM information to an XML file. You can transform this XML file using XSL or transfer the file to other systems.

```
'----------------------------------------------------------------------
' Preconditions:
' 1. Open a drawing document with at least on BOM.
' 2. Add a reference to Microsoft Scripting Runtime (right-click
'    the name of the project in the Project Explorer and click Add Reference >
'    the Browse tab > C:\windows\system32\scrrun.dll > OK.
'
' Postconditions:
' 1. Saves an XML file to the folder where the drawing document resides,
'    overwriting any existing file of the same name.
' 2. Examine the folder where the drawing document resides.
'
' NOTES:
' * XML tags are based on BOM column headings.
' * Invalid characters must be removed from the
'   column headings.
'  * XML schema is:
'            <BOMS>
'                <SHEET>
'                    <NAME>Sheet1</NAME>
'                    <BOM>
'                        <NAME>Bill Of Materials1</NAME>
'                        <TABLE>
'                            <ROW>
'                                <ITEM_NO>1</ITEM_NO>
'                                <PART_NUMBER>2004_Part</PART_NUMBER>
'                                <DESCRIPTION></DESCRIPTION>
'                                <QTY>2</QTY>
'                            </ROW>
'                            <ROW>
'                                <ITEM_NO>2</ITEM_NO>
'                                <PART_NUMBER>2004_Part</PART_NUMBER>
'                                <DESCRIPTION></DESCRIPTION>
'                                <QTY>1</QTY>
'                            </ROW>
'                            <ROW>
'                                <ITEM_NO>3</ITEM_NO>
'                                <PART_NUMBER>2004_Part</PART_NUMBER>
'                                <DESCRIPTION></DESCRIPTION>
'                                <QTY>1</QTY>
'                            </ROW>
'                            <ROW>
'                                <ITEM_NO>4</ITEM_NO>
'                                <PART_NUMBER>bead7</PART_NUMBER>
'                                <DESCRIPTION></DESCRIPTION>
'                                <QTY>1</QTY>
'                            </ROW>
'                        </TABLE>
'                    </BOM>
'                </SHEET>
'                <SHEET>
'                    <NAME>Sheet2</NAME>
'                    <BOM>
'                        <NAME>Bill Of Materials2</NAME>
'                        <TABLE>
'                            <ROW>
'                                <ITEM_NO>1</ITEM_NO>
'                                <PART_NUMBER>Assem3</PART_NUMBER>
'                                <DESCRIPTION></DESCRIPTION>
'                                <QTY>1</QTY>
'                            </ROW>
'                            <ROW>
'                                <ITEM_NO></ITEM_NO>
'                                <PART_NUMBER>  cylinder</PART_NUMBER>
'                                <DESCRIPTION></DESCRIPTION>
'                                <QTY>1</QTY>
'                            </ROW>
'                            <ROW>
'                                <ITEM_NO></ITEM_NO>
'                                <PART_NUMBER>  cylinder</PART_NUMBER>
'                                <DESCRIPTION></DESCRIPTION>
'                                <QTY>1</QTY>
'                            </ROW>
'                            <ROW>
'                                <ITEM_NO></ITEM_NO>
'                                <PART_NUMBER>  SimpleCube_A</PART_NUMBER>
'                                <DESCRIPTION></DESCRIPTION>
'                                <QTY>1</QTY>
'                            </ROW>
'                            <ROW>
'                                <ITEM_NO></ITEM_NO>
'                                <PART_NUMBER>  JoinedCyl</PART_NUMBER>
'                                <DESCRIPTION></DESCRIPTION>
'                                <QTY>1</QTY>
'                            </ROW>
'                        </TABLE>
'                    </BOM>
'                    <BOM>
'                        <NAME>Bill Of Materials3</NAME>
'                        <TABLE>
'                            <ROW>
'                                <ITEM_NO>8</ITEM_NO>
'                                <PART_NUMBER>2004_Part</PART_NUMBER>
'                                <DESCRIPTION></DESCRIPTION>
'                                <QTY>2</QTY>
'                            </ROW>
'                        </TABLE>
'                        <TABLE>
'                            <ROW>
'                                <ITEM_NO>9</ITEM_NO>
'                                <PART_NUMBER>2004_Part</PART_NUMBER>
'                                <DESCRIPTION></DESCRIPTION>
'                                <QTY>1</QTY>
'                            </ROW>
'                            <ROW>
'                                <ITEM_NO>10</ITEM_NO>
'                                <PART_NUMBER>2004_Part</PART_NUMBER>
'                                <DESCRIPTION></DESCRIPTION>
'                                <QTY>1</QTY>
'                            </ROW>
'                        </TABLE>
'                        <TABLE>
'                            <ROW>
'                                <ITEM_NO>11</ITEM_NO>
'                                <PART_NUMBER>bead7</PART_NUMBER>
'                                <DESCRIPTION></DESCRIPTION>
'                                <QTY>1</QTY>
'                            </ROW>
'                        </TABLE>
'                    </BOM>
'                    <BOM>
'                        <NAME>Bill Of Materials4</NAME>
'                        <TABLE>
'                            <TITLE>BOM Table 2</TITLE>
'                            <ROW>
'                                <ITEM_NO>1</ITEM_NO>
'                                <PART_NUMBER>cylinder</PART_NUMBER>
'                                <DESCRIPTION></DESCRIPTION>
'                                <QTY>1</QTY>
'                            </ROW>
'                            <ROW>
'                                <ITEM_NO>2</ITEM_NO>
'                                <PART_NUMBER>cylinder</PART_NUMBER>
'                                <DESCRIPTION></DESCRIPTION>
'                                <QTY>1</QTY>
'                            </ROW>
'                        </TABLE>
'                        <TABLE>
'                            <TITLE>BOM Table 2</TITLE>
'                            <ROW>
'                                <ITEM_NO>3</ITEM_NO>
'                                <PART_NUMBER>SimpleCube_A</PART_NUMBER>
'                                <DESCRIPTION></DESCRIPTION>
'                                <QTY>1</QTY>
'                            </ROW>
'                            <ROW>
'                                <ITEM_NO>4</ITEM_NO>
'                                <PART_NUMBER>JoinedCyl</PART_NUMBER>
'                                <DESCRIPTION></DESCRIPTION>
'                                <QTY>1</QTY>
'                            </ROW>
'                        </TABLE>
'                    </BOM>
'                </SHEET>
'            </BOMS>
'----------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics
Imports Scripting

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swDraw As DrawingDoc
        Dim swFeat As Feature
        Dim swBomFeat As BomFeature
        Dim sPathName As String
        Dim bIsFirstSheet As Boolean
        Dim fso As Scripting.FileSystemObject
        Dim XMLfile As Scripting.TextStream

        swModel = swApp.ActiveDoc
        swDraw = swModel
        bIsFirstSheet = True
        ' Strip off SOLIDWORKS file extension (slddrw)
        ' and add XML extension (xml)
        sPathName = swModel.GetPathName
        sPathName = Left(sPathName, Len(sPathName) - 6)
        sPathName = sPathName + "xml"
        fso = CreateObject("Scripting.FileSystemObject")
        XMLfile = fso.CreateTextFile(sPathName, True)
        XMLfile.WriteLine("<BOMS>")
        swFeat = swModel.FirstFeature
        Do While Not swFeat Is Nothing
            If "DrSheet" = swFeat.GetTypeName Then
                XMLfile.WriteLine("    <SHEET>")
                XMLfile.WriteLine("        <NAME>" + swFeat.Name + "</NAME>")
                bIsFirstSheet = False
            End If
            If "BomFeat" = swFeat.GetTypeName Then
                swBomFeat = swFeat.GetSpecificFeature2
                ProcessBomFeature(swApp, swModel, swBomFeat, XMLfile)
            End If
            swFeat = swFeat.GetNextFeature
            If Not swFeat Is Nothing Then
                If "DrSheet" = swFeat.GetTypeName And Not bIsFirstSheet Then
                    XMLfile.WriteLine("    </SHEET>")
                End If
            End If
        Loop

        XMLfile.WriteLine("    </SHEET>")
        XMLfile.WriteLine("</BOMS>")
        XMLfile.Close()

    End Sub

    Sub ProcessTableAnn(ByVal swApp As SldWorks, ByVal swModel As ModelDoc2, ByVal swTableAnn As TableAnnotation, ByVal XMLfile As Scripting.TextStream)
        Dim nNumRow As Integer
        Dim nNumCol As Integer
        Dim nNumHeader As Integer
        Dim sHeaderText() As String
        Dim j As Integer
        Dim k As Integer
        Dim nIndex As Integer
        Dim nCount As Integer
        Dim nStart As Integer
        Dim nEnd As Integer
        Dim nSplitDir As Integer
```

```
        nNumHeader = swTableAnn.GetHeaderCount : Debug.Assert(nNumHeader >= 1)
        nSplitDir = swTableAnn.GetSplitInformation(nIndex, nCount, nStart, nEnd)
        If swTableSplitDirection_e.swTableSplit_None = nSplitDir Then
            Debug.Assert(0 = nIndex)
            Debug.Assert(0 = nCount)
            Debug.Assert(0 = nStart)
            Debug.Assert(0 = nEnd)
            nNumRow = swTableAnn.RowCount
            nNumCol = swTableAnn.ColumnCount
            nStart = nNumHeader
            nEnd = nNumRow - 1
        Else
            Debug.Assert(swTableSplitDirection_e.swTableSplit_Horizontal = nSplitDir)
            Debug.Assert(nIndex >= 0)
            Debug.Assert(nCount >= 0)
            Debug.Assert(nStart >= 0)
            Debug.Assert(nEnd >= nStart)
            nNumCol = swTableAnn.ColumnCount
            If 1 = nIndex Then
                ' Add header offset for first portion of table
                nStart = nStart + nNumHeader
            End If
        End If
        XMLfile.WriteLine("            <TABLE>")
        If swTableAnn.TitleVisible Then
            XMLfile.WriteLine("                <TITLE>" & swTableAnn.Title & "</TITLE>")
        End If
        ReDim sHeaderText(nNumCol - 1)
        For j = 0 To nNumCol - 1
            sHeaderText(j) = swTableAnn.GetColumnTitle2(j, True)
            ' Replace invalid characters for XML tags
            sHeaderText(j) = Replace(sHeaderText(j), ".", "")
            sHeaderText(j) = Replace(sHeaderText(j), " ", "_")
        Next j
        For j = nStart To nEnd
            XMLfile.WriteLine("                <ROW>")
            For k = 0 To nNumCol - 1
                XMLfile.WriteLine("                    " + "<" + sHeaderText(k) + ">" + swTableAnn.Text2(j, k, True) + "</" + sHeaderText(k) + ">")
            Next k
            XMLfile.WriteLine("                </ROW>")
        Next j
        XMLfile.WriteLine("            </TABLE>")
    End Sub
    Sub ProcessBomFeature(ByVal swApp As SldWorks, ByVal swModel As ModelDoc2, ByVal swBomFeat As BomFeature, ByVal XMLfile As Scripting.TextStream)
        Dim swFeat As Feature
        Dim vTableArr As Object
        Dim vTable As Object
        Dim swTable As TableAnnotation

        swFeat = swBomFeat.GetFeature
        XMLfile.WriteLine("        <BOM>")
        XMLfile.WriteLine("            <NAME>" & swFeat.Name & "</NAME>")
        vTableArr = swBomFeat.GetTableAnnotations
        For Each vTable In vTableArr
            swTable = vTable
            ProcessTableAnn(swApp, swModel, swTable, XMLfile)
        Next vTable
        XMLfile.WriteLine("        </BOM>")
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
