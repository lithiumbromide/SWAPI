---
title: "DPartDocEvents_FeatureSketchEditPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_FeatureSketchEditPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FeatureSketchEditPreNotifyEventHandler.html"
---

# DPartDocEvents_FeatureSketchEditPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user program when the user edits the definition of a sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_FeatureSketchEditPreNotifyEventHandler( _
   ByVal EditFeature As System.Object, _
   ByVal featureSketch As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_FeatureSketchEditPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_FeatureSketchEditPreNotifyEventHandler(
   System.object EditFeature,
   System.object featureSketch
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_FeatureSketchEditPreNotifyEventHandler(
   System.Object^ EditFeature,
   System.Object^ featureSketch
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EditFeature`: [Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) that contains the sketch
- `featureSketch`: Edited [sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html)

## VBA Syntax

See [FeatureSketchEditPreNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~FeatureSketchEditPreNotify_EV.html).

## Remarks

The interface pointer is passed as an IDispatch. You then have to do a QueryInterface for the ISketch interface. If the sketch is not part of a feature, then EditFeature is NULL.

If developing a C++ application, use [swPartFeatureSketchEditPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
