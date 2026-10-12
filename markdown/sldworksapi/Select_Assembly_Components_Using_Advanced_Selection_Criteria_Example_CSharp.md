---
title: "Select Assembly Components Using Advanced Selection Criteria Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Assembly_Components_Using_Advanced_Selection_Criteria_Example_CSharp.htm"
---

# Select Assembly Components Using Advanced Selection Criteria Example (C#)

This example shows how to select assembly components that are mated to a specified part.

```vb
 // -------------------------------------------------------
 // Preconditions:
 // 1. Open Public_Documents\SOLIDWORKS\SOLIDWORKS 2021\samples\tutorial\advdrawings\98food processor.sldasm.
 // 2. Create InContextHasMate.xml with the following content:
 //    <?xml version="1.0" encoding="UTF-8"?>
 //       <SWQueryList>
 //          <Query Name="InContextHasMate" Favourites_Index="1">
 //             <Boolean Name="And" Category="In Context Relations" SubCategory="Has mate to part" Condition="=" Value="base plate-1@98food processor"/>
 //          </Query>
 //       </SWQueryList>
 // 3. Place InContextHasMate.xml in c:\temp.
 // 4. Open the Immediate window.
 //
 // Postconditions: Inspect the Immediate window and the six selections
 // in the FeatureManager design tree.
 // -------------------------------------------------------
 using System;
 using System.Diagnostics;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Threading.Tasks;
 using System.Windows;
 using System.Windows.Forms;

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;

 namespace SelectComponents_CSharp
 {
       public  partial  class   SolidWorksMacro
      {
            public  void Main()
           {

                   AssemblyDoc swAssem;
                   ModelDoc2 swModel;
                    AdvancedSelectionCriteria criteria;
                   int Count;
                   string CriteriaFileName;
                   bool LoadSuccess;
                   int index;
                   bool SelectSuccess;
                   string category1;
                   string category2;
                   int condition;
                   string val;
                   bool isAnd;

                  swModel = (ModelDoc2)swApp.ActiveDoc;
                  swAssem = (AssemblyDoc)swModel;
                  criteria = swAssem.GetAdvancedSelection();

                  Count = criteria.GetItemCount();
                   Debug.Print("Before loading a query, GetItemCount returned " + Count);

                   // Query file
                  CriteriaFileName =   @"C:\temp\InContextHasMate.xml";

                   // Load query file
                  LoadSuccess = criteria.LoadCriteria(CriteriaFileName);

                  Count = criteria.GetItemCount();
                   Debug.Print("After loading a query, GetItemCount returned " + Count);

                   for (index = 0; index <= Count - 1; index++)
                  {
                       if (criteria.GetItem2(index,  out category1,  out category2,   out condition,   out val,   out isAnd) > -1)
                            Debug.Print(   " Criterion " + index +  ": " + category1 +  ", " + category2 +   ", " + condition +   ", " + val +   ", " + isAnd);
                      else
                            Debug.Print(   " Criterion " + index +  " not found");
                  }

                   Debug.Print(((SelectionMgr)(swModel.SelectionManager)).GetSelectedObjectCount2(-1) +   " objects selected before running query");

                  // Select components using selection criteria
                  SelectSuccess = criteria.Select();
                   Debug.Print("Select was successful: " + SelectSuccess);

                   Debug.Print(((SelectionMgr)(swModel.SelectionManager)).GetSelectedObjectCount2(-1) +   " objects selected after running query");

      }

       // The SldWorks swApp variable is pre-assigned for you.
       public  SldWorks swApp;

      }
 }
```
