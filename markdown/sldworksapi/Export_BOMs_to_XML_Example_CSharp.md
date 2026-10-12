---
title: "Export BOMs to XML Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Export_BOMs_to_XML_Example_CSharp.htm"
---

# Export BOMs to XML Example (C#)

SOLIDWORKS Design manages Bills of Materials (BOM) and controls the information within them. You can extract this information for use in downstream systems such as ERP or other business systems.

In SOLIDWORKS 2004 and later, BOMs are now features and appear during a traversal of the FeatureManager design tree. This example shows how to get to each BOM in a drawing document and save the BOM information to an XML file. You can transform this XML file using XSL or transfer the file to other systems.

```
//----------------------------------------------------------------------
// Preconditions:
// 1. Open a drawing document with at least on BOM.
// 2. Add a reference to Microsoft Scripting Runtime (right-click
//    the name of the project in the Project Explorer and click Add Reference >
//    the Browse tab > C:\windows\system32\scrrun.dll > OK.
//
// Postconditions:
// 1. Saves an XML file to the folder where the drawing document resides,
//    overwriting any existing file of the same name.
// 2. Examine the folder where the drawing document resides.
//
// NOTES:
// * XML tags are based on BOM column headings.
// * Invalid characters must be removed from the
//   column headings.
//  * XML schema is:
//            <BOMS>
//                <SHEET>
//                    <NAME>Sheet1</NAME>
//                    <BOM>
//                        <NAME>Bill Of Materials1</NAME>
//                        <TABLE>
//                            <ROW>
//                                <ITEM_NO>1</ITEM_NO>
//                                <PART_NUMBER>2004_Part</PART_NUMBER>
//                                <DESCRIPTION></DESCRIPTION>
//                                <QTY>2</QTY>
//                            </ROW>
//                            <ROW>
//                                <ITEM_NO>2</ITEM_NO>
//                                <PART_NUMBER>2004_Part</PART_NUMBER>
//                                <DESCRIPTION></DESCRIPTION>
//                                <QTY>1</QTY>
//                            </ROW>
//                            <ROW>
//                                <ITEM_NO>3</ITEM_NO>
//                                <PART_NUMBER>2004_Part</PART_NUMBER>
//                                <DESCRIPTION></DESCRIPTION>
//                                <QTY>1</QTY>
//                            </ROW>
//                            <ROW>
//                                <ITEM_NO>4</ITEM_NO>
//                                <PART_NUMBER>bead7</PART_NUMBER>
//                                <DESCRIPTION></DESCRIPTION>
//                                <QTY>1</QTY>
//                            </ROW>
//                        </TABLE>
//                    </BOM>
//                </SHEET>
//                <SHEET>
//                    <NAME>Sheet2</NAME>
//                    <BOM>
//                        <NAME>Bill Of Materials2</NAME>
//                        <TABLE>
//                            <ROW>
//                                <ITEM_NO>1</ITEM_NO>
//                                <PART_NUMBER>Assem3</PART_NUMBER>
//                                <DESCRIPTION></DESCRIPTION>
//                                <QTY>1</QTY>
//                            </ROW>
//                            <ROW>
//                                <ITEM_NO></ITEM_NO>
//                                <PART_NUMBER>  cylinder</PART_NUMBER>
//                                <DESCRIPTION></DESCRIPTION>
//                                <QTY>1</QTY>
//                            </ROW>
//                            <ROW>
//                                <ITEM_NO></ITEM_NO>
//                                <PART_NUMBER>  cylinder</PART_NUMBER>
//                                <DESCRIPTION></DESCRIPTION>
//                                <QTY>1</QTY>
//                            </ROW>
//                            <ROW>
//                                <ITEM_NO></ITEM_NO>
//                                <PART_NUMBER>  SimpleCube_A</PART_NUMBER>
//                                <DESCRIPTION></DESCRIPTION>
//                                <QTY>1</QTY>
//                            </ROW>
//                            <ROW>
//                                <ITEM_NO></ITEM_NO>
//                                <PART_NUMBER>  JoinedCyl</PART_NUMBER>
//                                <DESCRIPTION></DESCRIPTION>
//                                <QTY>1</QTY>
//                            </ROW>
//                        </TABLE>
//                    </BOM>
//                    <BOM>
//                        <NAME>Bill Of Materials3</NAME>
//                        <TABLE>
//                            <ROW>
//                                <ITEM_NO>8</ITEM_NO>
//                                <PART_NUMBER>2004_Part</PART_NUMBER>
//                                <DESCRIPTION></DESCRIPTION>
//                                <QTY>2</QTY>
//                            </ROW>
//                        </TABLE>
//                        <TABLE>
//                            <ROW>
//                                <ITEM_NO>9</ITEM_NO>
//                                <PART_NUMBER>2004_Part</PART_NUMBER>
//                                <DESCRIPTION></DESCRIPTION>
//                                <QTY>1</QTY>
//                            </ROW>
//                            <ROW>
//                                <ITEM_NO>10</ITEM_NO>
//                                <PART_NUMBER>2004_Part</PART_NUMBER>
//                                <DESCRIPTION></DESCRIPTION>
//                                <QTY>1</QTY>
//                            </ROW>
//                        </TABLE>
//                        <TABLE>
//                            <ROW>
//                                <ITEM_NO>11</ITEM_NO>
//                                <PART_NUMBER>bead7</PART_NUMBER>
//                                <DESCRIPTION></DESCRIPTION>
//                                <QTY>1</QTY>
//                            </ROW>
//                        </TABLE>
//                    </BOM>
//                    <BOM>
//                        <NAME>Bill Of Materials4</NAME>
//                        <TABLE>
//                            <TITLE>BOM Table 2</TITLE>
//                            <ROW>
//                                <ITEM_NO>1</ITEM_NO>
//                                <PART_NUMBER>cylinder</PART_NUMBER>
//                                <DESCRIPTION></DESCRIPTION>
//                                <QTY>1</QTY>
//                            </ROW>
//                            <ROW>
//                                <ITEM_NO>2</ITEM_NO>
//                                <PART_NUMBER>cylinder</PART_NUMBER>
//                                <DESCRIPTION></DESCRIPTION>
//                                <QTY>1</QTY>
//                            </ROW>
//                        </TABLE>
//                        <TABLE>
//                            <TITLE>BOM Table 2</TITLE>
//                            <ROW>
//                                <ITEM_NO>3</ITEM_NO>
//                                <PART_NUMBER>SimpleCube_A</PART_NUMBER>
//                                <DESCRIPTION></DESCRIPTION>
//                                <QTY>1</QTY>
//                            </ROW>
//                            <ROW>
//                                <ITEM_NO>4</ITEM_NO>
//                                <PART_NUMBER>JoinedCyl</PART_NUMBER>
//                                <DESCRIPTION></DESCRIPTION>
//                                <QTY>1</QTY>
//                            </ROW>
//                        </TABLE>
//                    </BOM>
//                </SHEET>
//            </BOMS>
//----------------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using Scripting;
using System.Diagnostics;

namespace XMLCsharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            DrawingDoc swDraw = default(DrawingDoc);
            Feature swFeat = default(Feature);
            BomFeature swBomFeat = default(BomFeature);
            string sPathName = null;
            bool bIsFirstSheet = false;
            Scripting.FileSystemObject fso = default(Scripting.FileSystemObject);
            Scripting.TextStream XMLfile = default(Scripting.TextStream);

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swDraw = (DrawingDoc)swModel;
            bIsFirstSheet = true;
            // Strip off SOLIDWORKS file extension (slddrw)
            // and add XML extension (xml)
            sPathName = swModel.GetPathName();
            //sPathName = Strings.Left(sPathName, Strings.Len(sPathName) - 6);
            sPathName = sPathName.Substring(0, sPathName.Length - 6);
            sPathName = sPathName + "xml";
            //fso = Interaction.CreateObject("Scripting.FileSystemObject");
            fso = new Scripting.FileSystemObject();
            XMLfile = fso.CreateTextFile(sPathName, true, true);
            XMLfile.WriteLine("<BOMS>");
            swFeat = (Feature)swModel.FirstFeature();
            while ((swFeat != null))
            {
                if ("DrSheet" == swFeat.GetTypeName())
                {
                    XMLfile.WriteLine("    <SHEET>");
                    XMLfile.WriteLine("        <NAME>" + swFeat.Name + "</NAME>");
                    bIsFirstSheet = false;
                }
                if ("BomFeat" == swFeat.GetTypeName())
                {
                    swBomFeat = (BomFeature)swFeat.GetSpecificFeature2();
                    ProcessBomFeature(swApp, swModel, swBomFeat, XMLfile);
                }
                swFeat = (Feature)swFeat.GetNextFeature();
                if ((swFeat != null))
                {
                    if ("DrSheet" == swFeat.GetTypeName() & !bIsFirstSheet)
                    {
                        XMLfile.WriteLine("    </SHEET>");
                    }
                }
            }

            XMLfile.WriteLine("    </SHEET>");
            XMLfile.WriteLine("</BOMS>");
            XMLfile.Close();

        }

        public void ProcessTableAnn(SldWorks swApp, ModelDoc2 swModel, TableAnnotation swTableAnn, Scripting.TextStream XMLfile)
        {
            int nNumRow = 0;
            int nNumCol = 0;
            int nNumHeader = 0;
            string[] sHeaderText = null;
            int j = 0;
            int k = 0;
            int nIndex = 0;
            int nCount = 0;
            int nStart = 0;
            int nEnd = 0;
            int nSplitDir = 0;

            nNumHeader = swTableAnn.GetHeaderCount();
            Debug.Assert(nNumHeader >= 1);
            nSplitDir = swTableAnn.GetSplitInformation(ref nIndex, ref nCount, ref nStart, ref nEnd);
            if ((int)swTableSplitDirection_e.swTableSplit_None == nSplitDir)
            {
                Debug.Assert(0 == nIndex);
                Debug.Assert(0 == nCount);
                Debug.Assert(0 == nStart);
                Debug.Assert(0 == nEnd);
                nNumRow = swTableAnn.RowCount;
                nNumCol = swTableAnn.ColumnCount;
                nStart = nNumHeader;
                nEnd = nNumRow - 1;
            }
            else
            {
                Debug.Assert((int)swTableSplitDirection_e.swTableSplit_Horizontal == nSplitDir);
                Debug.Assert(nIndex >= 0);
                Debug.Assert(nCount >= 0);
                Debug.Assert(nStart >= 0);
                Debug.Assert(nEnd >= nStart);
                nNumCol = swTableAnn.ColumnCount;
                if (1 == nIndex)
                {
                    // Add header offset for first portion of table
                    nStart = nStart + nNumHeader;
                }
            }
            XMLfile.WriteLine("            <TABLE>");
            if (swTableAnn.TitleVisible)
            {
                XMLfile.WriteLine("                <TITLE>" + swTableAnn.Title + "</TITLE>");
            }
            sHeaderText = new string[nNumCol];
            for (j = 0; j <= nNumCol - 1; j++)
            {
                sHeaderText[j] = (string)swTableAnn.GetColumnTitle2(j, true);
                // Replace invalid characters for XML tags
                sHeaderText[j] = sHeaderText[j].Replace(".", "");
                sHeaderText[j] = sHeaderText[j].Replace(" ", "_");
            }
            for (j = nStart; j <= nEnd; j++)
            {
                XMLfile.WriteLine("                <ROW>");
                for (k = 0; k <= nNumCol - 1; k++)
                {
                    XMLfile.WriteLine("                    " + "<" + sHeaderText[k] + ">" + swTableAnn.get_Text2(j, k, true) + "</" + sHeaderText[k] + ">");
                }
                XMLfile.WriteLine("                </ROW>");
            }
            XMLfile.WriteLine("            </TABLE>");
        }
        public void ProcessBomFeature(SldWorks swApp, ModelDoc2 swModel, BomFeature swBomFeat, Scripting.TextStream XMLfile)
        {
            Feature swFeat = default(Feature);
            object[] vTableArr = null;
            object vTable = null;
            TableAnnotation swTable = default(TableAnnotation);

            swFeat = (Feature)swBomFeat.GetFeature();
            XMLfile.WriteLine("        <BOM>");
            XMLfile.WriteLine("            <NAME>" + swFeat.Name + "</NAME>");
            vTableArr = (object[])swBomFeat.GetTableAnnotations();
            foreach (object vTable_loopVariable in vTableArr)
            {
                vTable = vTable_loopVariable;
                swTable = (TableAnnotation)vTable;
                ProcessTableAnn(swApp, swModel, swTable, XMLfile);
            }
            XMLfile.WriteLine("        </BOM>");

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
