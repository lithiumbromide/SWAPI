---
title: "DAssemblyDocEvents_FeatureEditPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_FeatureEditPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FeatureEditPreNotifyEventHandler.html"
---

# DAssemblyDocEvents_FeatureEditPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user program when the user edits the definition of a selected feature.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_FeatureEditPreNotifyEventHandler( _
   ByVal EditFeature As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_FeatureEditPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_FeatureEditPreNotifyEventHandler(
   System.object EditFeature
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_FeatureEditPreNotifyEventHandler(
   System.Object^ EditFeature
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EditFeature`: Edited [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) definition

## VBA Syntax

See [FeatureEditPreNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~FeatureEditPreNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyFeatureEditPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
