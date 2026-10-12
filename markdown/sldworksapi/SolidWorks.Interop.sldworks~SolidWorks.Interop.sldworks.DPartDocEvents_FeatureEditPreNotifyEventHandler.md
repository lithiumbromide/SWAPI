---
title: "DPartDocEvents_FeatureEditPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_FeatureEditPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FeatureEditPreNotifyEventHandler.html"
---

# DPartDocEvents_FeatureEditPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user program when the user edits the definition of a selected feature.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_FeatureEditPreNotifyEventHandler( _
   ByVal EditFeature As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_FeatureEditPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_FeatureEditPreNotifyEventHandler(
   System.object EditFeature
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_FeatureEditPreNotifyEventHandler(
   System.Object^ EditFeature
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EditFeature`: Edited [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureEditPreNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~FeatureEditPreNotify_EV.html).

## Remarks

The interface pointer is passed as an IDispatch. You then have to do a QueryInterface for the IFeature interface. Next, call [IFeature::GetTypeName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetTypeName.html), and then call [IFeature::GetSpecificFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetSpecificFeature2.html).

If developing a C++ application, use [swPartFeatureEditPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this event.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
