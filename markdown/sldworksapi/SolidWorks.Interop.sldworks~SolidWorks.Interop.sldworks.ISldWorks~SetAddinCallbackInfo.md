---
title: "SetAddinCallbackInfo Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "SetAddinCallbackInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetAddinCallbackInfo.html"
---

# SetAddinCallbackInfo Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::SetAddinCallbackInfo2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetAddinCallbackInfo2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetAddinCallbackInfo( _
   ByVal ModuleHandle As System.Integer, _
   ByVal AddinCallbacks As System.Object, _
   ByVal Cookie As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim ModuleHandle As System.Integer
Dim AddinCallbacks As System.Object
Dim Cookie As System.Integer
Dim value As System.Boolean

value = instance.SetAddinCallbackInfo(ModuleHandle, AddinCallbacks, Cookie)
```

### C#

```csharp
System.bool SetAddinCallbackInfo(
   System.int ModuleHandle,
   System.object AddinCallbacks,
   System.int Cookie
)
```

### C++/CLI

```cpp
System.bool SetAddinCallbackInfo(
   System.int ModuleHandle,
   System.Object^ AddinCallbacks,
   System.int Cookie
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModuleHandle`: Instance handle of the add-in
- `AddinCallbacks`: Object that includes the add-in callback methods
- `Cookie`: Add-in ID; this is the same Cookie you specified in [ISwAddin::ConnectToSW](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.html)

### Return Value

True if the add-in callback commands are set, false if if not

## VBA Syntax

See [SldWorks::SetAddinCallbackInfo](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~SetAddinCallbackInfo.html).

## Examples

```vb
'-----------------------------------------
' Module-level variables
Dim iSldWorks                   As SldWorks.SldWorks
Dim iCookie                     As Long
'-----------------------------------------
'Implementation methods of the SwAddin interface
Private Function SwAddin_ConnectToSW(ByVal ThisSW As Object, ByVal Cookie As Long) As Boolean
    Dim bRet                As Boolean

    ' Store reference to SOLIDWORKS Design session
    Set iSldWorks = ThisSW

    ' Store cookie from SOLIDWORKS Design
    iCookie = Cookie

    'Inform SOLIDWORKS Design about the object that contains the callbacks
    bRet = iSldWorks.SetAddinCallbackInfo(App.hInstance, Me, iCookie)
    ...

    SwAddin_ConnectToSW = True
End Function
'-----------------------------------------
```

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::AddCallback Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddCallback.html)
[ISldWorks::CallBack Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CallBack.html)
[ISldWorks::RemoveCallback Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveCallback.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
