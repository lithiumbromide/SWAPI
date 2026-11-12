---
title: "GetComponentCount Method (IInterference)"
project: "SOLIDWORKS API Help"
interface: "IInterference"
member: "GetComponentCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~GetComponentCount.html"
---

# GetComponentCount Method (IInterference)

Gets the number of components interfering with each other.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IInterference
Dim value As System.Integer

value = instance.GetComponentCount()
```

### C#

```csharp
System.int GetComponentCount()
```

### C++/CLI

```cpp
System.int GetComponentCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of components interfering with each other

## VBA Syntax

See [Interference::GetComponentCount](ms-its:sldworksapivb6.chm::/sldworks~Interference~GetComponentCount.html).

## Examples

[Run Interference Detection (C#)](Run_Interference_Detection_Example_CSharp.htm)
[Run Interference Detection (VB.NET)](Run_Interference_Detection_Example_VBNET.htm)
[Run Interference Detection (VBA)](Run_Interference_Detection_Example_VB.htm)

## Remarks

Call this method before calling [IInterference::IGetComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IInterference~IGetComponents.html).

## See Also

[IInterference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference.html)
[IInterference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference_members.html)
[IInterference::Components Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~Components.html)
[IInterferenceDetectionMgr::GetInterferenceComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceComponentCount.html)
[IInterferenceDetectionMgr::GetInterferenceComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceComponents.html)
[IInterferenceDetectionMgr::IGetInterferenceComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetInterferenceComponents.html)
[IInterferenceDetectionMgr::MakeInterferingPartsTransparent Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~MakeInterferingPartsTransparent.html)
[IInterferenceDetectionMgr::NonInterferingComponentDisplay Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~NonInterferingComponentDisplay.html)
[IInterferenceDetectionMgr::TreatSubAssembliesAsComponents Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~TreatSubAssembliesAsComponents.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
