---
title: "DPartDocEvents_SuppressionStateChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_SuppressionStateChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_SuppressionStateChangeNotifyEventHandler.html"
---

# DPartDocEvents_SuppressionStateChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the suppression state of a feature changes.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_SuppressionStateChangeNotifyEventHandler( _
   ByVal Feature As Feature, _
   ByVal NewSuppressionState As System.Integer, _
   ByVal PreviousSuppressionState As System.Integer, _
   ByVal ConfigurationOption As System.Integer, _
   ByRef ConfigurationNames As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_SuppressionStateChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_SuppressionStateChangeNotifyEventHandler(
   Feature Feature,
   System.int NewSuppressionState,
   System.int PreviousSuppressionState,
   System.int ConfigurationOption,
   ref System.object ConfigurationNames
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_SuppressionStateChangeNotifyEventHandler(
   Feature^ Feature,
   System.int NewSuppressionState,
   System.int PreviousSuppressionState,
   System.int ConfigurationOption,
   System.Object^% ConfigurationNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Feature`: [Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) whose suppression state changed
- `NewSuppressionState`: New suppression state for the feature as defined by [swFeatureSuppressionAction_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureSuppressionAction_e.html)
- `PreviousSuppressionState`: New suppression state for the feature as defined by [swFeatureSuppressionAction_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureSuppressionAction_e.html)
- `ConfigurationOption`: Configuration option as defined by [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `ConfigurationNames`: Array of configurations in which the suppression state of the feature changes

## VBA Syntax

See [SuppressionStateChangeNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~SuppressionStateChangeNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartSuppressionStateChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
