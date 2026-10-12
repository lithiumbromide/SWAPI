---
title: "GetInterferenceComponents Method (IInterferenceDetectionMgr)"
project: "SOLIDWORKS API Help"
interface: "IInterferenceDetectionMgr"
member: "GetInterferenceComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceComponents.html"
---

# GetInterferenceComponents Method (IInterferenceDetectionMgr)

Calculates and gets the interfering components.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetInterferenceComponents() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IInterferenceDetectionMgr
Dim value As System.Object

value = instance.GetInterferenceComponents()
```

### C#

```csharp
System.object GetInterferenceComponents()
```

### C++/CLI

```cpp
System.Object^ GetInterferenceComponents();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of the interfering [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [InterferenceDetectionMgr::GetInterferenceComponents](ms-its:sldworksapivb6.chm::/sldworks~InterferenceDetectionMgr~GetInterferenceComponents.html).

## See Also

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.html)
[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.html)
[IInterferenceDetectionMgr::GetInterferenceComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceComponentCount.html)
[IInterferenceDetectionMgr::IGetInterferenceComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetInterferenceComponents.html)
[IInterferenceDetectionMgr::MakeInterferingPartsTransparent Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~MakeInterferingPartsTransparent.html)
[IInterferenceDetectionMgr::NonInterferingComponentDisplay Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~NonInterferingComponentDisplay.html)
[IInterferenceDetectionMgr::TreatSubAssembliesAsComponents Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~TreatSubAssembliesAsComponents.html)
[IInterference::GetComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~GetComponentCount.html)
[IInterference::IGetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~IGetComponents.html)
[IInterference::Components Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~Components.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
