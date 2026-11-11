---
title: "Fire Application and Document Events Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Fire_Application_and_Document_Events_Example_CSharp.htm"
---

# Fire Application and Document Events Example (C#)

This example shows how to fire application and document events.

```
//------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add references to System and System.Windows.Forms.
// 5. Change the path and name of the image file to insert.
//    NOTE: Image must be a PNG file.
// 6. Start DraftSight, create, save, and close a drawing named
//    c:\test\circle.dwg.
// 7. Set a break point in the project where the project connects
//    to DraftSight.
// 8. Press F10 to step through the project.
//
// Postconditions: Message boxes pop up for all events,
// regardless if fired.  Read the the text in each message box
// before clicking OK to close it.
//--------------------------------------------------------------
```

```
using System;
using System.Runtime.InteropServices;
using System.Windows.Forms;
using DraftSight.Interop.dsAutomation;
```

```
    static class Program
    {
```

```
        static DraftSight.Interop.dsAutomation.Application dsApp = null;
        static Document dsDoc = null;
        static bool filePreOpenNotify;
        static bool filePostOpenNotify;
        static bool docDestroyNotify;
        static bool fileSavePreNotify;
        static bool fileSavePostNotify;
        static bool fileModifyNotify;
```

```
        static string docName = "c:\\test\\circle.dwg";
        static string imageFileName = "c:\\test\\note.png";
```

```
   public static void Main()
   {
	//Connect to DraftSight
	dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
	dsApp.AbortRunningCommand(); // abort any command currently running in DraftSight to avoid nested commands
```

```
        //Set up dsApp events
        AttachAppEventHandlers();
```

```
        //Open document
```

```
        filePostOpenNotify = false;
        filePreOpenNotify = false;
```

```
        dsDoc = (Document)dsApp.OpenDocument2(docName, dsDocumentOpenOption_e.dsDocumentOpen_Default, dsEncoding_e.dsEncoding_Default);
```

```
        if (dsDoc != null)
        {
            if (false == filePreOpenNotify)
            {
                MessageBox.Show("FileOpenPreNotify event wasn't fired while opening a document.");
            }
            if (false == filePostOpenNotify)
            {
                MessageBox.Show("FileOpenPostNotify event wasn't fired while opening a document.");
            }
        }
```

```
        //Set up dsDoc events
        AttachDocEventHandlers();
```

```
        //Modify document
	TestFileModifyEvents();
```

```
        //Save document as a different document
	TestFileSaveEvents();
```

```
        //Close documents
        CloseAllDocuments();
```

```
        //Detach events
        DetachEventHandlers();
```

```
	}
```

```
        //Attach dsApp event handlers
        static public void AttachAppEventHandlers()
        {
            AttachAppEvents();
        }
```

```
        static public void AttachAppEvents()
        {
            dsApp.FileOpenPostNotify += new _IApplicationEvents_FileOpenPostNotifyEventHandler(FileOpenPostNotify);
            dsApp.FileOpenPreNotify += new _IApplicationEvents_FileOpenPreNotifyEventHandler(FileOpenPreNotify);
        }
```

```
        //Attach dsDoc event handlers
        static public void AttachDocEventHandlers()
        {
            AttachDocEvents();
        }
```

```
        static public void AttachDocEvents()
        {
            dsDoc.FileSavePostNotify += new _IDocumentEvents_FileSavePostNotifyEventHandler(FileSavePostNotify);
            dsDoc.FileSavePreNotify += new _IDocumentEvents_FileSavePreNotifyEventHandler(FileSavePreNotify);
            dsDoc.ModifyNotify += new _IDocumentEvents_ModifyNotifyEventHandler(ModifyNotify);
            dsDoc.DestroyNotify += new _IDocumentEvents_DestroyNotifyEventHandler(DestroyNotify);
        }
```

```
        //Detach all event handlers
        static public void DetachEventHandlers()
        {
            dsApp.FileOpenPostNotify -= new _IApplicationEvents_FileOpenPostNotifyEventHandler(FileOpenPostNotify);
            dsApp.FileOpenPreNotify -= new _IApplicationEvents_FileOpenPreNotifyEventHandler(FileOpenPreNotify);
            dsDoc.FileSavePostNotify -= new _IDocumentEvents_FileSavePostNotifyEventHandler(FileSavePostNotify);
            dsDoc.FileSavePreNotify -= new _IDocumentEvents_FileSavePreNotifyEventHandler(FileSavePreNotify);
            dsDoc.ModifyNotify -= new _IDocumentEvents_ModifyNotifyEventHandler(ModifyNotify);
            dsDoc.DestroyNotify -= new _IDocumentEvents_DestroyNotifyEventHandler(DestroyNotify);
        }
```

```
        static public void TestFileModifyEvents()
        {
            filePreOpenNotify = false;
            filePostOpenNotify = false;
```

