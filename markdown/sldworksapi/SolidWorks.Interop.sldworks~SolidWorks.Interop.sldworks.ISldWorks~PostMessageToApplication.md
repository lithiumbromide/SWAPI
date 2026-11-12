---
title: "PostMessageToApplication Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "PostMessageToApplication"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PostMessageToApplication.html"
---

# PostMessageToApplication Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::PostMessageToApplicationx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PostMessageToApplicationx64.html).

This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016.

The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used.

Posts a message to the application that invoked this method.

## Syntax

### Visual Basic (Declaration)

```vb
Sub PostMessageToApplication( _
   ByVal Cookie As System.Integer, _
   ByVal UserData As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim UserData As System.Integer

instance.PostMessageToApplication(Cookie, UserData)
```

### C#

```csharp
void PostMessageToApplication(
   System.int Cookie,
   System.int UserData
)
```

### C++/CLI

```cpp
void PostMessageToApplication(
   System.int Cookie,
   System.int UserData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Cookie`: Cookie specified in [ISwAddin::ConnectToSW](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.html)
- `UserData`: Additional message-specific information defined by the application

## VBA Syntax

See [SldWorks::PostMessageToApplication](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~PostMessageToApplication.html).

## Examples

Contact SOLIDWORKS API Support to obtain either the 32-bit or 64-bit version of **C++ 32-bit and 64-bit Add-ins Post Messages After Every Selection**.

## Remarks

**All applications are required to be compatible with SOLIDWORKS x64. You must replace all calls to 32-bit only APIs with calls to their 64-bit safe counterparts.**

See [Eliminating 32-bit only API use](sldworksapiprogguide.chm::/Overview/Eliminating_32-Bit_Only_API_Use.htm) for more information.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::AddCallback Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddCallback.html)

## Availability

SOLIDWORKS 2010 SP1, Revision Number 18.1
