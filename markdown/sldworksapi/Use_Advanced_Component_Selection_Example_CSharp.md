---
title: "Use Advanced Component Selection Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Use_Advanced_Component_Selection_Example_CSharp.htm"
---

# Use Advanced Component Selection Example (C#)

This example shows how to:

- load an advanced selection component query file.
- select, add, delete, and save a selection criteria.

```
//-------------------------------------------------------
// Preconditions:
// 1. An assembly document is active.
// 2. A selection criteria query file named c:\temp\QueryMassLess.02.sqy
//    exists and contains one selection criteria.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Adds a selection criteria to c:\temp\QueryMassLess.02.sqy.
// 2. Deletes first selection criteria from c:\temp\QueryMassLess.02.sqy.
// 3. Saves selection criteria file c:\temp\QueryNewCriteria.sqy.
// 4. Examine the Immediate window and c:\temp.
//-------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace AdvancedSelectionCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 ModelDoc2 = default(ModelDoc2);
            ModelDoc2 = (ModelDoc2)swApp.ActiveDoc;

            int DocType = 0;
            DocType = ModelDoc2.GetType();

            if (DocType != (int)swDocumentTypes_e.swDocASSEMBLY)
            {
                Debug.Print("An assembly document is not active");
                return;
            }

            ModelDoc2.ClearSelection2(true);

            AssemblyDoc AssemblyDoc = default(AssemblyDoc);
            AssemblyDoc = (AssemblyDoc)ModelDoc2;

            AdvancedSelectionCriteria AdvancedSelectionCriteria = default(AdvancedSelectionCriteria);
            // Get advanced component selection
            AdvancedSelectionCriteria = (AdvancedSelectionCriteria)AssemblyDoc.GetAdvancedSelection();

            int Count = 0;
            // Get number of advanced component selections before loading a query
            // Should be 0
            Count = AdvancedSelectionCriteria.GetItemCount();
            Debug.Print("Before loading a query, GetItemCount returned " + Count);

            string CriteriaFileName = null;
            // Query file
            CriteriaFileName = "c:\\temp\\QueryMassLess.02.sqy";

            bool LoadSuccess = false;
            // Load query file
            LoadSuccess = AdvancedSelectionCriteria.LoadCriteria(CriteriaFileName);
            Debug.Print("Query " + CriteriaFileName + " load was" + (LoadSuccess == false ? " NOT " : " ") + "successful");
            ReportAllValues(AdvancedSelectionCriteria);
            bool SelectSuccess = false;
            // Select selection criteria from query list
            SelectSuccess = AdvancedSelectionCriteria.Select();
            Debug.Print("Select was" + (SelectSuccess == false ? " NOT " : " ") + "successful");

            int AddRetVal = 0;
            // Add selection criteria to query list
            AddRetVal = AdvancedSelectionCriteria.AddItem("Document name -- SW Special", 0x4, "Gear", false);
            Debug.Print("AddItem returned " + AddRetVal);

            // Print values of advanced component selection criteria
            ReportAllValues(AdvancedSelectionCriteria);

            // Select first advanced component selection criteria
            SelectSuccess = AdvancedSelectionCriteria.Select();
            Debug.Print("Select was" + (SelectSuccess == false ? " NOT " : " ") + "successful");
            bool DeleteStatus = false;
            // Delete first component selection criteria
            DeleteStatus = AdvancedSelectionCriteria.DeleteItem(0);
            Debug.Print("DeleteItem was" + (DeleteStatus == false ? " NOT " : " ") + "successful");

            ReportAllValues(AdvancedSelectionCriteria);
            bool SaveStatus = false;
            // Save query file
            SaveStatus = AdvancedSelectionCriteria.SaveCriteria("C:\\temp\\QueryNewCriteria.sqy");
            //If wanted, need to specify extension
            Debug.Print("SaveCriteria was" + (SaveStatus == false ? " NOT " : " ") + "successful");

            // Load query file that was just saved
            LoadSuccess = AdvancedSelectionCriteria.LoadCriteria("C:\\temp\\QueryNewCriteria.sqy");
            Debug.Print("Query " + "c:\\temp\\QueryNewCriteria.sqy" + " load was" + (LoadSuccess == false ? " NOT " : " ") + "successful");
            // Print contents query file
            ReportAllValues(AdvancedSelectionCriteria);
        }

        public string GetStringFromEnum(int EnumVal)
        {
            string functionReturnValue = null;
            //From enum swAdvSelecType_e
            if (EnumVal == 1)
            {
                functionReturnValue = "And";
            }
            else if (EnumVal == 2)
            {
                functionReturnValue = "Or";
            }
            else if (EnumVal == 16384)
            {
                functionReturnValue = "is yes";
            }
            else if (EnumVal == 32768)
            {
                functionReturnValue = "is no";
            }
            else if (EnumVal == 8)
            {
                functionReturnValue = "is not";
            }
            else if (EnumVal == 16)
            {
                functionReturnValue = "contains";
            }
            else if (EnumVal == 32)
            {
                functionReturnValue = "Is_Contained_By";
            }
            else if (EnumVal == 64)
            {
                functionReturnValue = "Interferes_With";
            }
            else if (EnumVal == 128)
            {
                functionReturnValue = "Does_Not_Interferes_With";
            }
            else if (EnumVal == 4)
            {
                functionReturnValue = "is (exactly)";
            }
            else if (EnumVal == 8192)
            {
                functionReturnValue = "not =";
            }
            else if (EnumVal == 512)
            {
                functionReturnValue = "<";
            }
            else if (EnumVal == 2048)
            {
                functionReturnValue = "<=";
            }
            else if (EnumVal == 4096)
            {
                functionReturnValue = "=";
            }
            else if (EnumVal == 1024)
            {
                functionReturnValue = ">=";
            }
            else if (EnumVal == 256)
            {
                functionReturnValue = ">";
            }
            else
            {
                functionReturnValue = "Condition NOT found";
            }
            return functionReturnValue;
        }
        public void ReportAllValues(AdvancedSelectionCriteria AdvancedSelectionCriteria)
        {
            Debug.Print("");

            int Count = 0;
            Count = AdvancedSelectionCriteria.GetItemCount();
            Debug.Print("GetItemCount returned " + Count);

            int i = 0;
            string aProperty = "";
            int Condition = 0;
            string Value = "";
            bool IsAnd = false;
            int Rindex = 0;
            string ConditionString = null;
            string PrintString = null;

            string IndexFmt = null;
            string RindexFmt = null;
            string AndOrFmt = null;
            string PropertyFmt = null;
            string ConditionFmt = null;
            string ValueFmt = null;
            IndexFmt = "!@@@@@@@@";
            RindexFmt = "!@@@@@@@@@";
            AndOrFmt = "!@@@@@@@@@";
            PropertyFmt = "!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";
            ConditionFmt = "!@@@@@@@@@@@@@@@";
            ValueFmt = "#.00";

            //Debug.Print
            PrintString = string.Format("Index", IndexFmt) + "     " + string.Format("Rindex", RindexFmt) + "  " + string.Format("And/Or", AndOrFmt) + "  " + string.Format("Property", PropertyFmt) + "                     " + string.Format("Condition", ConditionFmt) + "     " + string.Format("Value", ValueFmt);
            Debug.Print(PrintString);
            for (i = 0; i <= Count - 1; i++)
            {
                Rindex = AdvancedSelectionCriteria.GetItem(i, out aProperty, out Condition, out Value, out IsAnd);
                ConditionString = GetStringFromEnum(Condition);
                PrintString = string.Format(i.ToString(), IndexFmt) + "         " + string.Format(Rindex.ToString(), RindexFmt) + "       " + string.Format((IsAnd == false ? "OR" : "AND"), AndOrFmt) + "      " + string.Format(aProperty, PropertyFmt) + "  " + string.Format(ConditionString, ConditionFmt) + "  " + string.Format(Value, ValueFmt);
                Debug.Print(PrintString);
            }
            Debug.Print("");
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
