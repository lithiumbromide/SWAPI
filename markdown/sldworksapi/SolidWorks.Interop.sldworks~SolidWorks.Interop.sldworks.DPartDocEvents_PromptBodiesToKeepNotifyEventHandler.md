---
title: "DPartDocEvents_PromptBodiesToKeepNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_PromptBodiesToKeepNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_PromptBodiesToKeepNotifyEventHandler.html"
---

# DPartDocEvents_PromptBodiesToKeepNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Generated when a body is cut into multiple bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_PromptBodiesToKeepNotifyEventHandler( _
   ByVal Feature As System.Object, _
   ByRef Bodies As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_PromptBodiesToKeepNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_PromptBodiesToKeepNotifyEventHandler(
   System.object Feature,
   ref System.object Bodies
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_PromptBodiesToKeepNotifyEventHandler(
   System.Object^ Feature,
   System.Object^% Bodies
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Feature`: [Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)
- `Bodies`: Array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [PromptBodiesToKeepNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~PromptBodiesToKeepNotify_EV.html).

## Examples

[Cut Body and Keep All Bodies (C#)](Cut_Body_and_Keep_All_Bodies_Example_CSharp.htm)
[Cut Body and Keep All Bodies (VB.NET)](Cut_Body_and_Keep_All_Bodies_Example_VBNET.htm)
[Cut Body and Keep All Bodies (VBA)](Cut_Body_and_Keep_All_Bodies_Example_VB.htm)

## Remarks

If developing a C++ application, use [swPartPromptBodiesToKeepNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
