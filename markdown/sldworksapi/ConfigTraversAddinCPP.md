---
title: "Get Names of Configurations Using BSTR* C-array Example (C++)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/ConfigTraversAddinCPP.htm"
---

# Get Names of Configurations Using BSTR* C-array Example (C++)

// ConfigTraversAddin.cpp : Implementation of CConfigTraversAddin

// Add-in for getting the names of configurations in an active model document

// Demonstrates ModelDoc2::IGetConfigurationNames taking a BSTR* C-array

#include "stdafx.h"

#include "ConfigTraversAddin.h"

#include "BitmapHandler.h"

// CConfigTraversAddin

// This method adds the CommandManager to the SOLIDWORKS Design user-interface

void CConfigTraversAddin::AddCommandManager()

{

CComPtr<ICommandGroup> icmdGroup;

CComObject<CBitmapHandler> *iBmp;

CComObject<CBitmapHandler>::CreateInstance(&iBmp);

long cmdIndex0, cmdIndex1;

const int array_size = 2;

HRESULT hres;

int* docTypes = new int[array_size];

docTypes[0] = swDocASSEMBLY;

docTypes[1] = swDocDRAWING,

docTypes[2] = swDocPART;

CComBSTR title;

title.LoadString(IDS_TOOLBAR_TITLE);

CComBSTR hint;

hint.LoadString(IDS_MENU_HINT);

iCmdMgr->CreateCommandGroup(1,title,title,hint,-1,&icmdGroup);

CComBSTR smallImageFile;

iBmp->CreateBitmapFileFromResource(IDB_TOOLBAR_SMALL, &smallImageFile);

icmdGroup->put_SmallIconList(smallImageFile);

CComBSTR largeImageFile;

iBmp->CreateBitmapFileFromResource(IDB_TOOLBAR_LARGE, &largeImageFile);

icmdGroup->put_LargeIconList(largeImageFile);

CComBSTR largeIconFile;

iBmp->CreateBitmapFileFromResource(IDB_ICON_LARGE, &largeIconFile);

icmdGroup->put_LargeMainIcon(largeIconFile);

CComBSTR smallIconFile;

iBmp->CreateBitmapFileFromResource(IDB_ICON_SMALL, &smallIconFile);

icmdGroup->put_SmallMainIcon(smallIconFile);

CComBSTR tip;

CComBSTR callback;

CComBSTR enable;

long cmdIndex;

VARIANT_BOOL cmdActivated;

callback.LoadString(IDS_TOOLBAR_CALLBACK0);

enable.LoadString(IDS_TOOLBAR_ENABLE0);

tip.LoadString(IDS_TOOLBAR_TIP0);

hint.LoadString(IDS_TOOLBAR_HINT0);

icmdGroup->AddCommandItem(tip,-1,hint,tip,0,callback,enable,0,&cmdIndex0);

icmdGroup->put_HasToolbar(true);

icmdGroup->put_HasMenu(true);

icmdGroup->Activate(&cmdActivated);

for(int i=0; i < array_size + 1; i++)

{

CComPtr<ICommandTab> pTab = NULL;

long TabCount, docType = docTypes[i];

CComPtr<ICommandTab> AddinTab;

iCmdMgr->GetCommandTabCount(docType, &TabCount);

// Check for tab

iCmdMgr->GetCommandTab(docType, title, &pTab);

if(pTab == NULL)

{

// If no tab, then add one

iCmdMgr->AddCommandTab(docType, title, &pTab);

CComPtr<ICommandTabBox> pBox;

pTab->AddCommandTabBox(&pBox);

// Create two commands on this tab

long CommandIDCount = 2;

long* CommandIDs = new long[2];

long* TextDisplayStyles = new long[2];

long cmdID = 0;

// The two command buttons have different text styles

icmdGroup->get_CommandID(cmdIndex0, &cmdID);

CommandIDs[0] = cmdID;

TextDisplayStyles[0] = swCommandTabButton_TextHorizontal;

icmdGroup->get_ToolbarId(&cmdID);

CommandIDs[1] = cmdID;

TextDisplayStyles[1] = swCommandTabButton_TextHorizontal;

VARIANT_BOOL vbResult = VARIANT_FALSE;

pBox->IAddCommands(CommandIDCount, CommandIDs, TextDisplayStyles, &vbResult);

CommandIDCount = 1;

CommandIDs = new long[1];

TextDisplayStyles = new long[1];

icmdGroup->get_ToolbarId(&cmdID);

CommandIDs[0] = cmdID;

TextDisplayStyles[0] = swCommandTabButton_TextBelow | swCommandTabButton_ActionFlyout;

CComPtr<ICommandTabBox> pBox1;

pTab->AddCommandTabBox(&pBox1);

pBox1->IAddCommands(CommandIDCount, CommandIDs, TextDisplayStyles, &vbResult);

CComPtr<ICommandTabBox> pBoxNew1, pBoxNew2;

pTab->AddSeparator(pBox1, cmdID, &pBoxNew1);

}

}

// Clean up

iBmp->Dispose();

iBmp->Release();

}

