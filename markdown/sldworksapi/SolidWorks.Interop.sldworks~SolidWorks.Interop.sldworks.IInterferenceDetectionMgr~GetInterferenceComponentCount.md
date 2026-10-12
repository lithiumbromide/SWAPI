---
title: "GetInterferenceComponentCount Method (IInterferenceDetectionMgr)"
project: "SOLIDWORKS API Help"
interface: "IInterferenceDetectionMgr"
member: "GetInterferenceComponentCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceComponentCount.html"
---

# GetInterferenceComponentCount Method (IInterferenceDetectionMgr)

Calculates and gets the number of interfering components.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetInterferenceComponentCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IInterferenceDetectionMgr
Dim value As System.Integer

value = instance.GetInterferenceComponentCount()
```

### C#

```csharp
System.int GetInterferenceComponentCount()
```

### C++/CLI

```cpp
System.int GetInterferenceComponentCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of interfering components

## VBA Syntax

See [InterferenceDetectionMgr::GetInterferenceComponentCount](ms-its:sldworksapivb6.chm::/sldworks~InterferenceDetectionMgr~GetInterferenceComponentCount.html).

## Remarks

Call this method before calling [IInterferenceDectectionMgr::IGetInterferenceComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IInterferenceDetectionMgr~IGetInterferenceComponents.html).

## See Also

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.html)
[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.html)
[IInterferenceDetectionMgr::GetInterferenceComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceComponents.html)
[IInterferenceDetectionMgr::MakeInterferingPartsTransparent Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~MakeInterferingPartsTransparent.html)
[IInterferenceDetectionMgr::NonInterferingComponentDisplay Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~NonInterferingComponentDisplay.html)
[IInterferenceDetectionMgr::TreatSubAssembliesAsComponents Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~TreatSubAssembliesAsComponents.html)
[IInterference::GetComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~GetComponentCount.html)
[IInterference::IGetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~IGetComponents.html)
[IInterference::Components Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~Components.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
