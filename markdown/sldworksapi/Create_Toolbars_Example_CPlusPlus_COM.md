---
title: "Create Toolbars Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Toolbars_Example_CPlusPlus_COM.htm"
---

# Create Toolbars Example (C++ COM)

Toolbars are added automatically by the C++ COM Addin Wizard, so you should examine the code that the wizard generates. An example is also included in this topic.

ISldWorks::AddToolbar4 takes bitmap filenames as arguments. You can create those filenames from resources using CreateBitmapFIleFromResource().

```vb
//This method adds the user toolbar to the SOLIDWORKS Design user interface
void CswSampleAddin::AddToolbar()
{
long docType = swDocTemplateTypePART;
CComBSTR title;
CComBSTR callback;
CComBSTR enable;
CComBSTR tip;
CComBSTR hint;
VARIANT_BOOL added;
long menuPos = 0; //Not used
title.LoadString(IDS_TOOLBAR_TITLE);
CComBSTR smallImageFile, largeImageFile;
bmp->CreateBitmapFileFromResource(IDB_TOOLBAR_SMALL, &smallImageFile);
bmp->CreateBitmapFileFromResource(IDB_TOOLBAR_LARGE, &largeImageFile);
iSwApp->AddToolbar4(addinID, title, smallImageFile, largeImageFile, menuPos, docType, &toolbarID);

callback.LoadString(IDS_TOOLBAR_CALLBACK0);
enable.LoadString(IDS_TOOLBAR_ENABLE0);
tip.LoadString(IDS_TOOLBAR_TIP0);
hint.LoadString(IDS_TOOLBAR_HINT0);
iSwApp->AddToolbarCommand2(addinID, toolbarID, 0, callback, enable, tip, hint, &added);
iSwApp->AddToolbarCommand2(addinID, toolbarID, 1, callback, enable, tip, hint, &added);
iSwApp->AddToolbarCommand2(addinID, toolbarID, 2, callback, enable, tip, hint, &added);
```
