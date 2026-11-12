---
title: "Create and Remove Dictionaries Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_and_Remove_Dictionaries_Example_VBA.htm"
---

# Create and Remove Dictionaries Example (VBA)

This example shows how to create and release dictionaries.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight and open a drawing document.
' 5. Run the macro.
'
' Postconditions:
' 1.  Constructs a Circle.
' 2.  Gets the root dictionary of the document.
' 3.  Gets the existing table-style dictionary of the document.
' 4.  Gets the active style in the table-style dictionary and
'     prints the style type to the command window.
' 5.  Creates a dictionary in the root dictionary called Our_Dict
'     and prints the name of the dictionary to the command window.
' 6.  Adds an XRecord entry to Out_Dict dictionary and prints
'     the name of the XRecord to the command window.
' 7.  Creates an extension dictionary for the Circle.
' 8.  Adds XRecord entries to the Circle's extension dictionary.
' 9.  Reads the XRecord entries in the Circle's extension dictionary
'     and prints their data to the command window.
' 10. Removes the XRecord entries from the Circle's extension dictionary.
' 11. Releases and erases the Circle's extension dictionary and prints
'     confirmation to the command window.
'----------------------------------------------------------------
```

```
Option Explicit
```

```
    Sub main()
```

```
        Dim dsApp As DraftSight.Application
        Dim dsDoc As DraftSight.Document
```

```
        'Connect to DraftSight application
        Set dsApp = GetObject(, "DraftSight.Application")
```

```
        ' Abort any command currently running in DraftSight to avoid nested commands
        dsApp.AbortRunningCommand
```

```
        If dsApp Is Nothing Then
            Return
        End If
```

```
        'Get active document
        Set dsDoc = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MsgBox ("There are no open documents in DraftSight.")
            Return
        End If
```

```
        'Get command message
        Dim dsCmdMsg As DraftSight.CommandMessage
        Set dsCmdMsg = dsApp.GetCommandMessage()
```

```
        'Construct Circle
        Dim dsModel As DraftSight.Model
        Dim dsSketchMgr As DraftSight.SketchManager
        Set dsModel = dsDoc.GetModel()
        Set dsSketchMgr = dsModel.GetSketchManager()
        Dim dsCircle As DraftSight.Circle
        Set dsCircle = dsSketchMgr.InsertCircle(5, 5, 0, 10)
```

```
        'Get drawing's root dictionary
        Dim dsRootDict As DraftSight.Dictionary
        Set dsRootDict = dsDoc.GetNamedObjectsDictionary()
```

```
        ' Get an existing dictionary (e.g., each drawing has a table-style dictionary)
        Dim hasEntry As Boolean
        hasEntry = dsRootDict.hasEntry("ACAD_TABLESTYLE")
```

```
        If hasEntry Then
            Dim entityType As dsObjectType_e
            Dim entity As Object
            Set entity = dsRootDict.GetEntry("ACAD_TABLESTYLE", entityType)
```

```
            'Dictionary entries can be of arbitrary entity types
            'In this case, the arbitrary entity type should be a dictionary
            If entityType = dsObjectType_e.dsDictionaryType Then
                Dim dict As DraftSight.Dictionary
                Set dict = entity
```

```
                'Table-style dictionary should contain an active style
                Dim dsTblStyleMgr As DraftSight.TableStyleManager
                Set dsTblStyleMgr = dsDoc.GetTableStyleManager()
                Dim dsActiveTblStyle As DraftSight.TableStyle
                Set dsActiveTblStyle = dsTblStyleMgr.GetActiveTableStyle()
```

```
                Dim activeTblStyleEntryName As String
                activeTblStyleEntryName = dict.GetNameOf(dsActiveTblStyle)
```

```
                dsCmdMsg.PrintLine ("Active table-style entry: " & activeTblStyleEntryName)
            End If
        End If
```

```
        'Create a dictionary in root dictionary
        Dim dsOurDict As DraftSight.Dictionary
        Set dsOurDict = dsRootDict.CreateDictionary("Our_Dict")
