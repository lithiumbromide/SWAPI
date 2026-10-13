---
title: "DSldWorksEvents_ReferenceNotFoundNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_ReferenceNotFoundNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_ReferenceNotFoundNotifyEventHandler.html"
---

# DSldWorksEvents_ReferenceNotFoundNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies the user program before SOLIDWORKS displays a dialog box prompting the end-user to browse for the referenced file.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_ReferenceNotFoundNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_ReferenceNotFoundNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_ReferenceNotFoundNotifyEventHandler(
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_ReferenceNotFoundNotifyEventHandler(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Path and filename of the referenced file

## VBA Syntax

See [ReferenceNotFoundNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~ReferenceNotFoundNotify_EV.html).

## Examples

This code illustrates the proper use of this event:

```vb
HRESULT swAppEvents::AppReferenceNotFoundNotify (BSTR FileName)
{
static bool test = true;
TRACE( _T(" TestbedEvents - SldWorks.swAppReferenceNotFoundNotify event fired\n"));
if( test)
{
LPSLDWORKS pSldWorks = NULL;
m_lpObject->QueryInterface(IID_ISldWorks, (void**)&pSldWorks);
pSldWorks->SetMissingReferencePathName( FileName);
pSldWorks->Release();
return S_false;
}
else
return S_OK;
}
```

## Remarks

Use this event with [ISldWorks::SetMissingReferencePathName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetMissingReferencePathName.html). Returning S_false from your event handler successfully replaces the specified fileName with the filename specified in the call to ISldWorks::SetMissingReferencePathName.

This event is generated when a document is opened and one of its dependencies is not found.

If developing a C++ application, use [swAppReferenceNotFoundNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
