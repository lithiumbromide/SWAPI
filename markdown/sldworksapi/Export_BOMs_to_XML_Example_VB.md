---
title: "Export BOMs to XML Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Export_BOMs_to_XML_Example_VB.htm"
---

# Export BOMs to XML Example (VBA)

SOLIDWORKS Design manages Bills of Materials (BOM) and controls the information within them. You can extract this information for use in downstream systems such as ERP or other business systems.

In SOLIDWORKS 2004 and later, BOMs are now features and appear during a traversal of the FeatureManager design tree. This example shows how to get to each BOM in a drawing document and save the BOM information to an XML file. You can transform this XML file using XSL or transfer the file to other systems.

```
'----------------------------------------------------------------------
' Preconditions:
' 1. Open a drawing document with at least on BOM.
' 2. Add a reference to Microsoft Scripting Runtime (click
'    Tools > References > Browse > C:\windows\system32\scrrun.dll.
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
```

```
Option Explicit
```

```
Sub ProcessTableAnn(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swTableAnn As SldWorks.TableAnnotation, XMLfile As Scripting.TextStream)
```

```
    Dim nNumRow As Long
    Dim nNumCol As Long
    Dim nNumHeader As Long
    Dim sHeaderText() As String
    Dim j As Long
    Dim k  As Long
    Dim nIndex As Long
    Dim nCount As Long
    Dim nStart As Long
    Dim nEnd As Long
    Dim nSplitDir As Long
```

```
    nNumHeader = swTableAnn.GetHeaderCount: Debug.Assert nNumHeader >= 1
```

```
    nSplitDir = swTableAnn.GetSplitInformation(nIndex, nCount, nStart, nEnd)
```

```
    If swTableSplit_None = nSplitDir Then
        Debug.Assert 0 = nIndex
        Debug.Assert 0 = nCount
        Debug.Assert 0 = nStart
        Debug.Assert 0 = nEnd
        nNumRow = swTableAnn.RowCount
        nNumCol = swTableAnn.ColumnCount
        nStart = nNumHeader
        nEnd = nNumRow - 1
    Else
        Debug.Assert swTableSplit_Horizontal = nSplitDir
        Debug.Assert nIndex >= 0
        Debug.Assert nCount >= 0
        Debug.Assert nStart >= 0
        Debug.Assert nEnd >= nStart
        nNumCol = swTableAnn.ColumnCount
        If 1 = nIndex Then
            ' Add header offset for first portion of table
            nStart = nStart + nNumHeader
        End If
    End If
```

```
    XMLfile.WriteLine "            <TABLE>"
```

```
    If swTableAnn.TitleVisible Then
        XMLfile.WriteLine "                <TITLE>" & swTableAnn.Title & "</TITLE>"
    End If
```

```
    ReDim sHeaderText(nNumCol - 1)
```

```
    For j = 0 To nNumCol - 1
        sHeaderText(j) = swTableAnn.GetColumnTitle2(j, True)
        ' Replace invalid characters for XML tags
        sHeaderText(j) = Replace(sHeaderText(j), ".", "")
        sHeaderText(j) = Replace(sHeaderText(j), " ", "_")
    Next j
```

```
    For j = nStart To nEnd
        XMLfile.WriteLine "                <ROW>"
        For k = 0 To nNumCol - 1
            XMLfile.WriteLine "                    " + "<" + sHeaderText(k) + ">" + swTableAnn.Text2(j, k, True) + "</" + sHeaderText(k) + ">"
        Next k
```

```
        XMLfile.WriteLine "                </ROW>"
```

```
    Next j
```

```
    XMLfile.WriteLine "            </TABLE>"
```

```
End Sub
```

```
Sub ProcessBomFeature(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swBomFeat As SldWorks.BomFeature, XMLfile As Scripting.TextStream)
```

```
    Dim swFeat As SldWorks.Feature
    Dim vTableArr As Variant
    Dim vTable As Variant
    Dim swTable As SldWorks.TableAnnotation
```

```
    Set swFeat = swBomFeat.GetFeature
```

```
    XMLfile.WriteLine "        <BOM>"
    XMLfile.WriteLine "            <NAME>" & swFeat.Name & "</NAME>"
```

```
    vTableArr = swBomFeat.GetTableAnnotations
    For Each vTable In vTableArr
        Set swTable = vTable
        ProcessTableAnn swApp, swModel, swTable, XMLfile
    Next vTable
```

```
    XMLfile.WriteLine "        </BOM>"
```

```
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDraw As SldWorks.DrawingDoc
    Dim swFeat As SldWorks.Feature
    Dim swBomFeat As SldWorks.BomFeature
    Dim sPathName As String
    Dim bIsFirstSheet As Boolean
    Dim fso As Scripting.FileSystemObject
    Dim XMLfile As Scripting.TextStream
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
```

```
    bIsFirstSheet = True
```

```
    ' Strip off SOLIDWORKS file extension (slddrw)
    ' and add XML extension (xml)
    sPathName = swModel.GetPathName
    sPathName = Left(sPathName, Len(sPathName) - 6)
    sPathName = sPathName + "xml"
    Set fso = CreateObject("Scripting.FileSystemObject")
    Set XMLfile = fso.CreateTextFile(sPathName, True)
```

```
    XMLfile.WriteLine "<BOMS>"
```

```
    Set swFeat = swModel.FirstFeature
    Do While Not swFeat Is Nothing
        If "DrSheet" = swFeat.GetTypeName Then
            XMLfile.WriteLine "    <SHEET>"
            XMLfile.WriteLine "        <NAME>" + swFeat.Name + "</NAME>"
```

```
            bIsFirstSheet = False
        End If
```

```
        If "BomFeat" = swFeat.GetTypeName Then
            Set swBomFeat = swFeat.GetSpecificFeature2
            ProcessBomFeature swApp, swModel, swBomFeat, XMLfile
        End If
```

```
        Set swFeat = swFeat.GetNextFeature
        If Not swFeat Is Nothing Then
            If "DrSheet" = swFeat.GetTypeName And Not bIsFirstSheet Then
                XMLfile.WriteLine "    </SHEET>"
            End If
```

```
        End If
```

```
    Loop
```

```
    XMLfile.WriteLine "    </SHEET>"
    XMLfile.WriteLine "</BOMS>"
    XMLfile.Close
```

```
End Sub
```
