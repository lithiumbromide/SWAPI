---
title: "PostMessageToApplicationx64 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "PostMessageToApplicationx64"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PostMessageToApplicationx64.html"
---

# PostMessageToApplicationx64 Method (ISldWorks)

Posts a message to the application that invoked this method in 64-bit applications.

## Syntax

### Visual Basic (Declaration)

```vb
Sub PostMessageToApplicationx64( _
   ByVal Cookie As System.Integer, _
   ByVal UserData As System.Long _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim UserData As System.Long

instance.PostMessageToApplicationx64(Cookie, UserData)
```

### C#

```csharp
void PostMessageToApplicationx64(
   System.int Cookie,
   System.long UserData
)
```

### C++/CLI

```cpp
void PostMessageToApplicationx64(
   System.int Cookie,
   System.int64 UserData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Cookie`: Cookie specified in [ISwAddin::ConnectToSW](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.html)
- `UserData`: Additional message-specific information defined by the application

## VBA Syntax

See [SldWorks::PostMessageToApplicationx64](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~PostMessageToApplicationx64.html).

## Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS Design software.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::PostMessageToApplication Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PostMessageToApplication.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