void CConfigTraversAddin::RemoveCommandManager()

{

VARIANT_BOOL cmdRemoved;

iCmdMgr->RemoveCommandGroup(1,&cmdRemoved);

}

// Event handlers

// Called when the active document in SOLIDWORKS Design changes

STDMETHODIMP CConfigTraversAddin::OnDocChange(void)

{

// TODO: Add your implementation code here

return S_OK;

}

// Called when a new document is created or a document is loaded

STDMETHODIMP CConfigTraversAddin::OnDocLoad(BSTR docTitle, BSTR docPath)

{

// TODO: Add your implementation code here

return S_OK;

}

// Called when the active model document changes in SOLIDWORKS Design

STDMETHODIMP CConfigTraversAddin::OnModelDocChange(void)

{

// TODO: Add your implementation code here

return S_OK;

}

// Called when a new file is created

STDMETHODIMP CConfigTraversAddin::OnFileNew(LPDISPATCH newDoc, long docType, BSTR templateName)

{

// TODO: Add your implementation code here

return S_OK;

}

// Utility methods

// Set up the add-in to catch events

VARIANT_BOOL CConfigTraversAddin::AttachEventHandlers()

{

VARIANT_BOOL attached = VARIANT_TRUE;

this->m_libid = LIBID_SldWorks;

this->m_wMajorVerNum = GetSldWorksTlbMajor();

this->m_wMinorVerNum = 0;

CSldWorksEvents::_tih.m_wMajor = this->m_wMajorVerNum;

// Connect to the SldWorks event sink

HRESULT success = this->DispEventAdvise(iSwApp, &__uuidof(DSldWorksEvents));

if (success != S_OK)

return VARIANT_FALSE;

return attached;

}

// Stop listening for events

VARIANT_BOOL CConfigTraversAddin::DetachEventHandlers()

{

VARIANT_BOOL detached = VARIANT_TRUE;

// Disconnect from the SldWorks event sink

HRESULT success = this->DispEventUnadvise(iSwApp, &__uuidof(DSldWorksEvents));

CSldWorksEvents::_tih.m_plibid = &GUID_NULL;

if (success != S_OK)

return VARIANT_FALSE;

return detached;

}

// ISwAddin Methods

// This is the starting point for the add-in

STDMETHODIMP CConfigTraversAddin::ConnectToSW(LPDISPATCH ThisSW, long Cookie, VARIANT_BOOL * IsConnected)

{

ThisSW->QueryInterface(__uuidof(ISldWorks), (void**)&iSwApp);

addinID = Cookie;

iSwApp->GetCommandManager(Cookie,&iCmdMgr);

VARIANT_BOOL status = VARIANT_FALSE;

iSwApp->SetAddinCallbackInfo((long)_AtlBaseModule.GetModuleInstance(), static_cast<IConfigTraversAddin*>(this), addinID, &status);

// Get the current type library version

{

USES_CONVERSION;

CComBSTR bstrNum;

std::string strNum;

char *buffer;

iSwApp->RevisionNumber(&bstrNum);

strNum = W2A(bstrNum);

m_swMajNum = strtol(strNum.c_str(), &buffer, 10 );

m_swMinNum=0;

}

// Create the addin's user-interface

AddCommandManager();

// Listen for events

*IsConnected = AttachEventHandlers();

*IsConnected = VARIANT_TRUE;

return S_OK;

}

STDMETHODIMP CConfigTraversAddin::DisconnectFromSW(VARIANT_BOOL * IsDisconnected)

{

// Remove the addin's user-interface

RemoveCommandManager();

// Stop listening for events

*IsDisconnected = DetachEventHandlers();

iCmdMgr.Release();

// Make sure you release the SOLIDWORKS pointer last

iSwApp.Release();

return E_NOTIMPL;

}

// IConfigTraversAddin methods

// Menu and toolbar callbacks

STDMETHODIMP CConfigTraversAddin::ToolbarCallback0(void)

{

// Use ATL smart pointers

CComPtr<ISldWorks> swApp;

CComPtr<IModelDoc2> swModel;

swApp = iSwApp;

swApp->get_IActiveDoc2(&swModel);

if (! swModel) {

return(S_OK);

}

CComBSTR strModelTitle;

long nDocumentType; // swDocumentTypes_e

swModel->GetTitle(&strModelTitle);

swModel->GetType(&nDocumentType);

long lNumConfigurations;

swModel->GetConfigurationCount(&lNumConfigurations);

BSTR* aConfigurationNames = new BSTR[lNumConfigurations];

swModel->IGetConfigurationNames(&lNumConfigurations, aConfigurationNames);

for (int i = 0; i < lNumConfigurations; i++) {

CComBSTR bstrConfigurationName(aConfigurationNames[i]);

}

delete [] aConfigurationNames;

return(S_OK);

}

STDMETHODIMP CConfigTraversAddin::ToolbarEnable0(long* status)

{

// TODO: Add your implementation code here

*status = 1;

return S_OK;

}
