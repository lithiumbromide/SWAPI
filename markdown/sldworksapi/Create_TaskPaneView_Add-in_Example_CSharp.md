---
title: "Create Task Pane View Add-in Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_TaskPaneView_Add-in_Example_CSharp.htm"
---

# Create Task Pane View Add-in Example (C#)

This example shows how to create an add-in that creates a Task Pane view and
notifies when the Task Pane view and Display Pane are exercised.

//----------------------------------------------------------------------------------------------------------------------------

1. Install the SOLIDWORKS API SDK templates using**SOLIDWORKS API SDK.msi**located in the apisdk folder of your SOLIDWORKS
  installation. If apisdk does not exist, modify your SOLIDWORKS
  installation from**Settings > Apps**(under Product
  Select, check**API Tools**and**SOLIDWORKS API SDK
  (install manually)).****apisdk/SOLIDWORKS API SDK.msi**will be installed in your installation folder.
2. Create a new project in Visual Studio using the
  SwCSharpAddin template.
3. Copy the following sample code intoSwAddin.csand EventHandling.cs of the new project.
4. Replace the Guid with a newly generated unique
  one if required (**VS menu > Tools > Create GUID**).
5. Add references to and modify the framework and
  build configuration of the project as needed.
6. Debug
  the program.

//------------------------------------------------------------------------------------------------------------------------------

#### //SwAddin.cs

using System;

using System.Runtime.InteropServices;

using System.Collections;

using System.Reflection;

using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swpublished;

using SolidWorks.Interop.swconst;

using SolidWorksTools;

using SolidWorksTools.File;

using System.Collections.Generic;

using System.Diagnostics;

namespace SwCSharpAddin1

