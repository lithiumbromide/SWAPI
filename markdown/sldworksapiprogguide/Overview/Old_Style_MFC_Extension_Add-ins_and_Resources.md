---
title: "Old Style MFC Extension Add-ins and Resources"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Old_Style_MFC_Extension_Add-ins_and_Resources.htm"
---

# Old Style MFC Extension Add-ins and Resources

Old style MFC extension DLLs register resources in the SOLIDWORKS resource table. To avoid conflicts with SOLIDWORKS resources and to ensure that your add-in's resource IDs are unique, do a resource switch before loading any add-in resources.

### SwitchToAddinResource.h

```vb
class CSwitchToAddinResource
{
public:
CSwitchToAddinResource ()
{
if (NULL != mAddinResourceHandle)
{
iOldOne = AfxGetResourceHandle();
AfxSetResourceHandle(mAddinResourceHandle);
}
}
~CSwitchToAddinResource ()
{
if (NULL != mAddinResourceHandle)
{
AfxSetResourceHandle(iOldOne);
}
}
private:
HINSTANCE iOldOne;
static HINSTANCE mAddinResourceHandle;
};
```

### Addin.cpp

```vb
HINSTANCE CSwitchToAddinResource::mAddinResourceHandle = NULL;
DllMain()
{
CSwitchToAddinResource::mAddinResourceHandle = hInstance; // or
LoadLibrary(“AddinRes.dll”);
}
SomeResourceLoadingFunction()
{
CSwitchToAddinResource tmpAddinResources;
CString s;
s.LoadString(IDS_ADDIN_STRING);
}
```
