---
title: "SetAddinCallbackInfo2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "SetAddinCallbackInfo2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetAddinCallbackInfo2.html"
---

# SetAddinCallbackInfo2 Method (ISldWorks)

Sets add-in callback commands.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetAddinCallbackInfo2( _
   ByVal ModuleHandle As System.Long, _
   ByVal AddinCallbacks As System.Object, _
   ByVal Cookie As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim ModuleHandle As System.Long
Dim AddinCallbacks As System.Object
Dim Cookie As System.Integer
Dim value As System.Boolean

value = instance.SetAddinCallbackInfo2(ModuleHandle, AddinCallbacks, Cookie)
```

### C#

```csharp
System.bool SetAddinCallbackInfo2(
   System.long ModuleHandle,
   System.object AddinCallbacks,
   System.int Cookie
)
```

### C++/CLI

```cpp
System.bool SetAddinCallbackInfo2(
   System.int64 ModuleHandle,
   System.Object^ AddinCallbacks,
   System.int Cookie
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModuleHandle`: Instance handle of the add-in
- `AddinCallbacks`: Object that includes the add-in callback methods
- `Cookie`: Add-in ID; this is the same cookie you specify in [ISwAddin::ConnectToSW](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.html)

### Return Value

True if the add-in callback commands are set, false if not

## VBA Syntax

See [SldWorks::SetAddinCallbackInfo2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~SetAddinCallbackInfo2.html).

## Examples

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::AddCallback Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddCallback.html)
[ISldWorks::RemoveCallback Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveCallback.html)
[ISldWorks::CallBack Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CallBack.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