{

/// <summary>

/// Summary description for SwCSharpAddin1.

/// </summary>

[Guid("d67ed0ef-3bc7-4f13-b3c8-2469ad715ea0"), ComVisible(true)]

[SwAddin(

Description = "SwCSharpAddin1 description",

Title = "SwCSharpAddin1",

LoadAtStartup = true

)]

public class SwAddin : ISwAddin

{

#region Local Variables

ISldWorks iSwApp = null;

ICommandManager iCmdMgr = null;

int addinID = 0;

TaskpaneView ctrl;

public const int mainCmdGroupID = 5;

public const int mainItemID1 = 0;

public const int mainItemID2 = 1;

public const int mainItemID3 = 2;

public const int flyoutGroupID = 91;

#region Event Handler Variables

Hashtable openDocs = new Hashtable();

SolidWorks.Interop.sldworks.SldWorks SwEventPtr = null;

#endregion

#region Property Manager Variables

UserPMPage ppage = null;

#endregion

// Public Properties

public ISldWorks SwApp

{

get { return iSwApp; }

}

public ICommandManager CmdMgr

{

get { return iCmdMgr; }

}

public Hashtable OpenDocs

{

get { return openDocs; }

}

public int Cookie

{

get { return addinID; }

}

#endregion

#region SolidWorks Registration

[ComRegisterFunctionAttribute]

public static void RegisterFunction ( Type t )

{

#region Get Custom Attribute: SwAddinAttribute

SwAddinAttribute SWattr = null;

Type type = typeof(SwAddin);

foreach (System.Attribute attr in type.GetCustomAttributes(false))

{

if (attr is SwAddinAttribute)

{

SWattr = attr as SwAddinAttribute;

break;

}

}

#endregion

try

{

Microsoft.Win32.RegistryKey hklm = Microsoft.Win32.Registry.LocalMachine;

Microsoft.Win32.RegistryKey hkcu = Microsoft.Win32.Registry.CurrentUser;

string keyname = "SOFTWARE\\SolidWorks\\Addins\\{" + t.GUID.ToString() +
"}";

Microsoft.Win32.RegistryKey addinkey = hklm.CreateSubKey(keyname);

addinkey.SetValue(null, 0);

addinkey.SetValue("Description", SWattr.Description);

addinkey.SetValue("Title", SWattr.Title);

keyname = "Software\\SolidWorks\\AddInsStartup\\{" + t.GUID.ToString() +
"}";

addinkey = hkcu.CreateSubKey(keyname);

addinkey.SetValue(null, Convert.ToInt32(SWattr.LoadAtStartup),
Microsoft.Win32.RegistryValueKind.DWord);

}

catch (System.NullReferenceException nl)

{

Console.WriteLine("There was a problem registering this dll: SWattr is
null. \n\"" + nl.Message + "\"");

System.Windows.Forms.MessageBox.Show("There was a problem registering
this dll: SWattr is null.\n\"" + nl.Message + "\"");

}

catch (System.Exception e)

{

Console.WriteLine(e.Message);

System.Windows.Forms.MessageBox.Show("There was a problem registering the
function: \n\"" + e.Message + "\"");

}

}

[ComUnregisterFunctionAttribute]

public static void UnregisterFunction ( Type t )

{

try

{

Microsoft.Win32.RegistryKey hklm = Microsoft.Win32.Registry.LocalMachine;

Microsoft.Win32.RegistryKey hkcu = Microsoft.Win32.Registry.CurrentUser;

string keyname = "SOFTWARE\\SolidWorks\\Addins\\{" + t.GUID.ToString() +
"}";

hklm.DeleteSubKey(keyname);

keyname = "Software\\SolidWorks\\AddInsStartup\\{" + t.GUID.ToString() +
"}";

hkcu.DeleteSubKey(keyname);

}

catch (System.NullReferenceException nl)

{

Console.WriteLine("There was a problem unregistering this dll: " +
nl.Message);

System.Windows.Forms.MessageBox.Show("There was a problem unregistering
this dll: \n\"" + nl.Message + "\"");

}

catch (System.Exception e)

{

Console.WriteLine("There was a problem unregistering this dll: " +
e.Message);

System.Windows.Forms.MessageBox.Show("There was a problem unregistering
this dll: \n\"" + e.Message + "\"");

}

}

#endregion

#region ISwAddin Implementation

public SwAddin ( )

{

}

public bool ConnectToSW ( object ThisSW, int cookie )

{

iSwApp = (ISldWorks)ThisSW;

addinID = cookie;

//Setup callbacks

iSwApp.SetAddinCallbackInfo(0, this, addinID);

// Register the callback for use with ISldWorks.PostMessageToApplication.

iSwApp.AddCallback(addinID, "AddInMessageCallback");

string[] bitmap = new string[1];

string toolTip;

bitmap[0] = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS
2024\\samples\\tutorial\\localhelp.bmp";

toolTip = "Extruded block tab";

ctrl = iSwApp. CreateTaskpaneView3 (bitmap, toolTip);

#region Setup the Event Handlers

SwEventPtr = (SolidWorks.Interop.sldworks.SldWorks)iSwApp;

openDocs = new Hashtable();

AttachEventHandlers();

#endregion

#region Setup Sample Property Manager

AddPMP();

#endregion

return true;

}

public bool DisconnectFromSW ( )

{

RemovePMP();

DetachEventHandlers();

iSwApp.RemoveCallback(addinID);

System.Runtime.InteropServices.Marshal.ReleaseComObject(iSwApp);

iSwApp = null;

//The addin _must_ call GC.Collect() here in order to retrieve all
managed code pointers

GC.Collect();

GC.WaitForPendingFinalizers();

GC.Collect();

GC.WaitForPendingFinalizers();

return true;

}

#endregion

// Ensure the dispatch pointer is marshalled correctly from the unmanaged
world into the managed world.

public bool AddInMessageCallback ( int cmd, int data,
[MarshalAs(UnmanagedType.IDispatch)] object dsp )

{

if (cmd != (int)swAppCallBackCmd_e.swAppPostNotifyEvent)

{

return (false);

}

// Check we are the intended recipient, by checking cookie value.

Debug.Assert(data == addinID);

AddinCallbackData callbackdata = (AddinCallbackData)dsp;

Trace.WriteLine("AddInMessageCallback called");

Trace.WriteLine(" operation = " + callbackdata.Operation.ToString());

Trace.WriteLine(" payload = " + callbackdata.Payload);

switch (callbackdata.Operation)

{

case AddinCallbackData.swCallbackOperation_e.swDoWork:

callbackdata.Handler.DoWorkCallback(callbackdata.Payload);

break;

case AddinCallbackData.swCallbackOperation_e.swDoMoreWork:

callbackdata.Handler.DoMoreWorkCallback(callbackdata.Payload + "; Added
some more work");

break;

default:

break;

}

// Cleanup: account for the call to Marshal.GetIDispatchForObject().

IntPtr pCallbackData = Marshal.GetIDispatchForObject(callbackdata);

Int32 refcnt =
Marshal.Release(pCallbackData);

return (true);

}

#region UI Methods

public void AddCommandMgr ( )

{

}

public void RemoveCommandMgr ( )

{

}

public Boolean AddPMP ( )

{

ppage = new UserPMPage(this);

return true;

}

public Boolean RemovePMP ( )

{

ppage = null;

return true;

}

#endregion

#region UI Callbacks

public void CreateCube ( )

{

//make sure we have a part open

string partTemplate =
iSwApp.GetUserPreferenceStringValue((int)swUserPreferenceStringValue_e.swDefaultTemplatePart);

if ((partTemplate != null) && (partTemplate != ""))

{

IModelDoc2 modDoc = (IModelDoc2)iSwApp.NewDocument(partTemplate,
(int)swDwgPaperSizes_e.swDwgPaperA2size, 0.0, 0.0);

modDoc.InsertSketch2(true);

modDoc.SketchRectangle(0, 0, 0, .1, .1, .1, false);

//Extrude the sketch

IFeatureManager featMan = modDoc.FeatureManager;

featMan.FeatureExtrusion(true,

false, false,

(int)swEndConditions_e.swEndCondBlind,
(int)swEndConditions_e.swEndCondBlind,

0.1, 0.0,

false, false,

false, false,

0.0, 0.0,

false, false,

false, false,

true,

false, false);

}

else

{

System.Windows.Forms.MessageBox.Show("There is no part template
available. Please check your options and make sure there is a part template
selected, or select a new part template.");

}

}

public void ShowPMP ( )

{

if (ppage != null)

ppage.Show();

}

public int EnablePMP ( )

{

if (iSwApp.ActiveDoc != null)

return 1;

else

return 0;

}

#endregion

#region Event Methods

public bool AttachEventHandlers ( )

{

AttachSwEvents();

//Listen for events on all currently open docs

AttachEventsToAllDocuments();

return true;

}

private bool AttachSwEvents ( )

{

try

{

SwEventPtr.ActiveDocChangeNotify += new
DSldWorksEvents_ActiveDocChangeNotifyEventHandler(OnDocChange);

SwEventPtr.DocumentLoadNotify2 += new
DSldWorksEvents_DocumentLoadNotify2EventHandler(OnDocLoad);

SwEventPtr.FileNewNotify2 += new
DSldWorksEvents_FileNewNotify2EventHandler(OnFileNew);

SwEventPtr.ActiveModelDocChangeNotify += new
DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler(OnModelChange);

SwEventPtr.FileOpenPostNotify += new
DSldWorksEvents_FileOpenPostNotifyEventHandler(FileOpenPostNotify);

SwEventPtr. TaskPaneShowNotify += new
DSldWorksEvents_ TaskPaneShowNotifyEventHandler (TaskpaneShowNotify);

SwEventPtr. TaskPaneHideNotify += new
DSldWorksEvents_ TaskPaneHideNotifyEventHandler (TaskpaneHideNotify);

SwEventPtr. TaskPanePinnedNotify += new
DSldWorksEvents_ TaskPanePinnedNotifyEventHandler (TaskpanePinnedNotify);

SwEventPtr. TaskPaneUnpinnedNotify += new
DSldWorksEvents_ TaskPaneUnpinnedNotifyEventHandler (TaskpaneUnpinnedNotify);

SwEventPtr. TaskPaneExpandNotify += new
DSldWorksEvents_ TaskPaneExpandNotifyEventHandler (TaskpanExpandNotify);

SwEventPtr. TaskPaneCollapseNotify += new
DSldWorksEvents_ TaskPaneCollapseNotifyEventHandler (TaskpaneCollapseNotify);

SwEventPtr. DisplayPaneActivationNotify += new
DSldWorksEvents_ DisplayPaneActivationNotifyEventHandler (DisplayPaneActivationNotify);

return true;

}

catch (Exception e)

{

Console.WriteLine(e.Message);

return false;

}

}

private bool DetachSwEvents ( )

{

try

{

SwEventPtr.ActiveDocChangeNotify -= new
DSldWorksEvents_ActiveDocChangeNotifyEventHandler(OnDocChange);

SwEventPtr.DocumentLoadNotify2 -= new
DSldWorksEvents_DocumentLoadNotify2EventHandler(OnDocLoad);

SwEventPtr.FileNewNotify2 -= new
DSldWorksEvents_FileNewNotify2EventHandler(OnFileNew);

SwEventPtr.ActiveModelDocChangeNotify -= new
DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler(OnModelChange);

SwEventPtr.FileOpenPostNotify -= new
DSldWorksEvents_FileOpenPostNotifyEventHandler(FileOpenPostNotify);

SwEventPtr. TaskPaneShowNotify += new
DSldWorksEvents_ TaskPaneShowNotifyEventHandler (TaskpaneShowNotify);

SwEventPtr. TaskPaneHideNotify += new
DSldWorksEvents_ TaskPaneHideNotifyEventHandler (TaskpaneHideNotify);

SwEventPtr. TaskPanePinnedNotify += new
DSldWorksEvents_ TaskPanePinnedNotifyEventHandler (TaskpanePinnedNotify);

SwEventPtr. TaskPaneUnpinnedNotify += new
DSldWorksEvents_ TaskPaneUnpinnedNotifyEventHandler (TaskpaneUnpinnedNotify);

SwEventPtr. TaskPaneExpandNotify += new
DSldWorksEvents_ TaskPaneExpandNotifyEventHandler (TaskpanExpandNotify);

SwEventPtr. TaskPaneCollapseNotify += new
DSldWorksEvents_ TaskPaneCollapseNotifyEventHandler (TaskpaneCollapseNotify);

SwEventPtr. DisplayPaneActivationNotify += new
DSldWorksEvents_ DisplayPaneActivationNotifyEventHandler (DisplayPaneActivationNotify);

return true;

}

catch (Exception e)

{

Console.WriteLine(e.Message);

return false;

}

}

public void AttachEventsToAllDocuments ( )

{

ModelDoc2 modDoc = (ModelDoc2)iSwApp.GetFirstDocument();

while (modDoc != null)

{

if (!openDocs.Contains(modDoc))

{

AttachModelDocEventHandler(modDoc);

}

modDoc = (ModelDoc2)modDoc.GetNext();

}

}

public bool AttachModelDocEventHandler ( ModelDoc2 modDoc )

{

if (modDoc == null)

return false;

DocumentEventHandler docHandler = null;

if (!openDocs.Contains(modDoc))

{

switch (modDoc.GetType())

{

case (int)swDocumentTypes_e.swDocPART:

{

docHandler = new PartEventHandler(modDoc, this);

break;

}

case (int)swDocumentTypes_e.swDocASSEMBLY:

{

docHandler = new AssemblyEventHandler(modDoc, this);

break;

}

case (int)swDocumentTypes_e.swDocDRAWING:

{

docHandler = new DrawingEventHandler(modDoc, this);

break;

}

default:

{

return false; //Unsupported document type

}

}

docHandler.AttachEventHandlers();

openDocs.Add(modDoc, docHandler);

}

return true;

}

public bool DetachModelEventHandler ( ModelDoc2 modDoc )

{

DocumentEventHandler docHandler;

docHandler = (DocumentEventHandler)openDocs[modDoc];

openDocs.Remove(modDoc);

modDoc = null;

docHandler = null;

return true;

}

public bool DetachEventHandlers ( )

{

DetachSwEvents();

//Close events on all currently open docs

DocumentEventHandler docHandler;

int numKeys = openDocs.Count;

object[] keys = new Object[numKeys];

//Remove all document event handlers

openDocs.Keys.CopyTo(keys, 0);

foreach (ModelDoc2 key in keys)

{

docHandler = (DocumentEventHandler)openDocs[key];

docHandler.DetachEventHandlers(); //This also removes the pair from the
hash

docHandler = null;

}

return true;

}

#endregion

#region Event Handlers

//Events

public int OnDocChange ( )

{

return 0;

}

public int OnDocLoad ( string docTitle, string docPath )

{

return 0;

}

int FileOpenPostNotify ( string FileName )

{

AttachEventsToAllDocuments();

return 0;

}

int TaskpaneShowNotify()

{

bool isVisible = iSwApp. IsTaskPaneVisible ();

Trace.WriteLine("Addin received - TaskpaneShowNotify");

return 0;

}

int TaskpaneHideNotify()

{

bool isVisible = iSwApp. IsTaskPaneVisible ();

Trace.WriteLine("Addin received - TaskpaneHideNotify");

return 0;

}

int TaskpanePinnedNotify()

{

bool isVisible = iSwApp. IsTaskPaneVisible ();

bool isActive = ctrl. IsActiveTab ();

Trace.WriteLine("Addin received - TaskpanePinnedNotify");

return 0;

}

int TaskpaneUnpinnedNotify()

{

Trace.WriteLine("Addin received - TaskpaneUnpinnedNotify");

return 0;

}

int TaskpaneExpandNotify()

{

bool isExpanded = iSwApp. IsTaskPaneExpanded ();

Trace.WriteLine("Addin received - TaskpaneExpandNotify");

return 0;

}

int TaskpaneCollapseNotify()

{

bool isExpanded = iSwApp. IsTaskPaneExpanded ();

Trace.WriteLine("Addin received - TaskpaneCollapseNotify");

return 0;

}

int
DisplayPaneActivationNotify(int ActivePaneIndex)

{

if(ActivePaneIndex == (int)swDisplayPaneIndex_e.swDisplayPaneNone)

MessageBox.Show("Nothing active");

else if(ActivePaneIndex ==
(int)swDisplayPaneIndex_e.swDisplayPaneLifeCycleTab)

MessageBox.Show("Life Cycle active");

else if(ActivePaneIndex == (int)swDisplayPaneIndex_e.swDisplayPaneTab)

MessageBox.Show("Display Pane active");

return 0;

}

public int OnFileNew ( object newDoc, int docType, string templateName )

{

AttachEventsToAllDocuments();

return 0;

}

public int OnModelChange ( )

{

return 0;

}

#endregion

}

}

//EventHandling.cs

using System;

using System.Collections;

//using SolidWorks.Interop.sldworks;

//using SolidWorks.Interop.swpublished;

//using SolidWorks.Interop.swconst;

using System.Runtime.InteropServices;

using System.Diagnostics;

using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swconst;

using System.Windows.Forms;

namespace SwCSharpAddin1

{

public class DocumentEventHandler

{

protected ISldWorks iSwApp;

protected ModelDoc2 document;

protected SwAddin userAddin;

protected Hashtable openModelViews;

public DocumentEventHandler ( ModelDoc2 modDoc, SwAddin addin )

{

document = modDoc;

userAddin = addin;

iSwApp = (ISldWorks)userAddin.SwApp;

openModelViews = new Hashtable();

}

virtual public bool DoWorkCallback ( string strDescription)

{

// No-op. To be overridden in derived class.

return (false);

}

virtual public bool DoMoreWorkCallback ( string strDescription )

{

// No-op. To be overridden in derived class.

return (false);

}

virtual public bool AttachEventHandlers ( )

{

return true;

}

virtual public bool DetachEventHandlers ( )

{

return true;

}

public bool ConnectModelViews ( )

{

IModelView mView;

mView = (IModelView)document.GetFirstModelView();

while (mView != null)

{

if (!openModelViews.Contains(mView))

{

DocView dView = new DocView(userAddin, mView, this);

dView.AttachEventHandlers();

openModelViews.Add(mView, dView);

}

mView = (IModelView)mView.GetNext();

}

return true;

}

public bool DisconnectModelViews ( )

{

//Close events on all currently open docs

DocView dView;

int numKeys;

numKeys = openModelViews.Count;

if (numKeys == 0)

{

return false;

}

object[] keys = new object[numKeys];

//Remove all ModelView event handlers

openModelViews.Keys.CopyTo(keys, 0);

foreach (ModelView key in keys)

{

dView = (DocView)openModelViews[key];

dView.DetachEventHandlers();

openModelViews.Remove(key);

dView = null;

}

return true;

}

public bool DetachModelViewEventHandler ( ModelView mView )

{

DocView dView;

if (openModelViews.Contains(mView))

{

dView = (DocView)openModelViews[mView];

openModelViews.Remove(mView);

mView = null;

dView = null;

}

return true;

}

}

public class PartEventHandler : DocumentEventHandler

{

PartDoc doc;

public PartEventHandler ( ModelDoc2 modDoc, SwAddin addin )

: base(modDoc, addin)

{

doc = (PartDoc)document;

}

override public bool DoWorkCallback ( string strDescription )

{

// Do some real work here.

Trace.WriteLine("Processing posted message in Part.DoWorkCallback");

Trace.WriteLine(" decription = " + strDescription);

return (true);

}

override public bool DoMoreWorkCallback ( string strDescription )

{

// Do some real work here.

Trace.WriteLine("Processing posted message in Part.DoMoreWorkCallback");

Trace.WriteLine(" decription = " + strDescription);

return (true);

}

override public bool AttachEventHandlers ( )

{

doc.DestroyNotify += new
DPartDocEvents_DestroyNotifyEventHandler(OnDestroy);

doc.NewSelectionNotify += new
DPartDocEvents_NewSelectionNotifyEventHandler(OnNewSelection);

doc.ModifyNotify += new
DPartDocEvents_ModifyNotifyEventHandler(OnModify);

doc.DisplayPaneExpandNotify += new DPartDocEvents_ DisplayPaneExpandNotifyEventHandler (OnDisplayPaneExpandNotify);

doc.DisplayPaneCollapseNotify += new DPartDocEvents_ DisplayPaneCollapseNotifyEventHandler (OnDisplayPaneCollapseNotify);

ConnectModelViews();

return true;

}

override public bool DetachEventHandlers ( )

{

doc.DestroyNotify -= new
DPartDocEvents_DestroyNotifyEventHandler(OnDestroy);

doc.NewSelectionNotify -= new
DPartDocEvents_NewSelectionNotifyEventHandler(OnNewSelection);

doc.ModifyNotify -= new
DPartDocEvents_ModifyNotifyEventHandler(OnModify);

doc.DisplayPaneExpandNotify -= new DPartDocEvents_ DisplayPaneExpandNotifyEventHandler (OnDisplayPaneExpandNotify);

doc.DisplayPaneCollapseNotify -= new DPartDocEvents_ DisplayPaneCollapseNotifyEventHandler (OnDisplayPaneCollapseNotify);

DisconnectModelViews();

userAddin.DetachModelEventHandler(document);

return true;

}

//Event Handlers

public int OnDestroy ( )

{

DetachEventHandlers();

return 0;

}

public int OnNewSelection ( )

{

return 0;

}

public int OnModify ( )

{

Trace.WriteLine("Deferring work in PartDoc.OnModify");

AddinCallbackData callbackdata = new
AddinCallbackData(AddinCallbackData.swCallbackOperation_e.swDoWork, this, "Work
on this. Greetings from PartDoc.OnModify");

// The returned pointer is one to the CCW for the managed object.

// That unmanaged CCW is referenced counted in COM style.

// So we assume it will be alive and in the same memory location for the
duration of the call back.

IntPtr pCallbackData = Marshal.GetIDispatchForObject(callbackdata);

if (Win32.Is64Bit())

{

iSwApp.PostMessageToApplicationx64(userAddin.Cookie,
pCallbackData.ToInt64());

}

else

{

iSwApp.PostMessageToApplication(userAddin.Cookie,
pCallbackData.ToInt32());

}

return 0;

}

public int OnDisplayPaneExpandNotify()

{

ModelDocExtension docExtn;

docExtn = document.Extension;

bool isvisible = docExtn. IsDisplayPaneVisible ();

int index = iSwApp. GetActiveDisplayPane ();

if (index == (int)swDisplayPaneIndex_e.swDisplayPaneNone)

MessageBox.Show("Nothing active");

else if (index == (int)swDisplayPaneIndex_e.swDisplayPaneLifeCycleTab)

MessageBox.Show("Life Cycle active");

else if (index == (int)swDisplayPaneIndex_e.swDisplayPaneTab)

MessageBox.Show("Display Pane active");

return 0;

}

public int OnDisplayPaneCollapseNotify()

{

ModelDocExtension docExtn;

docExtn = document.Extension;

bool isvisible = docExtn. IsDisplayPaneVisible ();

int index = iSwApp. GetActiveDisplayPane ();

if (index == (int)swDisplayPaneIndex_e.swDisplayPaneNone)

MessageBox.Show("Nothing active");

else if (index == (int)swDisplayPaneIndex_e.swDisplayPaneLifeCycleTab)

MessageBox.Show("Life Cycle active");

else if (index == (int)swDisplayPaneIndex_e.swDisplayPaneTab)

MessageBox.Show("Display Pane active");

return 0;

}

}

public class AssemblyEventHandler : DocumentEventHandler

{

AssemblyDoc doc;

SwAddin swAddin;

public AssemblyEventHandler ( ModelDoc2 modDoc, SwAddin addin )

: base(modDoc, addin)

{

doc = (AssemblyDoc)document;

swAddin = addin;

}

override public bool DoWorkCallback ( string strDescription )

{

// Do some real work here.

Trace.WriteLine("Processing posted message in Assembly.DoWorkCallback");

Trace.WriteLine(" decription = " + strDescription);

return (true);

}

override public bool DoMoreWorkCallback ( string strDescription )

{

// Do some real work here.

Trace.WriteLine("Processing posted message in
Assembly.DoMoreWorkCallback");

Trace.WriteLine(" decription = " + strDescription);

return (true);

}

override public bool AttachEventHandlers ( )

{

doc.DestroyNotify += new
DAssemblyDocEvents_DestroyNotifyEventHandler(OnDestroy);

doc.NewSelectionNotify += new
DAssemblyDocEvents_NewSelectionNotifyEventHandler(OnNewSelection);

doc.ComponentStateChangeNotify2 += new
DAssemblyDocEvents_ComponentStateChangeNotify2EventHandler(ComponentStateChangeNotify2);

doc.ComponentStateChangeNotify += new
DAssemblyDocEvents_ComponentStateChangeNotifyEventHandler(ComponentStateChangeNotify);

doc.ComponentVisualPropertiesChangeNotify += new
DAssemblyDocEvents_ComponentVisualPropertiesChangeNotifyEventHandler(ComponentVisualPropertiesChangeNotify);

doc.ComponentDisplayStateChangeNotify += new
DAssemblyDocEvents_ComponentDisplayStateChangeNotifyEventHandler(ComponentDisplayStateChangeNotify);

doc.ModifyNotify += new
DAssemblyDocEvents_ModifyNotifyEventHandler(OnModify);

doc.DisplayPaneExpandNotify += new DAssemblyDocEvents_ DisplayPaneExpandNotifyEventHandler (OnDisplayPaneExpandNotify);

doc.DisplayPaneCollapseNotify += new DAssemblyDocEvents_ DisplayPaneCollapseNotifyEventHandler (OnDisplayPaneCollapseNotify);

ConnectModelViews();

return true;

}

override public bool DetachEventHandlers ( )

{

doc.DestroyNotify -= new
DAssemblyDocEvents_DestroyNotifyEventHandler(OnDestroy);

doc.NewSelectionNotify -= new
DAssemblyDocEvents_NewSelectionNotifyEventHandler(OnNewSelection);

doc.ComponentStateChangeNotify2 -= new
DAssemblyDocEvents_ComponentStateChangeNotify2EventHandler(ComponentStateChangeNotify2);

doc.ComponentStateChangeNotify -= new
DAssemblyDocEvents_ComponentStateChangeNotifyEventHandler(ComponentStateChangeNotify);

doc.ComponentVisualPropertiesChangeNotify -= new
DAssemblyDocEvents_ComponentVisualPropertiesChangeNotifyEventHandler(ComponentVisualPropertiesChangeNotify);

doc.ComponentDisplayStateChangeNotify -= new
DAssemblyDocEvents_ComponentDisplayStateChangeNotifyEventHandler(ComponentDisplayStateChangeNotify);

doc.ModifyNotify -= new
DAssemblyDocEvents_ModifyNotifyEventHandler(OnModify);

doc.DisplayPaneExpandNotify -= new DAssemblyDocEvents_ DisplayPaneExpandNotifyEventHandler (OnDisplayPaneExpandNotify);

doc.DisplayPaneCollapseNotify -= new DAssemblyDocEvents_ DisplayPaneCollapseNotifyEventHandler (OnDisplayPaneCollapseNotify);

DisconnectModelViews();

userAddin.DetachModelEventHandler(document);

return true;

}

//Event Handlers

public int OnDestroy ( )

{

DetachEventHandlers();

return 0;

}

public int OnNewSelection ( )

{

return 0;

}

public int OnModify ( )

{

Trace.WriteLine("Deferring work in AssemblyDoc.OnModify");

AddinCallbackData callbackdata = new
AddinCallbackData(AddinCallbackData.swCallbackOperation_e.swDoMoreWork, this,
"Work on this. Greetings from AssemblyDoc.OnModify");

// The returned pointer is one to the CCW for the managed object.

// That unmanaged CCW is referenced counted in COM style.

// So we assume it will be alive and in the same memory location for the
duration of the call back.

IntPtr pCallbackData = Marshal.GetIDispatchForObject(callbackdata);

if (Win32.Is64Bit())

{

iSwApp.PostMessageToApplicationx64(userAddin.Cookie,
pCallbackData.ToInt64());

}

else

{

iSwApp.PostMessageToApplication(userAddin.Cookie,
pCallbackData.ToInt32());

}

return 0;

}

public int OnDisplayPaneExpandNotify()

{

ModelDocExtension docExtn;

docExtn = document.Extension;

bool isvisible = docExtn. IsDisplayPaneVisible ();

int index = iSwApp. GetActiveDisplayPane ();

if (index == (int)swDisplayPaneIndex_e.swDisplayPaneNone)

MessageBox.Show("Nothing active");

else if (index == (int)swDisplayPaneIndex_e.swDisplayPaneLifeCycleTab)

MessageBox.Show("Life Cycle active");

else if (index == (int)swDisplayPaneIndex_e.swDisplayPaneTab)

MessageBox.Show("Display Pane active");

return 0;

}

public int OnDisplayPaneCollapseNotify()

{

ModelDocExtension docExtn;

docExtn = document.Extension;

bool isvisible = docExtn. IsDisplayPaneVisible ();

int index = iSwApp. GetActiveDisplayPane ();

if (index == (int)swDisplayPaneIndex_e.swDisplayPaneNone)

MessageBox.Show("Nothing active");

else if (index == (int)swDisplayPaneIndex_e.swDisplayPaneLifeCycleTab)

MessageBox.Show("Life Cycle active");

else if (index == (int)swDisplayPaneIndex_e.swDisplayPaneTab)

MessageBox.Show("Display Pane active");

return 0;

}

//attach events to a component if it becomes resolved

protected int ComponentStateChange ( object componentModel, short
newCompState )

{

ModelDoc2 modDoc = (ModelDoc2)componentModel;

swComponentSuppressionState_e newState =
(swComponentSuppressionState_e)newCompState;

switch (newState)

{

case swComponentSuppressionState_e.swComponentFullyResolved:

{

if ((modDoc != null) &
!this.swAddin.OpenDocs.Contains(modDoc))

{

this.swAddin.AttachModelDocEventHandler(modDoc);

}

break;

}

case swComponentSuppressionState_e.swComponentResolved:

{

if ((modDoc != null) & !this.swAddin.OpenDocs.Contains(modDoc))

{

this.swAddin.AttachModelDocEventHandler(modDoc);

}

break;

}

}

return 0;

}

protected int ComponentStateChange ( object componentModel )

{

ComponentStateChange(componentModel,
(short)swComponentSuppressionState_e.swComponentResolved);

return 0;

}

public int ComponentStateChangeNotify2 ( object componentModel, string
CompName, short oldCompState, short newCompState )

{

return ComponentStateChange(componentModel, newCompState);

}

int ComponentStateChangeNotify ( object componentModel, short
oldCompState, short newCompState )

{

return ComponentStateChange(componentModel, newCompState);

}

int ComponentDisplayStateChangeNotify ( object swObject )

{

Component2 component = (Component2)swObject;

ModelDoc2 modDoc = (ModelDoc2)component.GetModelDoc();

return ComponentStateChange(modDoc);

}

int ComponentVisualPropertiesChangeNotify ( object swObject )

{

Component2 component = (Component2)swObject;

ModelDoc2 modDoc = (ModelDoc2)component.GetModelDoc();

return ComponentStateChange(modDoc);

}

}

public class DrawingEventHandler : DocumentEventHandler

{

DrawingDoc doc;

public DrawingEventHandler ( ModelDoc2 modDoc, SwAddin addin )

: base(modDoc, addin)

{

doc = (DrawingDoc)document;

}

override public bool AttachEventHandlers ( )

{

doc.DestroyNotify += new
DDrawingDocEvents_DestroyNotifyEventHandler(OnDestroy);

doc.NewSelectionNotify += new
DDrawingDocEvents_NewSelectionNotifyEventHandler(OnNewSelection);

doc.DisplayPaneExpandNotify += new DDrawingDocEvents_ DisplayPaneExpandNotifyEventHandler (OnDisplayPaneExpandNotify);

doc.DisplayPaneCollapseNotify += new DDrawingDocEvents_ DisplayPaneCollapseNotifyEventHandler (OnDisplayPaneCollapseNotify);

ConnectModelViews();

return true;

}

public int OnDisplayPaneExpandNotify()

{

ModelDocExtension docExtn;

docExtn = document.Extension;

bool isvisible = docExtn. IsDisplayPaneVisible ();

int index = iSwApp. GetActiveDisplayPane ();

if (index == (int)swDisplayPaneIndex_e.swDisplayPaneNone)

MessageBox.Show("Nothing active");

else if (index == (int)swDisplayPaneIndex_e.swDisplayPaneLifeCycleTab)

MessageBox.Show("Life Cycle active");

else if (index == (int)swDisplayPaneIndex_e.swDisplayPaneTab)

MessageBox.Show("Display Pane active");

return 0;

}

public int OnDisplayPaneCollapseNotify()

{

ModelDocExtension docExtn;

docExtn = document.Extension;

bool isvisible = docExtn. IsDisplayPaneVisible ();

int index = iSwApp. GetActiveDisplayPane ();

if (index == (int)swDisplayPaneIndex_e.swDisplayPaneNone)

MessageBox.Show("Nothing active");

else if (index == (int)swDisplayPaneIndex_e.swDisplayPaneLifeCycleTab)

MessageBox.Show("Life Cycle active");

else if (index == (int)swDisplayPaneIndex_e.swDisplayPaneTab)

MessageBox.Show("Display Pane active");

return 0;

}

override public bool DetachEventHandlers ( )

{

doc.DestroyNotify -= new
DDrawingDocEvents_DestroyNotifyEventHandler(OnDestroy);

doc.NewSelectionNotify -= new
DDrawingDocEvents_NewSelectionNotifyEventHandler(OnNewSelection);

DisconnectModelViews();

userAddin.DetachModelEventHandler(document);

return true;

}

//Event Handlers

public int OnDestroy ( )

{

DetachEventHandlers();

return 0;

}

public int OnNewSelection ( )

{

return 0;

}

}

public class DocView

{

ISldWorks iSwApp;

SwAddin userAddin;

ModelView mView;

DocumentEventHandler parent;

public DocView ( SwAddin addin, IModelView mv, DocumentEventHandler doc )

{

userAddin = addin;

mView = (ModelView)mv;

iSwApp = (ISldWorks)userAddin.SwApp;

parent = doc;

}

public bool AttachEventHandlers ( )

{

mView.DestroyNotify2 += new
DModelViewEvents_DestroyNotify2EventHandler(OnDestroy);

mView.RepaintNotify += new
DModelViewEvents_RepaintNotifyEventHandler(OnRepaint);

return true;

}

public bool DetachEventHandlers ( )

{

mView.DestroyNotify2 -= new
DModelViewEvents_DestroyNotify2EventHandler(OnDestroy);

mView.RepaintNotify -= new
DModelViewEvents_RepaintNotifyEventHandler(OnRepaint);

parent.DetachModelViewEventHandler(mView);

return true;

}

//EventHandlers

public int OnDestroy ( int destroyType )

{

return 0;

}

public int OnRepaint ( int repaintType )

{

return 0;

}

}

}
