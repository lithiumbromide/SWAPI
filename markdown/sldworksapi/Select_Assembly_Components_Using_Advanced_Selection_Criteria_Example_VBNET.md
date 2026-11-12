---
title: "Select Assembly Components Using Advanced Selection Criteria Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Assembly_Components_Using_Advanced_Selection_Criteria_Example_VBNET.htm"
---

# Select Assembly Components Using Advanced Selection Criteria Example (VB.NET)

This example shows how to select assembly components that are mated to a specified part.

```vb
  '-------------------------------------------------------
 ' Preconditions:
 ' 1. Open Public_Documents\SOLIDWORKS\SOLIDWORKS 2021\samples\tutorial\advdrawings\98food processor.sldasm.
 ' 2. Create InContextHasMate.xml with the following content:
 '    <?xml version="1.0" encoding="UTF-8"?>
 '    <SWQueryList>
 '        <Query Name="InContextHasMate" Favourites_Index="1">
 '           <Boolean Name="And" Category="In Context Relations" SubCategory="Has mate to part" Condition="=" Value="base plate-1@98food processor"/>
 '        </Query>
 '    </SWQueryList>
 ' 3. Place InContextHasMate.xml in c:\temp.
 ' 4. Open the Immediate window.
 '
 ' Postconditions: Inspect the Immediate window and the six selections
 ' in the FeatureManager design tree.
  '-------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial   Class   SolidWorksMacro
       Public  Sub main()

            Dim swAssem  As  AssemblyDoc
            Dim criteria  As   AdvancedSelectionCriteria
            Dim Count  As  Integer
            Dim CriteriaFileName  As   String
            Dim LoadSuccess  As   Boolean
            Dim index  As  Integer
            Dim SelectSuccess  As   Boolean
            Dim category1  As   String
            Dim category2  As   String
            Dim condition  As   Integer
            Dim val  As  String
            Dim isAnd  As  Boolean

           swAssem = swApp.ActiveDoc
           criteria = swAssem.GetAdvancedSelection

           Count = criteria.GetItemCount
            Debug.Print("Before loading a query, GetItemCount returned " & Count)

            ' Query file
           CriteriaFileName =   "C:\temp\InContextHasMate.xml"

            ' Load query file
           LoadSuccess = criteria.LoadCriteria(CriteriaFileName)

           Count = criteria.GetItemCount
            Debug.Print("After loading a query, GetItemCount returned " & Count)

            For index = 0  To Count - 1
               If criteria.GetItem2(index, category1, category2, condition, val, isAnd) > -1  Then
                   Debug.Print(vbTab   " Criterion " & index    ": " & category1   ", " & category2    ", " & condition   ", " & val   ", " & isAnd)
               Else
                   Debug.Print(vbTab   " Criterion " & index    " not found")
               End  If
            Next

            Debug.Print(swAssem.SelectionManager.GetSelectedObjectCount2(-1)   " objects selected before running query")

            ' Select components using selection criteria
           SelectSuccess = criteria.Select
            Debug.Print("Select was" & IIf(SelectSuccess =  False,  " NOT ",   " ")    "successful")

            Debug.Print(swAssem.SelectionManager.GetSelectedObjectCount2(-1)   " objects selected after running query")

       End  Sub
       '''  <summary>
       ''' The SldWorks swApp variable is pre-assigned for you.
       '''  </summary>
       Public swApp  As  SldWorks
 End  Class
```