```

```
        'New dictionary is entry in root dictionary
        'Check if dictionary has new entry
        Dim hasOurDict As Boolean
        hasOurDict = dsRootDict.hasEntry("Our_Dict")
        If hasOurDict Then
            dsCmdMsg.PrintLine ("Our_Dict dictionary added.")
        End If
```

```
        'Add XRecord entry
        Dim dsOurXRecord As DraftSight.xRecord
        Set dsOurXRecord = dsOurDict.CreateXRecord("Our_XRecord")
```

```
        'Check if dictionary has new entry
        Dim hasOurXRecord As Boolean
        hasOurXRecord = dsOurDict.hasEntry("Our_XRecord")
        If hasOurXRecord Then
            dsCmdMsg.PrintLine ("Our_XRecord XRecord added.")
        End If
```

```
        'XRecords can contain arbitrary data
        Dim dataCount As Long
        dataCount = dsOurXRecord.GetDataCount()
```

```
        'Add double data
        dsOurXRecord.InsertDoubleData dataCount, 20, 1.42
```

```
        dataCount = dsOurXRecord.GetDataCount()
```

```
        'Add string data
        dsOurXRecord.InsertStringData dataCount, 3, "XRecordstring data"
```

```
        'Each entity can have its own extension dictionary
        'Create extension dictionary for Circle entity
        Dim extDict As DraftSight.Dictionary
        Set extDict = dsCircle.CreateExtensionDictionary()
```

```
        'Add XRecords to Circle's extension dictionary
        Dim dsXRecord1 As DraftSight.xRecord
        Set dsXRecord1 = extDict.CreateXRecord("XRecord1")
        dsXRecord1.InsertStringData 0, 1, "part number"
        dsXRecord1.InsertInteger32Data 1, 90, 1
```

```
        Dim dsXRecord2 As DraftSight.xRecord
        Set dsXRecord2 = extDict.CreateXRecord("XRecord2")
        dsXRecord2.InsertStringData 0, 1, "Description"
        dsXRecord2.InsertStringData 1, 3, "Circle"
```

```
        'Read entries of Circle's extension dictionary
        Dim entitytypes As Variant
        Dim entries As Variant
        entries = extDict.GetEntries(entitytypes)
```

```
        Dim dsEntityTypes As Variant
        dsEntityTypes = entitytypes
        Dim index As Long
        Dim i As Long
        For index = 0 To UBound(dsEntityTypes)
            If dsEntityTypes(index) = dsObjectType_e.dsXRecordType Then
                Dim xRecord As DraftSight.xRecord
                Set xRecord = entries(index)
```

```
                If xRecord Is Nothing Then
                    Exit For
                End If
```

```
                Dim count As Long
                count = xRecord.GetDataCount()
```

```
                For i = 0 To count - 1
                    Dim dataType As dsCustomDataType_e
                    dataType = xRecord.GetDataType(i)
                    If dataType = dsCustomDataType_e.dsCustomDataType_String Then
                        Dim data As String
                        data = xRecord.GetStringData(i)
                        dsCmdMsg.PrintLine ("String data: " & data)
                    ElseIf dataType = dsCustomDataType_e.dsCustomDataType_Integer32 Then
                        Dim intData As Long
                        intData = xRecord.GetInteger32Data(i)
                        dsCmdMsg.PrintLine ("Int data: " & intData)
                    End If
                Next
            End If
        Next
```

```
        'Remove the XRecords in the Circle's extension dictionary
        extDict.RemoveEntry ("XRecord1")
        extDict.RemoveEntry ("XRecord2")
```

```
        'Release and erase the Circle's extension dictionary
        Dim removed As Boolean
        removed = dsCircle.ReleaseExtensionDictionary()
        If removed Then
            dsCmdMsg.PrintLine ("Circle's extension dictionary released and erased.")
        End If
```

```
    End Sub
```
