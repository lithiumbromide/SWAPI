---
title: "DAssemblyDocEvents_FeatureSketchEditPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_FeatureSketchEditPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FeatureSketchEditPreNotifyEventHandler.html"
---

# DAssemblyDocEvents_FeatureSketchEditPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user program when the user edits the definition of a sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_FeatureSketchEditPreNotifyEventHandler( _
   ByVal EditFeature As System.Object, _
   ByVal featureSketch As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_FeatureSketchEditPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_FeatureSketchEditPreNotifyEventHandler(
   System.object EditFeature,
   System.object featureSketch
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_FeatureSketchEditPreNotifyEventHandler(
   System.Object^ EditFeature,
   System.Object^ featureSketch
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EditFeature`: [Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) that contains the sketch
- `featureSketch`: Edited [sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html)

## VBA Syntax

See [FeatureSketchEditPreNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~FeatureSketchEditPreNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyFeatureSketchEditPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

If the sketch is not part of a feature, then the editFeature object is NULL.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
