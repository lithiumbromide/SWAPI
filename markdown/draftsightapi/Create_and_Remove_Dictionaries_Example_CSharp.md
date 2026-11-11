---
title: "Create and Remove Dictionaries Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_and_Remove_Dictionaries_Example_CSharp.htm"
---

# Create and Remove Dictionaries Example (C#)

## Create and Release Dictionaries Example (C#)

This example shows how to create and release dictionaries.

```
//--------------------------------------------------------------
// Preconditions:
// 1.  Create a C# Windows console project.
// 2.  Copy and paste this example into the C# IDE.
// 3.  Add a reference to:
//     install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4.  Add references to System and System.Windows.Forms.
// 5.  Start DraftSight and open a document.
// 6.  Start debugging the project.
//
// Postconditions:
// 1.  Constructs a Circle.
// 2.  Gets the root dictionary of the document.
// 3.  Gets the existing table-style dictionary of the document.
// 4.  Gets the active style in the table-style dictionary and
//     prints the style type to the command window.
// 5.  Creates a dictionary in the root dictionary called Our_Dict
//     and prints the name of the dictionary to the command window.
// 6.  Adds an XRecord entry to Out_Dict dictionary and prints
//     the name of the XRecord to the command window.
// 7.  Creates an extension dictionary for the Circle.
// 8.  Adds XRecord entries to the Circle's extension dictionary.
// 9.  Reads the XRecord entries in the Circle's extension dictionary
//     and prints their data to the command window.
// 10. Removes the XRecord entries from the Circle's extension dictionary.
// 11. Releases and erases the Circle's extension dictionary and prints
//     confirmation to the command window.
//----------------------------------------------------------------

using System;
using DraftSight.Interop.dsAutomation;
using System.Runtime.InteropServices;
using System.Windows.Forms;

namespace DictionariesAndXRecords
{
    static class Program
    {

        static void Main(string[] args)
        {
            DraftSight.Interop.dsAutomation.Application dsApp;
            Document dsDoc;

            //Connect to DraftSight application
            dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

            // Abort any command currently running in DraftSight to avoid nested commands
            dsApp.AbortRunningCommand();

            if (null == dsApp)
            {
                return;
            }

            //Get active document
            dsDoc = dsApp.GetActiveDocument();
            if (null == dsDoc)
            {
                MessageBox.Show("There are no open documents in DraftSight.");
                return;
            }

            //Get command message
            CommandMessage dsCmdMsg = dsApp.GetCommandMessage();

            //Construct Circle
            Model dsModel;
            SketchManager dsSketchMgr;
            dsModel = dsDoc.GetModel();
            dsSketchMgr = dsModel.GetSketchManager();
            Circle dsCircle;
            dsCircle = dsSketchMgr.InsertCircle(5, 5, 0, 10);

            //Get drawing's root dictionary
            Dictionary dsRootDict;
            dsRootDict = dsDoc.GetNamedObjectsDictionary();

            // Get an existing dictionary (e.g., each drawing has a table-style dictionary)
            bool hasEntry;
            hasEntry = dsRootDict.HasEntry( "ACAD_TABLESTYLE" );

            if( hasEntry )
            {
                dsObjectType_e entityType;

                object entity;
                entity = dsRootDict.GetEntry( "ACAD_TABLESTYLE", out entityType );

                //Dictionary entries can be of arbitrary entity types
                //In this case, the arbitrary entity type should be a dictionary
                if( entityType == dsObjectType_e.dsDictionaryType )
                {
                    Dictionary dict;
                    dict = (Dictionary)entity;

                    //Table-style dictionary should contain an active style
                    TableStyleManager dsTblStyleMgr;
                    dsTblStyleMgr = dsDoc.GetTableStyleManager();
                    TableStyle dsActiveTblStyle;
                    dsActiveTblStyle = dsTblStyleMgr.GetActiveTableStyle();

                    string activeTblStyleEntryName;
                    activeTblStyleEntryName = dict.GetNameOf( dsActiveTblStyle );

                    dsCmdMsg.PrintLine( String.Format("Active table-style entry: {0}", activeTblStyleEntryName ) );
                }
            }

            //Create a dictionary in root dictionary
            Dictionary dsOurDict;
            dsOurDict = dsRootDict.CreateDictionary( "Our_Dict" );

            //New dictionary is entry in root dictionary
            //Check if dictionary has new entry
            bool hasOurDict;
            hasOurDict = dsRootDict.HasEntry( "Our_Dict" );
            if (hasOurDict)
                dsCmdMsg.PrintLine("\"Our_Dict\" dictionary added.");

            //Add XRecord entry
            XRecord dsOurXRecord;
            dsOurXRecord = dsOurDict.CreateXRecord( "Our_XRecord" );

            //Check if dictionary has new entry
            bool hasOurXRecord;
            hasOurXRecord = dsOurDict.HasEntry("Our_XRecord");
            if (hasOurXRecord)
                dsCmdMsg.PrintLine("\"Our_XRecord\" XRecord added.");

            //XRecords can contain arbitrary data
            int dataCount;
            dataCount = dsOurXRecord.GetDataCount();

            //Add double data
            dsOurXRecord.InsertDoubleData( dataCount, 20, 1.42 );

            dataCount = dsOurXRecord.GetDataCount();

            //Add string data
            dsOurXRecord.InsertStringData( dataCount, 3, "XRecordstring data" );

            //Each entity can have its own extension dictionary
            //Create extension dictionary for Circle entity
            Dictionary extDict;
            extDict = dsCircle.CreateExtensionDictionary();

            //Add XRecords to Circle's extension dictionary
            XRecord dsXRecord1;
            dsXRecord1 = extDict.CreateXRecord( "XRecord1" );
            dsXRecord1.InsertStringData( 0, 1, "part number" );
            dsXRecord1.InsertInteger32Data( 1, 90, 1 );

            XRecord dsXRecord2;
            dsXRecord2 = extDict.CreateXRecord( "XRecord2" );
            dsXRecord2.InsertStringData( 0, 1, "Description" );
            dsXRecord2.InsertStringData( 1, 3, "Circle" );

            //Read entries of Circle's extension dictionary
            object entitytypes = null;
            object[] entries = null;
            entries = extDict.GetEntries(out entitytypes) as object[];

            int[] dsEntityTypes = (int[])entitytypes;
            for ( int index = 0; index < dsEntityTypes.Length; ++index )
            {
                if( (dsObjectType_e)dsEntityTypes[index] == dsObjectType_e.dsXRecordType )
                {
                    XRecord xRecord;
                    xRecord = (XRecord)entries[index];

                    if( xRecord == null )
                        continue;

                    int count;
                    count = xRecord.GetDataCount();

                    for( int i = 0; i < count; ++i )
                    {
                        dsCustomDataType_e type = xRecord.GetDataType(i);
                        if( type == dsCustomDataType_e.dsCustomDataType_String )
                        {
                            string data;
                            data = xRecord.GetStringData(i);
                            dsCmdMsg.PrintLine( String.Format("String data: {0}",data));

                        }
                        else if ( type == dsCustomDataType_e.dsCustomDataType_Integer32 )
                        {
                            int intData;
                            intData = xRecord.GetInteger32Data(i);
                            dsCmdMsg.PrintLine(String.Format("Int data: {0}", intData));
                        }
                    }
                }
            }

            //Remove the XRecords in the Circle's extension dictionary
            extDict.RemoveEntry("XRecord1");
            extDict.RemoveEntry("XRecord2");

            //Release and erase the Circle's extension dictionary
            bool removed;
            removed = dsCircle.ReleaseExtensionDictionary();
            if (removed)
            {
                dsCmdMsg.PrintLine(String.Format("Circle's extension dictionary released and erased."));
            }
        }
    }
}
```
