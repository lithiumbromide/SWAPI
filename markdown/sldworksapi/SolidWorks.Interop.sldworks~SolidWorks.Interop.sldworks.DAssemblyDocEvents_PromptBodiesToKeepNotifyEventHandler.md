---
title: "DAssemblyDocEvents_PromptBodiesToKeepNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_PromptBodiesToKeepNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_PromptBodiesToKeepNotifyEventHandler.html"
---

# DAssemblyDocEvents_PromptBodiesToKeepNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Generated when a body is cut into multiple bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_PromptBodiesToKeepNotifyEventHandler( _
   ByVal Feature As System.Object, _
   ByRef Bodies As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_PromptBodiesToKeepNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_PromptBodiesToKeepNotifyEventHandler(
   System.object Feature,
   ref System.object Bodies
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_PromptBodiesToKeepNotifyEventHandler(
   System.Object^ Feature,
   System.Object^% Bodies
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Feature`: [Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)
- `Bodies`: Array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [PromptBodiesToKeepNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~PromptBodiesToKeepNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyPromptBodiesToKeepNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