```
            ReferenceImage dsPicture = default(ReferenceImage);
```

```
            Model dsModel = default(Model);
            SketchManager dsSketchMgr = default(SketchManager);
```

```
            if ((dsDoc != null))
            {
                //Get model space
                dsModel = (Model)dsDoc.GetModel();
                if ((dsModel != null))
                {
                    //Get sketch manager
                    dsSketchMgr = (SketchManager)dsModel.GetSketchManager();
                    if ((dsSketchMgr != null))
                    {
                        fileModifyNotify = false;
```

```
                        //insert a picture in the model
                        dsPicture = (ReferenceImage)dsSketchMgr.InsertPicture(imageFileName, 0.0, 0.0, 0.0, 1.0, 0.0);
```

```
                        if ((dsPicture != null))
                        {
                            //Check if ModifyNotify event is fired
                            if (false == fileModifyNotify)
                            {
                                MessageBox.Show("ModifyNotify event wasn't fired while inserting a picture in the document.");
                            }
                        }
                        else
                        {
                            MessageBox.Show("ISketchManager::InsertPicture method returns Nothing for the '" + dsDoc.GetPathName() + "' document");
                        }
                    }
                    else
                    {
                        MessageBox.Show("IModel.GetSketchManager method returns Nothing for the '" + dsDoc.GetPathName() + "' document.");
                    }
                }
                else
                {
                    MessageBox.Show("IDocument.GetModel method returns Nothing for the '" + dsDoc.GetPathName() + "' document.");
                }
            }
            else
            {
                MessageBox.Show("IApplication.OpenDocument method returns Nothing for the '" + docName + "' document.");
            }
        }
```

```
        static public void TestFileSaveEvents()
        {
            dsDocumentSaveError_e saveError = default(dsDocumentSaveError_e);
```

```
            string savedDocName = null;
```

```
            if ((dsDoc != null))
            {
                fileSavePreNotify = false;
                fileSavePostNotify = false;
```

```
                //Save document
                savedDocName = docName + "_saved.dwg";
                dsDoc.SaveAs2(savedDocName, dsDocumentSaveAsOption_e.dsDocumentSaveAs_R2010_DWG, true, out saveError);
```

```
                if (saveError != dsDocumentSaveError_e.dsDocumentSave_Succeeded)
                {
                    MessageBox.Show("SaveAs method returns '" + saveError + "' error.");
                }
                else
                {
                    //Check FileSavePreNotify and FileSavePostNotify events
                    if (false == fileSavePreNotify)
                    {
                        MessageBox.Show("FileSavePreNotify event wasn't fired after saving the '" + docName + "' document");
                    }
                    if (false == fileSavePostNotify)
                    {
                        MessageBox.Show("FileSavePostNotify event wasn't fired after saving the '" + docName + "' document");
                    }
                }
            }
            else
            {
                MessageBox.Show("OpenDocument method returns Nothing for the '" + docName + "' document.");
            }
        }
```

```
        static public void CloseAllDocuments()
        {
            object[] dsDocs = null;
            int index = 0;
```

```
            docDestroyNotify = false;
```

```
            //Get documents
            dsDocs = (object[])dsApp.GetDocuments();
            if (dsDocs == null)
            {
                MessageBox.Show("No open documents.");
            }
            else
            {
                for (index = 0; index <= dsDocs.Length - 1; index++)
                {
                    dsDoc = (Document)dsDocs[index];
                    dsApp.CloseDocument(dsDoc.GetPathName(), false);
                    if (false == docDestroyNotify)
                    {
                        MessageBox.Show("DestroyNotify event wasn't fired after closing a document.");
                    }
                }
            }
        }
```

```
        static public void FileOpenPostNotify(Document Document)
        {
            filePostOpenNotify = true;
            MessageBox.Show("FileOpenPostNotify event was fired while opening a document.");
        }
```

```
        static public void FileOpenPreNotify(string FileName, dsDocumentOpenOption_e Option)
        {
            filePreOpenNotify = true;
            MessageBox.Show("FileOpenPreNotify event was fired while opening a document.");
        }
        static public void DestroyNotify()
        {
            docDestroyNotify = true;
            MessageBox.Show("DestroyNotify event was fired after closing a document.");
        }
        static public void FileSavePostNotify()
        {
            fileSavePostNotify = true;
            MessageBox.Show("FileSavePostNotify event was fired while saving a document.");
        }
        static public void FileSavePreNotify(string FileName, dsDocumentSaveAsOption_e SaveOption)
        {
            fileSavePreNotify = true;
            MessageBox.Show("FileSavePreNotify event was fired while saving a document.");
        }
        static public void ModifyNotify()
        {
            fileModifyNotify = true;
            MessageBox.Show("ModifyNotify event was fired while inserting a picture in a document.");
        }
    }
```
